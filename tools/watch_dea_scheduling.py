#!/usr/bin/env python3
"""Watch every DEA controlled-substance scheduling action, nationally.

This is EIGHTFOLD's core instrument, and it is a different kind of tool from
SEVENFOLD's watchers. Those follow one docket or two bills. This one follows a
CATEGORY: every scheduling action the Drug Enforcement Administration publishes,
on any substance.

Why a category watcher. SEVENFOLD Finding 55 establishes that enforcement selects
for the replacement, and Finding 56 that nobody counts what the previous action
did. Those are not facts about kratom. They recur on every action, which means the
same three questions can be asked every time:

    1. What harm figure is this action based on, and how was it counted?
    2. What treatment provision accompanies it?
    3. Which structurally adjacent compounds are NOT named, and on what basis?

A scheduling action is the moment those questions are answerable and on the record.
This watcher exists to make sure none of them passes unnoticed.

Source: the Federal Register API. Free, no key, authoritative, and it is the
publication of record -- an action is not effective until it appears there.

Run from cron, daily:
    31 6 * * *  /usr/bin/python3 /home/obsidian/case_eightfold/tools/watch_dea_scheduling.py

State to tools/.dea_scheduling.state, changes appended to
tools/dea_scheduling_watch.log. Exits 0 on no change, 10 on a new action.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, ".dea_scheduling.state")
LOG = os.path.join(HERE, "dea_scheduling_watch.log")
API = "https://www.federalregister.gov/api/v1/documents.json"

# Rules and Proposed Rules only. Notices are registrant actions -- importer and
# manufacturer applications, practitioner decisions -- and there are hundreds of
# them. Including them would bury the signal, which is the failure mode this
# watcher exists to avoid.
WANT_TYPES = ("Rule", "Proposed Rule")


def fetch():
    params = {
        "per_page": 100, "order": "newest",
        "conditions[agencies][]": "drug-enforcement-administration",
        "conditions[term]": "schedules of controlled substances",
        "conditions[publication_date][gte]": "2022-01-01",
        "fields[]": ["document_number", "title", "publication_date", "type",
                     "abstract", "html_url", "comments_close_on",
                     "regulations_dot_gov_info"],
    }
    url = API + "?" + urllib.parse.urlencode(params, doseq=True)
    out, page = [], 1
    while url and page <= 10:
        for attempt in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(
                        url, headers={"User-Agent": "OWG-eightfold/1.0"}), timeout=90) as r:
                    d = json.load(r)
                break
            except urllib.error.HTTPError as e:
                if e.code in (429, 503):
                    time.sleep(30); continue
                raise
            except Exception:
                time.sleep(10)
        else:
            return None          # a failed fetch must NOT read as "nothing new"
        out += d.get("results") or []
        url = d.get("next_page_url"); page += 1; time.sleep(0.4)
    return [x for x in out if x.get("type") in WANT_TYPES]


def classify(title):
    """Flag what kind of action this is, so the log says why it matters."""
    t = (title or "").lower()
    tags = []
    if "temporary placement" in t: tags.append("EMERGENCY")
    if "extension of temporary" in t: tags.append("extension")
    if "proposed" in t: tags.append("proposed")
    # Substance families already documented as substitution-driven in SEVENFOLD 55.
    for fam, pat in (("nitazene", r"nitazene|benzimidazole"),
                     ("fentanyl-related", r"fentanyl"),
                     ("benzo", r"azolam|azepam"),
                     ("synth-cannabinoid", r"pinaca|pica|cumyl|butica"),
                     ("kratom-scaffold", r"mitragyn|corynanth|MGM-1"),
                     ("metabolite", r"desmethyl|hydroxy|nor-|o-dsmt")):
        if re.search(pat, t, re.I): tags.append(fam)
    return tags


def main():
    docs = fetch()
    if docs is None:
        print("FETCH FAILED - result not usable, state left unchanged", flush=True)
        sys.exit(1)

    now = {d["document_number"]: {
        "title": d.get("title"), "date": d.get("publication_date"),
        "type": d.get("type"), "comments_close_on": d.get("comments_close_on"),
        "url": d.get("html_url")} for d in docs}

    old = {}
    if os.path.exists(STATE):
        try: old = json.load(open(STATE))
        except Exception: old = {}

    new_ids = sorted(set(now) - set(old), key=lambda k: now[k]["date"] or "", reverse=True)
    json.dump(now, open(STATE, "w"), indent=1, sort_keys=True)

    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    if not old:
        line = f"{stamp}  BASELINE  {len(now)} scheduling actions since 2022"
        with open(LOG, "a") as f: f.write(line + "\n")
        print(line); sys.exit(0)

    if not new_ids:
        line = f"{stamp}  no change  {len(now)} actions"
        with open(LOG, "a") as f: f.write(line + "\n")
        print(line); sys.exit(0)

    out = [f"{stamp}  NEW SCHEDULING ACTION(S): {len(new_ids)}"]
    for k in new_ids:
        n = now[k]
        tags = classify(n["title"])
        out.append(f"    {n['date']}  {n['type']}  {k}")
        out.append(f"      {' '.join(n['title'].split())[:150]}")
        if tags: out.append(f"      tags: {', '.join(tags)}")
        if n.get("comments_close_on"):
            out.append(f"      *** COMMENT PERIOD CLOSES {n['comments_close_on']} ***")
        out.append(f"      {n['url']}")
        out.append("      ASK: (1) what harm count is this based on, and how measured?")
        out.append("           (2) what treatment provision accompanies it?")
        out.append("           (3) which adjacent compounds are unnamed, and why?")
    block = "\n".join(out)
    with open(LOG, "a") as f: f.write(block + "\n")
    print(block)
    sys.exit(10)


if __name__ == "__main__":
    main()
