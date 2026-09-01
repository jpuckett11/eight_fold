# L-05 — Upstream

**Status: WORKED, 2026-08-31. Federal funding side established [P]. State-level
normalisation NOT done. Not yet a finding.**

Opened at Jay Puckett's direction. Inherits SEVENFOLD Findings 51 and 52.

---

## 1. The question

SEVENFOLD Finding 52 **priced** prevention. It never checked **who is buying**.

- Nurse-Family Partnership full course, pregnancy to age two: **$4,000/year × 2.5
  years = $10,000** [P, Finding 52]
- CDC lifetime cost of one nonfatal child maltreatment case: **$830,928** [P, 2015
  dollars, Finding 52]
- **83 to 1.** One published cost divided by another. The program does not have
  to work often. It has to work **once in eighty-three times**.
- Finding 51 is why this sits in an addiction case at all: the attributable risk
  fraction for addiction to illicit drugs from adverse childhood experiences is
  **64%**, and the relationship holds across four birth cohorts back to 1900 —
  unmoved by every change in drug availability, drug law and drug messaging since.

**L-05 asks: at what level is prevention actually funded, and by whom.**

## 2. What is now established [P]

Federal home visiting money flows through **MIECHV** — the Maternal, Infant and
Early Childhood Home Visiting program, **Assistance Listing 93.870** — which is
the vehicle funding NFP and comparable models in every state.

Source: **USAspending.gov**, the federal award system of record. No key required.
596 award records, 2021 to present.
Exhibit: `exhibits/miechv/usaspending_miechv_awards_all.json`.

**Current-cycle awards, nearly all beginning 2025-09-30:**

| | |
|---|---|
| Jurisdictions funded | **56** |
| **Total, all jurisdictions** | **$480,065,168** |
| 50 states + DC | $470,542,815 |
| Largest | Texas, **$30,146,654** |
| Smallest state | North Dakota, **$1,294,162** |
| Territories | ~$1.4M-$1.7M each |

## 3. The arithmetic, on Finding 52's own unit costs [I, from P inputs]

At $4,000 per family per year:

| | |
|---|---|
| Family-years funded nationally | **120,016** |
| Equivalent full 2.5-year courses | **48,007** |
| Share of Finding 52's $4.9B full-coverage figure | **9.8%** |
| Share of the CDC $592B annual burden | **0.081%** |

**[I] The United States funds roughly one tenth of the prevention it has already
priced, against a harm it has already costed at $592 billion a year.**

One prevented case, at CDC's own $830,928, pays for **83 full courses**. Federal
spending on the input side of that problem is **$480 million**.

## 4. Instrument failure caught during this work — read before extending it

**The first pass produced a false finding and it nearly went in.**

USAspending's `spending_by_geography` endpoint, queried for FY2025, returned
**Mississippi at $882,329** — below Guam, below American Samoa, and below the
statutory $1,000,000 base-funding floor. A striking, quotable, publication-ready
number.

**It is wrong. Mississippi's actual current award is $3,983,699.**

That endpoint sums **obligations falling inside the fiscal-year window**, not award
face values. MIECHV awards begin **2025-09-30** — the last day of FY2025 — and run
two years. A window query therefore measures *award timing and draw-down schedules*,
not what a state receives.

**Two checks were run. Only the second caught it:**

- `scope=recipient_location` vs `scope=place_of_performance`: **agreed exactly.**
  This ruled out a grantee-headquarters artifact and produced false confidence.
- Pulling the **underlying award records** for the bottom-ranked states: this is
  what exposed it.

**[I] Lesson for EIGHTFOLD generally: two views of the same aggregation can agree
and both still be wrong. Only descending to record level tests an aggregate.**
Added to `METHOD.md` §3 reasoning.

## 5. What is NOT established

- **No per-birth or per-capita normalisation.** Absolute dollars are not comparable
  between Texas and Vermont. **The ranking above must not be read as generosity or
  neglect.** This is the single most important missing piece and it is what would
  turn the table into a finding.
- **State appropriations are not counted at all.** MIECHV is the federal stream
  only. Some states add their own money; some face matching requirements. **The
  national total is a floor, not a total.** Any claim of the form "state X spends Y
  on prevention" is unsupported until state budgets are read.
- **Model mix is unknown.** MIECHV funds several evidence-based models, of which
  NFP is one. Finding 52's $10,000 unit cost is NFP's. Applying it across the whole
  MIECHV total is an approximation and is labeled as one.
- **The 9.8% and 0.081% inherit every caveat on Finding 52's inputs**, including
  that $830,928 is in 2015 dollars and $592B is an annual national burden estimate,
  not an appropriations figure.
- **Nothing here establishes causation** between home visiting funding and
  addiction outcomes in any state.

## 6. Next steps, in order

1. **Births by state.** The Census PEP API returned empty on 2026-08-31 and may now
   require a key; CDC WONDER natality is the alternative. **Without this the table
   cannot be normalized and must not be published.**
2. **Read state budgets** for home visiting lines, starting where SEVENFOLD already
   holds budget documents: **Utah** (Finding 48 — $1,905,400 to probation, prisons,
   courts, crime labs) and **Tennessee** (Finding 49 — $0, plus an unfunded coroner
   mandate).
3. **Build the ratio that is the whole point of L-05:** per state, dollars to
   enforcement against dollars to prevention. SEVENFOLD has the enforcement side
   for two states. This lead now has the federal prevention side for all fifty.
4. **Check MIECHV reauthorisation status.** The appropriation is not permanent and
   the program is periodically reauthorized. A lapse is the largest single event
   this lead could detect, which argues for a watcher on the `tools/` pattern.
