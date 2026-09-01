# EIGHTFOLD / FINDING 04
## The bottom third of the mortgage market was closed in 2008 and has stayed closed for sixteen years. The contraction is measurable. Calling it an overreaction is one inference short, and the data that would close it is behind a login.

**Status:** The contraction is **CONFIRMED [P]** from Federal Reserve primary data.
The **overreaction** characterization is **[S] supported and [I] not proven**, and
this finding says exactly where it stops.
**Analyst:** Aegis, for Obsidian Watch Group. **Date:** 2026-08-31.
**Opened at Jay Puckett's claim:** *"they are the victims of the over reaction of
banks and markets to the 08 collapse"*, and at his instruction to pull the vintage
default data before writing anything, *"data makes a big difference either way."*

Exhibits in `exhibits/housing/`. Companion to the H-11 addendum in `HYPOTHESES.md`.

---

## 1. What was asked, and why it needed its own pull

The H-11 addendum established that homeownership among the under-35 fell 43.1% ->
34.6% and has recovered only to 36.0%, with the loss monotonic in age and the 65+
cohort peaking *during* the crash. **That establishes that the young stopped buying.
It does not establish why.**

Puckett named a cause. **The rule in this case file is that a named cause gets
tested, including his.** This finding is the test.

## 2. The contraction, measured [P]

Federal Reserve Bank of New York, Consumer Credit Panel / Equifax, August 2026.
`exhibits/housing/nyfed_hhdc_2026q2_underlying_data.xlsx`.

**a. Credit score at mortgage origination, 10th percentile** — the score at the
bottom edge of who gets a loan. Annual means of published quarters:

| Era | 10th pct | Median |
|---|---|---|
| 2004-2007 | **588** | 718 |
| 2011-2013 | **663** | 774 |
| 2024-2026 | **658** | 770 |

**The floor of the mortgage market rose about 70 points and has not come back down
in fifteen years.** Not in the 2020-2021 boom, not since.

**b. Share of origination dollars going to borrowers under 660:**

| Year | Share <660 |
|---|---|
| 2004 | 22.3% |
| 2005 | 21.6% |
| 2006 | **24.0%** |
| 2010 | 9.5% |
| 2012 | **6.9%** |
| 2019 | 8.4% |
| 2021 | **4.8%** |
| 2026 | 8.2% |

**In 2006 nearly a quarter of mortgage lending went to borrowers below 660. Since
2010 it has never once exceeded 10.2%.** In 2021, at the peak of a $4.5 trillion
origination year, it was **4.8%** — the most mortgage money ever lent in a single
year, and the smallest share of it reaching the bottom of the distribution.

**That is the door. It shut in 2008 and it has not reopened.**

## 3. Lenders' own stated risk tolerance is near a record low [S]

Urban Institute Housing Finance Policy Center, April 2026 chartbook,
`exhibits/housing/urban_hfpc_chartbook_202604.pdf`. The Housing Credit Availability
Index measures the share of loans lenders are **willing** to see default — their
tolerance, not their outcome. Urban's own words:

> "The total default risk the government loan channel is willing to take bottomed
> out at 9.6 percent in Q3 2013... reaching **9.8 percent in Q4 2025; nearly the
> lowest level on record, far below the pre-bubble range of 19 to 23 percent.**"

> "From Q2 2011 to Q4 2018, the total risk taken by the GSE channel more than
> doubled, from 1.4 percent to 3.3 percent. **This is still very modest by
> pre-crisis standards.**" Q3 2025: **2.4 percent.**

**Read the benchmark carefully. "Pre-bubble," 19 to 23 percent, is the normal market
of 1999-2003 — not the mania.** Seventeen years after the crisis, the government
channel is taking roughly **half** the default risk it took in an ordinary market,
and it is near the lowest reading the index has ever produced.

**Labeled [S] deliberately.** The HCAI is an index constructed by the Urban
Institute from eMBS, CoreLogic, HMDA and Inside Mortgage Finance. It is not a
government statistic and this finding does not present it as one.

## 4. And here is where it stops short of "overreaction" [P, and then [I]]

If the tightening were a pure overreaction, the loans written under it should have
performed **far** better than necessary. Transition of current mortgages into 90+
days delinquent, annual means of quarterly rates, same NY Fed file:

| Era | -> 90+ per quarter |
|---|---|
| 2003-2006 (normal book) | 0.20, 0.17, 0.16, **0.14** |
| 2009 (crisis peak) | **0.67** |
| 2015-2019 (tight book) | 0.17, 0.15, **0.13**, 0.17, 0.15 |
| 2021 | **0.10** |
| 2026 | 0.24 |

**The tight book performs modestly better than the normal pre-bubble book, not
dramatically better.** 0.13-0.17 against 0.14-0.20. **That is a weaker result than
section 3 would lead a reader to expect, and it is reported here because it is
weaker.**

**And it cannot settle the question anyway, for a reason that has to be stated
plainly: it is endogenous.** Defaults on the post-2010 book are low **because the
lending was restricted to people unlikely to default.** Low realized default under
tight credit is what tight credit produces. It is not evidence that the excluded
borrowers would have defaulted, and it is not evidence that they would not have.

**The measure is also a stock, not a vintage.** The quarterly transition rate
describes every mortgage outstanding in that quarter, whatever year it was written.
The 2004 reading of 0.17 is mostly pre-bubble loans behaving well; the bubble
vintages do not appear until 2008-2010, at 0.57-0.67. **Anyone using this series to
compare underwriting standards across eras is using the wrong instrument, and this
finding names that rather than quietly relying on it.**

## 5. What would settle it, and why it is not here

**The discriminating measure is realized cumulative default by ORIGINATION VINTAGE**
— the 2012 book followed for its whole life against the 2002 book followed for its
whole life. If the 2012 vintage came in far below the 1999-2003 norm, the standard
was tighter than the risk required, and "overreaction" is evidenced.

**It was pursued and not obtained.** Recorded in `exhibits/housing/CAPTURED_AT.txt`:
Freddie Mac's Standard Dataset Summary Statistics is served only through a
MicroStrategy BI portal, not as a file. Freddie's investor supplement pools
everything before 2022 into one "Prior Years" column. Fannie Mae's loan performance
data requires registration. Urban's data catalog returns 403 to a scripted fetch.
**The non-standard-product summary was retrieved and is the wrong population; it is
not used.**

**Secondary sources report the comparison running strongly in Puckett's direction**
— pre-2003 vintages around 2% cumulative default, 2007 around 13-14%, post-2009
vintages tracking below the pre-2003 baseline. **None of that is captured, verified
or relied on here.** It is the reason the next pull is worth doing, not a result.

**Until that series is in hand, "overreaction" stays [U] in this case file.** The
contraction is [P]. The near-record-low risk tolerance is [S]. The verdict on
whether it exceeded the risk is not established, and no OWG output should say it is.

## 6. What is established, and it is enough to matter

1. **The bottom of the mortgage market closed and stayed closed.** 24% of lending
   below 660 in 2006, never above 10.2% since 2010. [P]
2. **The cost landed on the young**, monotonically by age, with the oldest cohort
   unharmed and still rising through the crash. [P, H-11 addendum]
3. **Lenders are taking about half the default risk of a normal pre-bubble market,
   seventeen years later, and near the lowest on record.** [S]
4. **Realized default on the restricted book is only modestly better than normal**,
   which is a fact that cuts against the strong version of the claim and is recorded
   here for that reason. [P]

**[I] Points 1 and 3 together are the durable observation.** Whatever the correct
verdict on 2008, **the correction did not expire.** A generation that was in school
during the crisis has spent its entire adult life inside a credit standard written
in response to something it had no part in, and the standard has not loosened as the
risk receded. **The people who caused the losses were not the people who paid for
the caution.**

## 7. Puckett's closing point, which this finding does not dispute

> *"data makes a big difference either way we are still leaving them behind"*

**Correct, and the arithmetic in this file supports it in both directions.** If the
tightening was justified, then a large group of Americans is permanently excluded
from the main mechanism by which ordinary people accumulate anything, and nothing
has been built to replace it. If it was an overreaction, the same group is excluded
for no good reason at all. **The exclusion is the same fact under either verdict.
Only the excuse changes.**

**This is the same structure as Finding 03 and Finding 02.** The instrument to see
the problem exists. The people it would describe are not the ones who get looked at.

## 8. Action

1. **Pull realized cumulative default by vintage.** Fannie Mae's loan performance
   data needs an account; Freddie's needs the BI portal walked by hand. Both are
   free. **This is the single highest-value open pull in EIGHTFOLD's housing thread
   and it is a login, not a research problem.**
2. **Do not use "overreaction" in any OWG output** until item 1 lands.
3. **Carry section 4 with section 3, always.** Quoting the HCAI without the realized
   default series next to it overstates what is known.

---

## 9. Addendum, same day — Puckett: *"the reason it underperformed is the rates were so high people couldn't pay... in 08 I mean"*

**First, a correction to something in section 2 that reads wrong.** *"24 percent in
2006"* is **not an interest rate.** It is the share of mortgage **dollars** that went
to borrowers with credit scores under 660. **Nobody paid 24% on a mortgage.** The
figure is about who got lent to, not what it cost. Flagging it because it is the kind
of number that gets repeated once and never recovers.

### 9a. The simple version of the claim does not survive the rate series [P]

Freddie Mac Primary Mortgage Market Survey, full weekly history,
`exhibits/housing/freddie_pmms_historical_weekly.xlsx`. 30-year fixed, annual means:

| Year | 30-yr FRM |
|---|---|
| 2000 | 8.05 |
| 2003 | 5.83 |
| 2004 | **5.84** |
| 2005 | **5.87** |
| 2006 | **6.41** |
| 2007 | **6.34** |
| 2008 | **6.03** |

**Rates during the bubble were among the lowest in the history of the series to that
date.** The loans that blew up were written into a cheap-money environment, not an
expensive one. **The rate level is not the mechanism.**

### 9b. But the underlying mechanism is real, and it has a different name [P + [I]]

**What Puckett is describing is payment shock, and payment shock is a property of the
loan structure, not the rate level.** The 2/28 and 3/27 subprime ARM opened at a
teaser and reset to index plus margin; the option ARM recast when negative
amortization hit its cap. **A borrower can face an unpayable payment in a low-rate
year if the loan was built to do that.**

**There is a signal for it in the PMMS data, and it is the ARM discount [P].** The
spread of the 5/1 ARM under the 30-year fixed, which is what an ARM is supposed to
buy you:

| Year | 30-yr FRM | 5/1 ARM | discount |
|---|---|---|---|
| 2005 | 5.87 | 5.32 | **55 bp** |
| 2006 | 6.41 | 6.08 | **33 bp** |
| 2007 | 6.34 | 6.07 | 27 bp |
| 2012 | 3.66 | 2.78 | **88 bp** |
| 2016 | 3.65 | 2.88 | 77 bp |

**[I] In 2006 an adjustable-rate mortgage bought a borrower 33 basis points.** That
is not a deal. **Anyone taking adjustable-rate product at that spread was not
choosing it to save money. They were taking the only thing they could qualify for.**

**Stated limit:** PMMS surveys **prime conforming** lenders. It does not price
subprime 2/28s or option ARMs, where the teaser-to-reset gap was far larger. **These
numbers are a floor on the effect, not a measure of it.**

### 9c. Why this matters more than it first appears

Urban's HCAI decomposes default risk into **product risk** and **borrower risk** —
the loan's structure versus the borrower's credit. **Dodd-Frank and the Qualified
Mortgage rule effectively legislated the product risk out of existence.** Urban
reports it now running "well below 0.5 percent" in the portfolio and private-label
channel.

**[I] So if the 2008 defaults were driven substantially by loan structure, killing
the structure was the fix, and it worked. Borrower credit standards were tightened
on top of that, and never loosened.** On that reading the bottom third of the market
has spent sixteen years locked out as a second remedy for a failure the first remedy
already addressed. **That is Puckett's argument stated precisely, and it is the
strongest form of it.**

**It is [I], not established.** Confirming it needs the product-versus-borrower risk
decomposition as a numeric series. The chartbook renders it as an image; the
underlying HCAI data file sits at `datacatalog.urban.org`, which returns **HTTP 403**
to scripted fetch. **Added to the open-pull list beside the vintage default series.**

### 9d. The mechanism fits the current window — but NOT the way section 9d first said it. WITHDRAWN AND REPLACED

**Original claim, written earlier today and wrong in its emphasis:** that serious
delinquency among 18-29 mortgage borrowers is up 6.5-fold since 2021 and is "now the
highest of any working-age band," and therefore "the young are carrying it."

**Puckett pushed back: 18-29 is the band with higher addiction and a larger
population.** Both halves of his objection were checked. **One is wrong, one is right
in principle but cannot carry the weight, and the check found a third problem that is
mine.**

**i. Population size cannot do this [P].** NY Fed Page 25 is a **transition rate** —
the percentage of mortgage-holding 18-29s moving into 90+ days late. A larger cohort
puts more people in both the numerator and the denominator. **A bigger population
does not raise a rate.** It would matter for counts. This is not a count.

**ii. Addiction cannot explain the CHANGE, and the arithmetic is direct [P].** SUD
prevalence among 18-25, NSDUH Figure 36 Table, `exhibits/nsduh/`:

| 2021 | 2022 | 2023 | 2024 | SAMHSA trend |
|---|---|---|---|---|
| 26.2 | 27.8 | 27.1 | **25.9** | **No Change** |

**The exposure is flat and slightly down. The delinquency it is supposed to explain
rose 6.5-fold over the same period.** A flat cause does not produce a sixfold effect.

**On the LEVEL rather than the change, his objection is live and untested**, and it
runs the opposite way from the obvious guess: people with substance use disorders are
**less** likely to hold a mortgage at all, so the 18-29 mortgage-holding population is
selected toward the healthier end of its own cohort. **Which direction that bias
points is not established here and is not claimed.**

**iii. The real problem was mine, and it is a bigger one [P].** The rise is **not
young-specific at all.** Multiples from the 2021 trough to 2026:

| Band | 2021 | 2026 | multiple |
|---|---|---|---|
| 18-29 | 0.28 | 1.81 | **x6.6** |
| 30-39 | 0.27 | 1.66 | **x6.2** |
| 40-49 | 0.39 | 1.63 | x4.1 |
| 50-59 | 0.35 | 1.70 | x4.8 |
| 60-69 | 0.31 | 0.94 | x3.0 |
| 70+ | 0.27 | 0.83 | x3.1 |

**And the "highest working-age band" claim is a margin of 0.11 points on a nearly
flat distribution.** Spread across the 18-59 bands: **1.12 points in 2005, 0.42 in
2019, 0.18 in 2026.** The young premium, 18-29 over 40-49, was **1.83 to 1.89 through
2000-2006** and is **1.11 today** — historically **compressed**, not expanded.

**Calling 18-29 the highest band was reading a level as distinctive when the entire
distribution had moved. That is the "verify the instrument" failure this case file
keeps recording, committed again.**

**iv. What actually survives, and it still supports the rate mechanism [P].** The
gradient is not young-versus-old. It is **working-age versus retirement-age**:
every band from 18 to 59 rose **4.1 to 6.6 fold**; both bands over 60 rose **3.0**.
**People holding an old fixed-rate mortgage were largely insulated. People who bought
or refinanced into the 6-7% environment were not, at every working age.** Rates went
2.96% to 6.81%, and Urban records median DTI rising 39 to 41 and LTV 91 to 95 since
December 2021 while median FICO **rose** 738 to 750.

**Better borrowers, worse payments, across the whole working-age range.** That is the
payment-shock mechanism, and it is broader than the original claim, not narrower.

### 9e. And this strengthens section 4 rather than weakening it

Section 4 compared the tight book (2015-2019) against the normal book (2003-2006) and
found only modest outperformance. **If rate stress drives defaults, check the rates in
those two windows:** 2015-2019 averaged **3.65 to 4.54%**; 2003-2006 averaged **5.83
to 6.41%**.

**The tight book was underwritten into a materially cheaper rate environment than the
book it is being compared against.** So its modest outperformance is, if anything,
**flattered** by the comparison. **Section 4's caution stands, and this objection —
tested — makes it firmer.**

**That is the honest outcome of checking Puckett's claim: the simple version fails,
the mechanism is right, it applies to a different decade than he aimed it at, and
where it does apply it does not help the argument it was raised to support.**
