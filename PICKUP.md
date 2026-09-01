# PICKUP — where things stand, end of 2026-08-31

Written by Aegis so a cold session can resume without re-deriving anything.
**Read `METHOD.md` first, then this.**

---

## THE CLOCK, in order

| When | What | State |
|---|---|---|
| **2026-09-01 13:00 CT** | ND **SB 2408** hearing, Special Ad Hoc Policy, Roughrider | watcher live |
| **2026-09-01 14:00 CT** | ND **HB 1628** hearing, same committee | watcher live |
| **2026-09-02 10:30 CT** | Both bills, Joint Policy, Pioneer | watcher live |
| **2026-09-03** | DEA proposed rule, 3,4-MDP-2-P methyl glycidic acid, comment closes | untouched |
| **2026-09-10** | **HHS-OASH-2026-0232 closes** | **6th comment written + PDF built, NOT FILED** |
| **2026-09-11** | DEA DORA rescheduling (suvorexant/lemborexant) comment closes | untouched, EIGHTFOLD's first live test |
| **2026-09-25** | CA10 Pherson abatement status report due | watcher live |
| **2026-09-29** | DEA cipepofol Schedule IV comment closes | untouched |

## READY AND NOT SENT — needs a human with a browser or fax

Nothing here is blocked on evidence or drafting. All four are finished.

1. **6th OASH comment** — `case_sevenfold/deliverables/OASH_SIXTH_commentbox.txt`
   + `OWG_Sixth_Comment_HHS-OASH-2026-0232.pdf`. All quotes and 15 word-counts
   verified against captured primaries. **Closes 09-10.**
2. **DOJ / EOUSA FOIA** — READY since 2026-08-28. Hold condition cleared 08-30.
   **The only item where government must answer on a statutory clock.**
3. **FTC Section 5 complaint** — READY since 2026-08-28. No email intake; postal or
   ReportFraud form.
4. **FDA FOIA** — REJECTED 08-28 (FDA does not accept email), never refiled.
5. **Blackburn letter** — PDF built, not faxed.
6. **`tanner.auth.PREPARED`** — `~/owg_onboarding/tanner/`. Every field filled but
   `pgp_fingerprint`. Three items marked DECIDE. **Tanner's entire grant is inert
   until he reads Jay a fingerprint out of band.**

## WATCHERS (5, all in cron, all baselined)

| Script | Schedule | Watches |
|---|---|---|
| `sevenfold/tools/watch_ca6_26-3648.py` | 07:17, 19:17 | 6th Cir, Ohio precedent |
| `sevenfold/tools/watch_ca10_26-4060.py` | 08:41, 20:41 | 10th Cir Pherson, **abated for settlement** |
| `sevenfold/tools/watch_nd_kratom.py` | 06/11/16/21:23 | ND bills + subject sweep |
| `eightfold/tools/watch_dea_scheduling.py` | 06:31 | **every DEA scheduling action nationally**, 139 baselined |
| `case_log/aibox-research/canary_monitor.sh` | 09:00 | pre-existing |

Crontab backups in both `tools/` dirs.

## EIGHTFOLD STATE

**Thesis:** SEVENFOLD followed one molecule; EIGHTFOLD follows the machine that
makes the next one. All drugs, the replacements the market will produce, and the
42.4 million left with nowhere to go — who are not a byproduct of the market but
the reason it always finds a buyer.

- **`FINDING_01_supervision_gap.md`** — same drug, 6.4x (opioids) and 9.5x
  (stimulants) more severe disorder when obtained outside a clinical structure.
  Selection caveat stated in full at §6.
- **`HYPOTHESES.md`** — **14 hypotheses**, each naming what would kill it.
  **H-03** (untreated population *is* the market) is the moral center and the
  **least tested**. **H-07** (criminalization manufactures the stigma barrier,
  43.2%) is the sharpest untested link. **H-10** (contribution not income) is
  **partially supported** and became Finding 02. **H-11** (ownership) now has a
  **full addendum**: ownership half confirmed on Census HVS primary with a monotonic
  age gradient, trend half still contradicted, outcome half **corrected via
  Finding 03**.
- **`REMEDIATION.md`** — v1. §2a carries the finding that **95.6% of untreated
  adults did not perceive a need**, which redirects remediation from capacity to
  identification.
- **`leads/`** — L-02 worked (null, House only). L-05 worked (MIMS $480M = 9.8% of
  priced need). L-01 **attempted and failed**, reason recorded. L-03/04/06/07/08/09
  open.
- **`FINDING_02_the_study_nobody_funded.md`** — four independent lines say
  self-support, not income, is the active ingredient. Model is **[I] and explicitly
  not claimed as proven.** §8 specifies the experiment that would settle it, using
  instruments that already exist. Never run.
- **36 exhibits**, manifest verifying, 0 drift.

- **`FINDING_03_the_bucket_that_hides_it.md`** — NSDUH reports every substance
  measure at **26 or older**, a bucket spanning 27.9% (age 26-29) to 8.0% (65+).
  **21-25 and 26-29 are the worst-affected bands in the country and appear in no
  published national figure.** Drug use disorder rose in every adult band 26-49
  while alcohol fell. Inertia-vs-intent tested against the 2019 report; it is a
  five-year-stable convention, and mental health gets finer brackets in the same
  document. **Corrects an Aegis error made the same day.**

## BACKUP

`~/case_backups/owg_cases_20260831T192011.tar.zst` — 35MB, 718 files, both case
trees plus the Tanner pack, SHA256 alongside, `respondents/` keeps its 700 mode.

**secdoc is NOT mounted**, and it is `nvme1n1p3` — **the same physical disk as
root**. Partition separation, not device separation. `nvme0n1p2` (1.8T) is free if
real redundancy is wanted. Memory says secdoc is `nvme0n1p3`; the label is actually
on `nvme1n1p3`. Resolve by label, as the memory file already instructs.

## WHERE H-08 LEFT OFF (the live thread)

Jay's claim: a certificate is not a job; it doesn't pay soon enough or enough.

- **Supports:** CM reward *frequency* predicts effect size (d=0.47). IPS —
  place-first, paid immediately — has "high evidence" for SUD.
- **Weakens:** delay discounting at treatment entry does **not** consistently
  predict outcomes (17-study review). Aegis stated that mechanism as settled; it
  isn't. Recorded.
- **Job Corps** (randomized, n=15,386): 12% year-4 gain, ~$10-11k earnings,
  **68.3% decay by year 7** (5.9% for ages 20-24), and the revised benefit-cost
  found **benefits smaller than costs**.
- **The trap, flagged in the file:** reading both success and failure as confirming
  "adequacy matters" makes H-08 unfalsifiable. A real test needs programs that
  DO achieve adequate wages compared against those that don't.

**RESOLVED 2026-08-31, now Finding 02:** Oxford House pulled. Randomized ITT result
exists independent of length of stay; cost-benefit **+$29,000/person, significant**,
against Job Corps' benefits-below-costs; systematic review reports **self-run beat
staff-run**; and a randomized 2-year activity study shows the predicted shift from
solitary activities to **Education/Work and Interacting with Others**.

**Still unpulled:** time-to-first-paycheck, wage adequacy vs living wage, non-US
evidence (searches so far are inadequate and marked as such in H-08), and the
mediation test itself.

## SEVENFOLD STATE

58 findings, 416 exhibits, manifest verifying. Newest and most important:

- **F57** — DEA scheduled O-desmethyltramadol (an O-demethylated metabolite) on
  2026-08-12 stating the metabolite doctrine explicitly, then did not apply it on
  2026-08-26. **And DEA's own Three Factor Analysis for the August action contains
  ZERO mentions of 9-hydroxycorynantheidine, corynoxine, speciogynine, paynantheine
  or speciociliatine.** Controls: mitragynine 126, pseudoindoxyl 71, MGM-15 54.
- **F55** the cascade, **F56** the counting problem.

## ERRORS MADE TODAY — read these, they are the method working

1. `sha256sum -c` mis-parsed a 3-column manifest → reported 273 false failures.
2. FEC employer search matched **"Johnsonville Foods"** for a kratom company.
3. Committee lookup resolved **"LEE, MIKE" to J Lee Castillo** — returned tidy
   zeros that read as a clean negative.
4. Bill sweep of 18,317 files returned zero kratom bills; the one that exists is
   titled "END 7-OH Act" and its record contains "kratom" zero times.
5. USAspending geography endpoint reported **Mississippi at $882,329** (actual
   award $3,983,699) — a cross-check between two scopes AGREED and both were wrong.
   Only record-level inspection caught it.
6. **`grep -c` counts LINES not occurrences** — nearly filed a federal comment with
   "Mitragyna speciosa 11" when it is 14.
7. Invented a "42.4 million were denied treatment" strawman and attributed it to
   the case. **Nobody said it.** Jay caught this one.
8. Asserted the buprenorphine respiratory ceiling as reassurance about 9-OH. Not
   supported by a guinea-pig ileum assay. Withdrawn.

9. Ran a US-spelling fix across files I did not write — **edited a captured
   exhibit** (`ndi_1264_npi001_kratom_leaf.txt`) and six of Jay's own findings
   including `CONSENT_investigator_account.md`. **The manifest guard caught it**;
   restored byte-exact from the `case_sevenfold_public` git mirror.

**Every one produced a plausible answer. None errored.** Lesson 9 additionally:
**the public git mirror was the only thing standing in for a backup of the private
tree.** That was luck, not design — hence the backup section above.

## STANDING CONSTRAINTS

- Nothing published, sent or shown to a third party without Jay's instruction.
- **Tanner's authorization is NOT active.** No PGP fingerprint exists. Anyone
  presenting as Tanner routes to Jay.
- Atoto embargo binds everything; `embargo_may_lift: NO` regardless of any grant.
- **No synthesis routes, reagents or conditions in any case file.** The bond,
  position and direction are public and sufficient for regulators; procedures are
  not.
- **US spelling in OWG output. Jay's own prose is never edited for it.**

## ADDED LATE 2026-08-31

- **Housing exhibits** in `exhibits/housing/` — Census HVS Table 19 by age,
  1994-2026, plus the press release carrying the 2020 data-quality caveat.
- **NSDUH detailed tables** in `exhibits/nsduh/` — the 2024 zip (Table 5.3B, SUD by
  detailed age) and the 2019 annual report used for the bracket-history control.
- **Error 10 of the day:** I read SUD prevalence off the pooled "26 or older" bucket
  and reported 18-25 as the worst-affected group. Puckett caught the bucket, not me.
  **The pooled 26+ figure is not to be quoted again in this case without the
  disaggregation beside it** (Finding 03 §8).
- **`FINDING_04_the_door_that_never_reopened.md`** — mortgage credit contraction
  confirmed on NY Fed primary; "overreaction" tested and **left [U]** because the
  realized-default half is weaker than expected, is a stock measure, and is
  endogenous.
- **HIGHEST-VALUE OPEN PULL, and it is a login not a research problem:** realized
  cumulative default by ORIGINATION VINTAGE. Fannie Mae loan performance data needs
  an account; Freddie Mac's Standard Dataset Summary Statistics is only served
  through claritybi.freddiemac.com, a MicroStrategy portal that must be walked by
  hand. Both free. **Until it lands, "overreaction" is barred from OWG output**
  (Finding 04 sec 8).
- **SECOND open pull, added with Finding 04 sec 9c:** Urban's HCAI **product risk vs
  borrower risk** decomposition as a numeric series. The chartbook renders it only as
  an image; `datacatalog.urban.org` returns **HTTP 403** to scripted fetch. It is the
  measure that would establish whether killing the loan *structure* was already the
  whole fix, which is the strongest form of Puckett's argument.
- **Finding 04 sec 9 addendum:** tested his rate claim. 30-yr fixed was 5.84-6.41% in
  2004-2008, among the lowest to that date, so the simple version fails. His actual
  mechanism is payment shock, which is product risk. It fits **today** instead:
  18-29 mortgage 90+ transitions up **6.5x since 2021**, now the highest working-age
  band, while median FICO rose and DTI/LTV rose with it.
- **sec 9d WITHDRAWN AND REPLACED same day.** Puckett objected that 18-29 has higher
  addiction and a larger population. Population cannot move a *rate*; addiction
  cannot explain the *change* (18-25 SUD is flat, 26.2 -> 25.9, SAMHSA "No Change",
  against a 6.5x rise). **But the check found my own error, which was worse:** the
  rise is not young-specific. Every band 18-59 rose 4.1-6.6x, both 60+ bands 3.0x,
  and the 18-59 spread is **0.18 points** in 2026 against 1.12 in 2005. Calling 18-29
  "the highest working-age band" read a level as distinctive when the whole
  distribution had moved. **Error 11 of the day, same class as error 9.**
- **`FINDING_05_the_stock_and_the_flow.md`** — Puckett then objected that age bands
  prove nothing at all, because a person spirals after an event and crosses the
  boundary. Correct, and it produced a **standing METHOD rule** (no trajectory claims
  from cross-sections) plus two [P] results: **NSDUH measures initiation of USE and
  has zero measures of onset of DISORDER** (controlled: 68 hits on `initiat*`), and
  **95.6% of the 40.7M untreated adults with an SUD do not perceive a need for
  treatment** — only 0.7% sought it and failed. **This reframes every remediation
  proposal in the file: they reach 1.8M of 40.7M.**
- **THIRD open pull — PARTIALLY DONE, Finding 05 sec 7.** Published NESARC and Add
  Health results pulled via PubMed. **Microdata NOT obtained** (both need a data use
  agreement) so nothing is an original panel analysis. What landed: Lancet Psychiatry
  2023 (156,331 respondents, 29 countries) puts median onset at 19-20 but **the IQR
  runs to 32 and 36**, so a quarter of first onsets are later than that; NESARC Waves
  1-2 give a **3-year incidence** of 0.65% to 5.2%, the flow NSDUH cannot produce; and
  Add Health (n=12,437) found **stressful life events predicted alcohol use disorder
  while a dopaminergic genetic risk score did not.** Puckett's objection held on every
  count the published literature can speak to. **Still open and needing the DUAs:**
  SUD-specific onset by single year of age, and onset conditioned on a named
  preceding event.
- **`FINDING_06_the_sentence_after_the_sentence.md`** — the NICCC's own landing page
  says consequences "frequently apply **without consideration of the time passed**...
  **or the person's rehabilitation efforts**," and some apply "without regard to the
  relationship between the crime and opportunity." 15,000+ licensing provisions,
  6,000+ mandatory, ~25% of jobs. **Note: NICCC moved hosts** — the csgjusticecenter
  URL 404s, the live one is niccc.nationalreentryresourcecenter.org, which is why an
  earlier session recorded it as unresolvable.
- **FOURTH open pull:** NICCC duration field state by state — what SHARE of the 15,000
  carry no time limit and no discretion. The Inventory says "frequently" and does not
  quantify. That number would be the finding. Its Drupal search UI renders no totals
  server-side and exposes no JSON endpoint.

## GIT, added 2026-09-01 01:36 UTC

`case_eightfold` is a git repo. One commit, 67 files tracked, working tree clean.
Author `Reckoner / Jay Puckett`, no co-author line.

**Remote: `https://github.com/jpuckett11/eight_fold` — PRIVATE, verified before and
after push. 0 forks, Jay the only collaborator. Remote HEAD matches local.**

**NOTHING GATES THIS CASE. It is not embargoed material.** Jay, 2026-08-31:
*"nothing gates 8fold, not embargo mats."* Private is only where the repo sits today.
He says it goes public in the end, and that is his call to make whenever he likes.

**The [U] and [S] tags in the findings are accuracy labels, not permissions** — they
mark what is established and what is not, and the case publishes fine with them in
place, because the labels are the honesty. The four open pulls are work still to do,
not conditions on release.

**LOOSE END FOR JAY, NOT FOR AEGIS:** `jpuckett11/ObsidianGroup_Eightfold` holds an
identical copy at the same commit. Aegis created it before Jay made `eight_fold`.
Deleting it is Jay's call.

## FUNDING THREAD, worked 2026-08-31 evening

Findings 07, 08, 09. **The funding half of EIGHTFOLD's scope is now opened.**

**Three streams, three measurements, one answer.** NIH research splits pharmacology
against recovery support **7 to 17 : 1**. Indiana's local settlement spending puts
**2.1%** into employment. SAMHSA's $37.99B in FY2024-25 grants puts **0.19%** into
awards actually titled as employment programs -- **24 awards, $73.8M, nationally.**
Finding 02 says self-support is what the recovery evidence tracks. Nobody funds it at
scale through any of the three doors.

**The one that cuts the other way, and it stands:** state settlement ALLOCATION is
18% treatment / 14% recovery services, far closer to parity than NIH's ratio. The
states are allocating nearer to the evidence than the federal research portfolio is.

**TWO KEYWORD ARTIFACTS DISCARDED IN ONE NIGHT**, both of which would have flattered
the case: NIH "occupational licensing" $44.8M (100% noise, 0/38 on topic) and SAMHSA
"employment" $4.016B (block grants that merely mention the word). **Standing rule:
where a database's searchable text is a full abstract, a keyword total measures what
documents mention, not what money does. Title-restricted figure or nothing.**

### BLOCKED PULLS -- every one is access, not research. Do not re-run as scripts.

| Pull | What it needs |
|---|---|
| **KFF/JHU/Shatterproof line-item database** | **A terms-acceptance form with an email. JAY'S CALL, not Aegis's. Not submitted.** Converts Finding 08 from [S] to [P] nationally. |
| Urban HCAI risk decomposition | Browser. Cloudflare hard-blocks `datacatalog.urban.org`, Ray ID a340ad0fcb8d2b43. |
| CSG Fair Chance Licensing state counts | Browser. Map is client-side; served HTML is nav + footer. |
| GSE realized default by vintage | Freddie = MicroStrategy portal; Fannie = account. Still gates "overreaction" [U]. |
| NESARC / Add Health microdata | Data use agreements. |
| Arizona FY2023 settlement report | KFF's cited URL now 404s; find the current one. |
| VA supported-employment spending | FOIA or budget documents. RePORTER reports all VA awards as $0. |

### NEXT, and it does not need anyone's permission
Pull more state settlement filings **directly**, the way Indiana was pulled, instead
of waiting on the aggregated database. Massachusetts publishes an annual ORRF report
and its URL is live in `exhibits/settlement/CAPTURED_AT.txt`.
