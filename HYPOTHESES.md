# EIGHTFOLD / HYPOTHESIS REGISTER

**Opened 2026-08-31.**

SEVENFOLD generated hypotheses and tested them inside findings. That worked because
the case was narrow. **EIGHTFOLD covers all substances, so a claim can survive for
weeks by being interesting rather than by being right.** This file is the guard.

## Rules

1. **A hypothesis is entered BEFORE it is tested.** With its test and its
   disconfirming evidence written down first. A hypothesis entered after the data
   is a conclusion wearing a costume.
2. **Every entry names what would kill it.** If nothing would, it is not a
   hypothesis and does not belong here.
3. **A hypothesis is never cited.** Only a finding is citable. Status stays
   `OPEN`, `SUPPORTED`, `REFUTED` or `UNTESTABLE` and the file records which.
4. **Refuted stays in the file.** Deleting a dead hypothesis destroys the record
   that we were wrong about it, which is the part worth keeping.
5. **Whose idea it was gets recorded.** Not for credit — so that when a hypothesis
   is confirmed by the person who proposed it, the confirmation bias is visible.

---

## H-01 — Availability without supervision drives severity

**Status: SUPPORTED, with the causal direction unresolved. → EIGHTFOLD Finding 01.**
**Proposed by Jay Puckett, 2026-08-31:** *"any type of substance abuse disorder
becomes severe when things become so available."*

**Refined form tested:** it is not availability alone but availability outside a
clinical structure that predicts severity.

**Test:** compare severe-disorder rates within a drug class, split by access mode.

**Result [P, NSDUH 2024]:** opioid use disorder from misuse **37.1% severe** vs
from prescribed use **5.8%** (6.4x). CNS stimulants **48.3%** vs **5.1%** (9.5x).
Alcohol — maximally available, legally supplied — **19.2%**, below both misuse
columns.

**What would have killed it:** no severity difference between access modes, or
alcohol showing the highest severity of all. Neither occurred.

**What remains open:** reverse causation. Severity may drive access mode rather
than the reverse. **Not resolvable with cross-sectional data.** The longitudinal
study that would settle it does not exist, and its absence is itself reportable.

---

## H-02 — Enforcement selects for the more lethal replacement

**Status: SUPPORTED at national scale. → SEVENFOLD Finding 55.**

**Test:** does a supply-side intervention that succeeds against its target reduce
total harm?

**Result [P]:** OxyContin reformulation 2010 cut misuse ~40%. Heroin deaths
**3,036 → 15,469** by 2016. Powell & Pacula (NBER 26988): "the transition to illicit
markets spurred by reformulation led to growth in the overall overdose rate to
unprecedented levels."

**What would kill it:** a supply-side action followed by a sustained fall in total
overdose mortality with no substitution. **Candidate test case: the 2026 fentanyl
potency decline.** If overdose deaths fell in 2024-25 because of reduced potency
rather than substitution, that is evidence the loop can break. **Not yet examined.**

---

## H-03 — The untreated population is the market, not a byproduct

**Status: OPEN. Central claim of the case and the least tested.**
**Proposed by Jay Puckett, 2026-08-31:** *"a country that leaves 42 million behind."*

**Claim:** a dependent, untreated population is what guarantees a buyer for each
successive substance. Demand is not incidental to the substitution engine; it is
its precondition.

**Test, and it is hard:** does treatment availability predict the speed or size of
substitution uptake? Compare jurisdictions with materially different treatment
capacity against the arrival curve of a new substance.

**What would kill it:** substitution proceeding at the same rate in
high-treatment-capacity jurisdictions as in low. That would mean the market finds
buyers regardless and the demand-side argument is rhetorical.

**Why it matters that this is untested:** it is the moral center of the case and
the part most likely to be believed without evidence, including by us.

---

## H-04 — The patent record is the only early-warning channel

**Status: OPEN. Instrument built, not yet validated. → L-07.**

**Claim:** manufacturing claims appear years before a substance reaches consumers,
and every downstream channel — adverse events, lobbying, retail observation —
requires the harm to already exist.

**Measured lead time so far [P]:** 9-OH manufacturing claim filed **2023-09-20**;
federal assessments as of 2026-08-31: **zero**. ~3 years.

**Test:** for substances scheduled 2022-2026, was there a prior manufacturing or
process patent, and how long before? `exhibits/dea_scheduling/` now holds 139
scheduling actions to work against.

**What would kill it:** most scheduled substances having no prior patent. That
would mean the channel is real for semi-synthetics and useless for the designer
compounds that dominate the emergency-scheduling list.

**[I] Prediction worth recording now, so it can be scored later:** the nitazenes
will show a *weak* patent signal, because they were synthesised in the 1950s and
require no new IP. If so, H-04 holds only for semi-synthetics derived from a legal
botanical feedstock — a much narrower claim than currently stated.

---

## H-05 — The emergency pathway structurally cannot see adjacent compounds

**Status: SUPPORTED for one action. Generalization untested.**

**Result [P]:** DEA's Three Factor Analysis for the 2026-08-26 action considered
three compounds and their parent scaffold. Zero occurrences of
9-hydroxycorynantheidine, corynoxine, speciogynine, paynantheine, speciociliatine.
HHS's role under 811(h) was confirming no pending drug applications — a regulatory
status check, correctly performed.

**Claim:** this is not an oversight but a property of the mechanism. Neither
instrument in temporary scheduling asks what else in the source does the same thing.

**Test:** read the Three Factor Analyses for the other emergency actions since 2022
and count whether any considers a compound it did not schedule.

**What would kill it:** any Three Factor Analysis that surveys adjacent
uncontrolled compounds and explains why they were excluded. **One such document
refutes the structural claim entirely** and reduces the kratom case to a
one-off omission.

---

## H-06 — Prevention is underfunded relative to its own published return

**Status: SUPPORTED on federal funding. State funding uncounted. → L-05.**

**Result [P]:** MIECHV total **$480,065,168**, ~**9.8%** of the $4.9B needed for
full coverage of first-time Medicaid mothers, **0.081%** of the CDC's $592B annual
burden.

**What would kill it:** state appropriations closing the gap. **Not yet counted,
so the claim is currently a floor argument only.** Anyone stating "prevention is
underfunded" without the state numbers is overclaiming.

---

## H-07 — Criminalisation manufactures the stigma that keeps people out of treatment

**Status: OPEN. Entered 2026-08-31. The sharpest untested link in the case.**

**Claim:** enforcement action against a substance raises the social and legal cost
of being identified as someone who uses it, and that cost is a measured barrier to
treatment. If so, the two halves of this case are not merely adjacent policies that
fail separately — **the enforcement half actively suppresses uptake of the
treatment half.**

**The measured quantity it rests on [P, NSDUH 2024, Table A.56B]:** among adults
with an SUD who perceived an unmet need for treatment, **43.2% cited being worried
what people would think or say if they got treatment.** Alongside 38.9% who did not
know how or where to get it and 45.3% who thought it would cost too much.

**Test:** compare the stigma-barrier percentage, or treatment-seeking rates, across
jurisdictions or time periods that differ in criminalisation intensity for the same
substance. Tennessee (outright kratom ban, Public Chapter 950) against a
regulate-and-register state is the natural experiment closest to hand.

**What would kill it:** stigma-barrier rates that do not differ with
criminalisation intensity, or that move in the opposite direction. Also fatal:
if the barrier is dominated by general addiction stigma rather than legal risk, in
which case the enforcement link is decorative.

**Why it matters that this is untested:** it is the single claim that would join
EIGHTFOLD's two halves into one mechanism. **It is therefore the claim we are most
motivated to believe, and must be held to the highest standard.**

**Note against confirmation bias:** this hypothesis was generated by Aegis while
reading a passage that *undercut* the case's framing (that 95.6% of untreated
adults do not perceive a need for treatment). A hypothesis discovered while being
refuted is not thereby correct.

---

## H-08 — A deferred, inadequate reward cannot compete with an immediate, reliable one

**Status: OPEN. Entered 2026-08-31. Mechanism already established in the cited
literature; the economic half is untested.**
**Proposed by Jay Puckett, 2026-08-31:** *"give them something they are passionate
about. A cert is not a job that is paying right away, or even paying enough for
them to live comfortably."*

### Why this is not a restatement of the existing argument

SEVENFOLD's remediation already contains half of it and does not contain the other
half.

**Already established there [P]:** *"A trade is not a passion, and a certificate is
not an occupation."* And the empirical null — prison vocational education, propensity
score matched, *IJOTCC* 2023, DOI 10.1177/0306624X231159886: **"After matching,
there were no differences in any outcome between those who obtained vocational
certificates and the comparison group."**

**Not established there, and this is the new claim:** the certificate fails not only
because it is not an occupation, but because of **when it pays and how much**.

### The mechanism is already in the case's own source, unapplied

The behavioral-economic model SEVENFOLD cites (*Exp Clin Psychopharmacol* 2024,
DOI 10.1037/pha0000735) has three clauses:

> "**steep delay discounting**, overvaluation of [substance] reinforcement, and low
> reinforcement from [substance]-free activities"

**SEVENFOLD applies the third clause and never applies the first.** Steep delay
discounting means this population systematically devalues delayed rewards — that is
the defining measured feature of the disorder, not a metaphor. **A reward that
arrives months later, and then arrives small, is precisely the reward shape the
model predicts will fail.**

**[I] So the vocational line is not merely weak. It is the wrong shape of
reinforcer for the population it is aimed at, by the case's own model.**

### The internal test the existing package already contains

The $21,802 package holds one immediate-reward intervention and one deferred-reward
intervention, and their costs are inverted against their evidence:

| Component | Reward timing | Cost | Evidence |
|---|---|---|---|
| Contingency management | **immediate**, tangible, contingent | **$750** | dose-response curve established |
| Vocational certification | **deferred**, uncertain, then modest | **$4,000** | **no measured effect after matching** |

**The package spends 5.3x more on the intervention the evidence does not support.**

### Test

1. **Time to first income** after vocational placement in SUD and reentry
   populations. If median time-to-paycheck exceeds the window in which relapse risk
   is highest, the intervention cannot function as a competing reinforcer.
2. **Wage adequacy.** Placement wages against local living-wage thresholds. The
   claim is that even successful placement frequently fails to produce a livable
   income.
3. **Does outcome track wage adequacy rather than certification?** If programs
   that place people into adequately-paid work succeed where certificate-only
   programs do not, the discriminating variable is income, not credential.

### What would kill it

- Vocational programs producing good outcomes **at low wages** — that would mean
  the credential or the structure matters and income does not.
- Outcomes tracking certification **independently of** wage level.
- Delay discounting failing to predict program dropout in this population, which
  would undercut the mechanism rather than the observation.

### Design implication if it survives

**Any alternative reinforcer must be immediate and adequate, not deferred and
marginal.** That points at income support during transition, paid training rather
than unpaid credentialing, and placement judged on wage adequacy rather than
completion rates. It also argues for rebalancing the package toward the $750 line
and away from the $4,000 one.

**Caution.** This hypothesis is proposed by the case's own principal and is
congruent with the case's existing argument. That is exactly the condition under
which a claim gets adopted without testing. **It is currently mechanism plus
intuition, and the economic half has no data attached.**

### H-08 — evidence pulled 2026-08-31

**Supports the immediacy half [P]:**
- **Contingency management, attendance meta-analysis** (*J Subst Abuse Treat* 2022,
  PMID 34210566): d = **0.47** on attendance, and **"Frequency of rewards was
  significantly associated with larger effect sizes."** A dose-response on reward
  *frequency*. This is the strongest direct support for immediacy.
- **Individual Placement and Support (IPS)** is the model already built and tested:
  its defining components are **"zero exclusion, rapid competitive job search"** —
  place first, paid from the start, train on the job. Review for SUD populations
  (PMID 31782349): **"high evidence to support the application of IPS for persons
  with SUD."** Meta-analysis (PMID 35815640) measures **wages** as an outcome and
  finds IPS effective across every subgroup examined.

**WEAKENS the mechanism I originally gave this hypothesis [P]:**
- *J Subst Use Addict Treat* 2023, PMID 37072099, systematic review of 17 studies:
  **"Delay discounting at treatment entry was not consistently associated with
  substance use treatment outcomes"** (47% overall; 0-40% for most outcomes).
  Association depended heavily on measurement method (64% of adjusting-choice
  computer tasks vs 25-33% of k/AUC studies).
  **Aegis stated the delay-discounting mechanism as settled when entering H-08. It
  is not.** The population characteristic is well established; the inference that
  deferred-reward interventions therefore fail is not.

**Complicates it in an interesting direction [P]:**
- *Drug Alcohol Depend* 2019, PMID 31645013, N = 8,925 Iowa SUD clients: employment
  **at intake** predicted treatment completion, but **"the same employment variables
  were predictive of maintained and increased use at six-month follow-up."** What
  predicted recovery was **change** — months employed increasing (AOR 1.53,
  95% CI 1.34-1.75). **Having a job did not help. Gaining one did.**

**The closest randomized test of the residential-paid-trade model: JOB CORPS [P]**

`exhibits/employment/national_job_corps_study_final_report_ED498081.pdf`.
Random assignment, 15,386 applicants, 1994-96.

| | |
|---|---|
| Year-4 earnings gain, survey data | **12%** |
| Year-4 earnings level | ~**$10,000-11,000** (1995 dollars) |
| **Decay in administrative earnings impact, year 4 → year 7** | **68.3%** full sample |
| Same decay, ages 20-24 | **5.9%** |
| Benefit-cost required | year-4 impact to "persist for at least nine years without any decline" |
| Revised conclusion | **"benefits to society of Job Corps are smaller than the substantial program costs"** |

**[I] Reading, and the trap in it.** Job Corps delivered residential housing, a
stipend and trade training, and produced a wage of about $10,000-11,000 — **not an
adequate income** — with an impact that decayed 68.3% within three years. That is
*consistent* with H-08: an inadequate reward produced a non-durable effect.

**But consistency is not a test, and this is where H-08 could become
unfalsifiable.** If both program success and program failure are read as
confirming "adequacy matters", the hypothesis explains nothing. **The actual test
requires comparing programs that DO achieve adequate wages against those that do
not** — Job Corps alone cannot supply that, because it has no high-wage arm.

**The 20-24 subgroup is the most interesting unexplained result in the file:**
decay of 5.9% against 68.3% for the full sample. Age, or something correlated with
it, changes durability by an order of magnitude. Not yet explained.

**Still not pulled:** time-to-first-paycheck data, and wage adequacy against living
wage thresholds. **The economic half of H-08 remains unevidenced.**

### On the military analogy, entered 2026-08-31

Jay Puckett: *"what the military does can be done in the civ world, there are
already existing facilities like this."*

**Strong as design, weak as evidence, and the distinction matters.**

Strong as design: a military supplies the entire package in one institution — paid
from day one, housing, food, healthcare, a trade learned while being paid,
structure, identity, peer group. Basic training is place-first-train-while-paying.
That is IPS plus housing plus belonging.

Weak as evidence: **selection.** Militaries choose entrants and separate those who
fail — the exact bias that erased the vocational-certificate effect under propensity
matching (*IJOTCC* 2023). And post-service transition is itself a period of
concentrated harm, which complicates any simple "it works".

**The civilian analogues Jay refers to exist and are researchable:** therapeutic
communities (155 PubMed records), recovery housing and Oxford House (113),
Delancey Street, Homeboy Industries, conservation corps. **None has been pulled
yet.** These are the population-matched versions of the argument, where Job Corps
is only age-matched. **Next step for H-08.**

---

## H-09 — The non-livable wage is policy-imposed, not a program design failure

**Status: OPEN. Entered 2026-08-31. Unifies H-07 and H-08.**
**Proposed by Jay Puckett, 2026-08-31:** *"producing a non-livable wage is the
fault of the government stigmatizing these people, making them feel less than
human. How can anyone be expected to live or want to live when you can't even pay
your way?"*

**Claim.** The wage ceiling these programs run into is not a deficiency of the
training. It is imposed from outside by criminal records, occupational licensing
bars, collateral consequences and employer exclusion — all of which are downstream
of enforcement. **If so, H-08's "inadequate income" is not something better
program design can fix, because the same state that funds the program caps
what its graduates may earn.**

**[I] Why this matters structurally.** It joins the two halves of the case into one
mechanism. Enforcement produces the record; the record produces the wage ceiling;
the inadequate wage means the alternative reinforcer cannot compete; the person
returns to the substance; enforcement produces another record.

### First evidence, and it is not simple [P]

**Ban-the-Box** (*PLoS One* 2025, PMID 40238754), applicant-level data from one
employer before and after voluntary adoption:

> "the enactment of the BTB policy has **little or no association** with the rate
> at which individuals with criminal records survive the candidate assessment
> process and receive conditional employment offers. Indeed, our findings suggest a
> **modest indication of a negative association**..."

The authors' explanation: after losing access to criminal history, **"employers
increase their reliance on hiring criteria that are correlated to criminal
history."**

**[I] This supports the exclusion being real and structural, and refutes the simple
version of the remedy.** The barrier is not a checkbox on a form. Remove the box
and the exclusion re-routes through proxies. **That makes H-09 more serious, not
less** — an exclusion that survives its own prohibition is not a paperwork problem.

### What would kill it

- Wage outcomes for people with records matching otherwise-similar controls once
  employment is obtained. That would mean the barrier is access, not ceiling.
- Occupational licensing bars showing no measurable wage effect.
- Programmes achieving adequate wages **without** any change to collateral
  consequences — which would mean design can beat policy after all.

### Not yet pulled

Occupational licensing restrictions by state, the collateral-consequences
inventories, and wage-penalty audit studies. **H-09 currently rests on one BTB
paper and an argument.**

---

## H-08 — additional evidence, 2026-08-31: the Oxford House result

**This is the strongest counter-model in the file, and it cuts against the stipend
framing rather than for it.**

**Oxford House RCT** (*Addiction* 2007, PMID 17567399): n=150 discharged from
residential treatment, **randomly assigned** to an Oxford House or usual aftercare,
followed 24 months.

| Condition at 24 months | Substance abuse |
|---|---|
| Oxford House, **6+ months** | **15.6%** |
| Oxford House, under 6 months | 45.7% |
| Usual aftercare | **64.8%** |

Better outcomes also in **employment** and self-regulation.

**[I] The mechanism is not a stipend. Oxford Houses are self-governed, democratic,
have no professional staff, and residents PAY THEIR OWN RENT from their own
earnings.** There is no benefactor. Compare Job Corps — residential, stipend,
training, gains decaying 68.3% within three years.

**[I] Hypothesis worth entering separately if it survives scrutiny: paying your own
way may BE the reinforcer**, rather than an obstacle the program has to overcome.
That is congruent with Jay's framing — "how can anyone be expected to want to live
when you can't pay your way" — read as a statement about dignity and agency rather
than about cash flow. **Not yet formalised; needs a test that separates
self-support from housing stability, which the existing studies do not.**

**Scale caution [P]:** the 2025 systematic review of recovery housing
(*Front Public Health*, PMID 40115346) found only **five eligible studies** —
3 RCTs and 2 quasi-experimental — for what it calls "the most widely available form
of substance use disorder recovery support infrastructure." **The same sparse-
evidence pattern SEVENFOLD found for vocational training.**

**Who is actually in these settings [P]:** *Eur Addict Res* 2021, 5 residential
therapeutic communities, n=180 — **ADHD prevalence 51%, "nearly 10-fold compared to
the globally recorded values."**

### Note on the non-US search

Jay asked for non-US studies. **The specific searches run so far returned thin
results** — a Scandinavian/Italian residential-rehab query returned zero, and the
Europe/UK/Australia query returned nine records of mixed relevance. The TC records
retrieved are published in European journals but several describe non-US cohorts
(Czech TCs above). **This is not yet an adequate non-US search and should not be
reported as one.** EUDA / EMCDDA grey literature, already cited in SEVENFOLD
REMEDIATION §6, is the better route and has not been worked here.

---

## H-09 — evidence pulled 2026-08-31: the ceiling is in statute

**NCSL, "Barriers to Work: People with Criminal Records"**, verbatim
[P, `exhibits/barriers/`]:

> the National Inventory of Collateral Consequences of Conviction "catalogs over
> **15,000 provisions of law** in both statute and regulatory codes that limit
> occupational licensing opportunities for individuals with [criminal records]"

> "catalogs over **6,000 mandatory** occupational licensing consequences for people
> with criminal records"

> "**Licensed workers now comprise nearly 25 percent of all employed Americans.**"

And the blanket-ban mechanism: "automatic prohibitions for people with criminal
records — particularly for felony convictions that are deemed 'violent' or
'serious'."

**[I] This converts H-09 from an argument into a measurement.** A quarter of the
American labor market requires a license. Fifteen thousand legal provisions limit
access to those licences for people with records, and **six thousand of them are
mandatory** — not discretionary, not case-by-case, automatic.

**So the wage ceiling is not an emergent property of employer prejudice. A
substantial part of it is written down, by governments, as law.** A program that
trains someone for an occupation they are statutorily barred from entering has not
failed at training. It has been overruled.

**And Ban-the-Box shows why the obvious fix does not work:** removing the question
produced "little or no association" with hiring and "a modest indication of a
negative association," because employers fall back on correlated proxies. **The
statutory bar and the informal exclusion are two separate mechanisms and removing
one does not touch the other.**

**Unresolved and recorded rather than smoothed over:** a search summary gave
"more than 40,000" total collateral consequences and "10,000-plus" licensing
consequences; NCSL's captured document says over 15,000 licensing provisions.
**Not reconciled. Use the NCSL figures. The 40,000 is [S] unverified** — the NICCC
homepage carries no aggregate counts and its CSG domain did not resolve.

---

## H-10 — Contribution, not income, is the active ingredient

**Status: PARTIALLY SUPPORTED. Written up as EIGHTFOLD Finding 02, 2026-08-31.
A better-specified form of H-08. See the Oxford House and mediation sections at the
end of this file.**
**Proposed by Jay Puckett, 2026-08-31:** *"when they can pay their own way and
contribute they become a meaningful part of society, which in turn gives them the
drive and the want to continue not to relapse, because then they don't have to
worry about imposter syndrome — they are doing something."*

**Claim.** The operative variable is not the size of the paycheque but what earning
it makes the person: a contributor rather than a recipient. Income is the vehicle;
**legitimacy and agency are the reinforcer.** A stipend, a grant or a subsidised
placement may fail precisely because it is given — it confirms the recipient status
rather than dissolving it.

**Why this is the better-specified version of H-08.** H-08 predicts that adequate,
immediate income works. H-10 predicts something sharper and distinguishable: that
**self-supported** income outperforms **equivalent granted** income. Those two make
different predictions and can be told apart.

**The natural experiment already in the file [P]:**

| | Job Corps | Oxford House |
|---|---|---|
| Model | residential, **stipend received** | self-governed, **residents pay own rent** |
| Staff | professional | **none** |
| Design | randomized, n=15,386 | randomized, n=150 |
| Result | 12% year-4 gain, **68.3% decay** by year 7; revised benefit-cost: benefits < costs | **15.6%** substance abuse at 24 months (6+ mo) vs **64.8%** usual aftercare |

**[I] Same population domain, opposite reward structures, opposite durability.**
Not a controlled comparison — different populations, eras, outcome measures and
sample sizes — **but it is the shape H-10 predicts, and it is the shape H-08 alone
does not explain**, since Job Corps supplied income and housing and still decayed.

**It is measurable, and that is the main practical point [P].** The PhenX Toolkit
released 15 recommended recovery protocols in 2025 (*Drug Alcohol Depend* 2026,
PMID 42501516), including validated measures for **recovery identity** and
**recovery capital**. **"Do they experience themselves as a contributing member"
is not a soft construct — it has a pre-vetted instrument.**

**Test.** Compare self-supported against granted-income conditions, holding total
income and housing constant, with recovery identity as a mediator. If H-10 holds,
recovery identity mediates the outcome and the *source* of income predicts it
better than the *amount*.

**What would kill it.**
- Outcomes tracking income amount, with source making no difference once amount is
  controlled. That would collapse H-10 back into H-08.
- Recovery identity failing to mediate.
- Oxford House's effect being explained by selection or by housing stability alone.
  **The 2007 trial randomized assignment, which helps, but residents still choose to
  stay — and the headline contrast is between people who stayed 6+ months and those
  who did not.** That is not random. **This is the most serious threat to the
  reading above and it is not resolved.**

**Bias note.** Proposed by the case's principal, congruent with the case's argument,
and emotionally compelling. **Those are three reasons to hold it harder, not
softer.** The 6-month self-selection problem above must be answered before H-10 is
cited anywhere.

---

## H-10 — the Oxford House literature, pulled 2026-08-31

**The confound I raised is substantially answered, and the comparison H-10 needed
now has numbers on both sides.**

### 1. The randomized result exists, independent of length of stay [P]

My objection was that the 15.6% / 64.8% headline compares people who *stayed* 6+
months against those who did not — self-selected. **That objection does not apply
to the intent-to-treat comparisons, which also favor Oxford House:**

- *J Subst Abuse Treat* 2013, PMID 22498012: "participants in the **Oxford House
  condition were significantly more likely to remain continuously abstinent**
  throughout the course of this randomized clinical trial."
- *Adv Dual Diagn* 2016, PMID 27158265: randomized to therapeutic community vs
  Oxford House vs usual care; residential conditions showed significant reductions
  in psychiatric severity. **n = 39, small.**
- *N Am J Psychol* 2011, PMID 23357959: n = 150 randomized, 75 OH vs 75 usual care.

**The length-of-stay split should still not be quoted as if it were the randomized
result.** Two different comparisons, and only one is protected by randomization.

### 2. The cost-benefit, and it is the direct counterpart to Job Corps [P]

*Eval Program Plann* 2012, PMID 22054524. Cost-benefit built on the RCT, OH n = 68
vs usual care n = 61:

> "the **net benefit of an OH stay was estimated to be roughly $29,000 per person
> on average.** Bootstrapped standard errors suggested that the net benefit was
> **statistically significant.**"

| | Job Corps | Oxford House |
|---|---|---|
| Model | stipend **received**, professional staff | **self-supporting**, no staff |
| Economic verdict | **"benefits to society... smaller than the substantial program costs"** | **+$29,000 per person, statistically significant** |

**[I] Same domain. Opposite reward structure. Opposite economic verdict.** This is
the cleanest support H-10 has.

### 3. Self-run beat staff-run, which is H-10's specific prediction [P]

*Front Public Health* 2025 systematic review, PMID 40115346:

> "Recovery housing interventions performed better than continuing care as usual/no
> intervention on abstinence, **income, employment**, criminal charges... Recovery
> housing also **performed better than comparative interventions delivered in other
> types of residential settings (e.g., therapeutic communities)**."

**Therapeutic communities are staffed and professionally run. Oxford Houses are
not.** H-08 predicts only that residential support helps. **H-10 predicts the
self-run model beats the staffed one, and that is what the review reports.**

### 4. And the wage finding lands directly on H-09 [P]

*Alcohol Treat Q* 2016, PMID 27594760. 136 women in Oxford Houses nationwide:

> "There was a positive relationship between length of stay and wages. **Criminal
> history modified the association** between length of stay and wages, and **length
> of stay had a significantly greater impact on wages for women with criminal
> convictions.**"

**[I] The group facing the statutory wage ceiling documented in H-09 benefited MORE
from the self-run housing model than the group without records.** If that holds, it
is the single most policy-relevant result in this file: an intervention that costs
the state nothing partially offsets a barrier the state itself imposes.

**Caveat: cross-sectional regression, length of stay again not randomized.** The
selection problem that applies to §1's headline applies here too.

### 5. What complicates it [P]

*Subst Abus* 2016, PMID 26308507, survival analysis, N = 268: "**demographic and
employment variables did not significantly predict relapse risk.**" What did
predict it was severity of substance use disorder, psychiatric problems, and
time-varying alcohol abstinence self-efficacy.

**[I] That is awkward for any purely economic reading of H-08.** If employment does
not predict relapse, then income alone is not the mechanism — which is an argument
*for* H-10 over H-08, but also a warning that the active ingredient may be the
community and the self-efficacy rather than the paycheck. **Those are not the same
claim and this file should stop treating them as interchangeable.**

### 6. Status change

**H-10 moves from OPEN to PARTIALLY SUPPORTED.** The randomized comparisons, the
cost-benefit contrast with Job Corps, and the self-run-beats-staff-run finding are
three independent lines pointing the same way.

**It is NOT confirmed.** Every length-of-stay result remains self-selected, the
dual-diagnosis RCT is n = 39, and no study isolates *self-support* from *housing
stability* or *community*. That isolation is still the missing experiment.

### 7. The mediation model, and it resolves §5

**Proposed by Jay Puckett, 2026-08-31, in response to the §5 null:** *"when you
have the money to be self sufficient and live comfortably you are doing things,
making friends, colleagues, and you have something."*

**The claim.** Income is not a parallel factor to community — it is **upstream** of
it. Money does not reinforce directly. It buys the ability to participate, and
participation builds the network, and the network sustains recovery.

    income -> participation and activity -> social network -> recovery

**[I] This dissolves the contradiction in §5 rather than arguing around it.** The
survival analysis found employment did not predict relapse **directly**. Under a
mediation model that is the expected result: a variable acting entirely through a
mediator shows no direct effect once the mediator is in the model. **The null is
evidence for the pathway, not against it.**

### The pathway is already documented, in a randomized design [P]

*Alcohol Treat Q* 2016, PMID 28484304. **270 justice-involved individuals with SUD,
randomized** into self-run Oxford Houses, a staffed therapeutic community, or usual
aftercare. Important Persons and Activities instrument, five waves over two years:

> "Reading/Writing activities, and Exercise/Sports activities, were most reported at
> baseline. **By Wave 5, Education/Work and Interacting with Others were the most
> reported activities.**"

**Baseline activities are solitary. Two years later the top two are work and other
people.** That is the shift the mediation model predicts, measured with a validated
instrument in a randomized sample.

### And the participants say the same thing in their own words [P]

*Work* 2017, PMID 28582944, women in sober-living homes across 20 urban areas:

> "Employment is important to women in substance abuse recovery, **not only as a
> means for financial support, but also as a life priority.**"

> "**employer scheduling practices, low-level positions, and lack of employment
> supports impact recovery.**"

**[I] "Low-level positions" is the wage-adequacy claim of H-08, stated by the
people it is about, as a thing that impedes recovery** — not merely as a financial
inconvenience.

### What this changes about the tests

The tests in H-08 and H-10 were written to compare outcomes against income amount
and income source. **They should instead specify the mediator.**

- Measure **participation and network** (Important Persons and Activities
  instrument, and the PhenX recovery-capital and recovery-identity protocols).
- Expect employment to show **no direct effect** on relapse. Under this model that
  is a prediction, not a disappointment.
- **The discriminating test:** does income predict network growth, and does network
  growth predict recovery? If income predicts recovery **without** predicting
  network, the mediation model is wrong and H-08's direct-economic reading returns.

### The honest position

**[I] This is now a coherent model that fits every result in this file** — the
Job Corps decay, the Oxford House cost-benefit, the self-run-beats-staffed finding,
the wage effect concentrated in women with criminal records, and the employment
null.

**A model that fits everything is also the model most at risk of being
unfalsifiable.** The mediation test above is written specifically so it can fail.
**Nobody has run it. Until someone does, this is a well-supported story and not a
finding.**

---

## H-11 — Ownership is the strongest form of "your money builds something that is yours"

**Status: OPEN. Premise PARTIALLY CONTRADICTED on first check. Entered 2026-08-31.**
**Proposed by Jay Puckett, 2026-08-31:** *"it's like the feeling of buying your first
home — it's yours, your money isn't going to someone else. That is something the
younger generations are experiencing at a lower rate. I wonder if this correlates to
increased substance use."*

**Why it belongs here.** H-10 holds that the reinforcer is contribution rather than
income — being a builder rather than a recipient. **Homeownership is the limit case
of that distinction.** Rent is money leaving; a mortgage is money accruing to you.
If H-10 is right about the mechanism, ownership should be its strongest expression,
and its withdrawal from a generation should be visible.

### The premise check, run FIRST, and it does not fully support the claim [P]

NSDUH 2024, past-year SUD by age, `exhibits/nsduh/`:

| Age | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|
| 12-17 | 9.2 | 8.7 | 8.5 | **7.8** |
| 18-25 | 26.2 | 27.8 | 27.1 | **25.9** |
| 26+ | 16.2 | 16.6 | — | **16.4** |
| all 12+ | 16.7 | 17.3 | 17.1 | **16.8** |

**Adolescent SUD is DECLINING. Young-adult SUD is flat to slightly down. Overall
prevalence shows no change.** In the 2021-2024 window, substance use is **not**
rising in the cohorts losing access to ownership.

**[I] The trend half of the hypothesis is not supported by the most recent data.**
Stating otherwise would be false and easily checked.

### What survives, and it is not trivial

**Cross-sectionally the pattern is exactly as predicted.** Adults 18-25 carry the
**highest SUD prevalence in the country — 25.9%, against 16.4% for everyone over
26** — and are the cohort furthest from ownership. Highest rate, lowest ownership,
same people.

**That is consistent with H-11 and proves nothing.** Age itself predicts substance
use for a dozen reasons that have nothing to do with housing.

### What would need to be true, and what would kill it

**Test.** Homeownership rate by age cohort against SUD prevalence by the same
cohort, over a long enough window to see movement. Census Housing Vacancy Survey
gives ownership by age; NSDUH gives SUD by age. **Neither has been pulled for this
purpose yet.**

**What would kill it:**
- The 2021-2024 divergence continuing over a longer window — ownership falling while
  SUD falls too. **This is currently the observed pattern and it is evidence
  against.**
- The correlation vanishing once age, income and employment are controlled.
- Renters and owners at equal income showing equal SUD rates. **That is the actual
  test of the mechanism**, and it is an individual-level question, not a cohort one.

### The trap, named up front

**This is an ecological hypothesis, and ecological correlation is the weakest form
of evidence there is.** Two national trends moving together across decades can be
joined by anything. Over the period when young-adult homeownership fell, the drug
supply was transformed by prescription opioids, then heroin, then fentanyl
(SEVENFOLD Finding 55). **Any apparent ownership-SUD correlation across that window
is confounded by the single largest change in drug supply in American history.**

**[I] The individual-level version is the one worth testing** — do renters and
owners at matched income differ in SUD? That question is answerable, is not
ecological, and speaks directly to H-10's mechanism. **The generational version is
rhetorically powerful and evidentially weak, and this file should not use it.**


### H-11 addendum, 2026-08-31 — the ownership half is now on primary data; the causal claim is supported by the age gradient; the outcome half is corrected

Puckett, same day: *"they are the victims of the over reaction of banks and markets
to the 08 collapse."*

**Pulled the primary rather than agreeing.** Census HVS Table 19, homeownership by
age of householder, 1994-2026, in `exhibits/housing/`. Annual figures are unweighted
means of the four published quarters, computed here.

**a. The ownership premise is CONFIRMED [P] and understated.** Under 35: **43.1% in
2004 -> 34.6% in 2016 -> 36.0% in 2026.** Eight and a half points lost, one and a
half recovered in ten years, still **7.1 points below 2004**.

**b. The damage is monotonic in age, youngest worst, which is the shape of a credit
shock [P].**

| Cohort | Peak | Trough | Change | 2026 vs peak |
|---|---|---|---|---|
| 35-44 | 2005, 69.3 | 2015, 58.5 | **-10.8** | -8.3 |
| Under 35 | 2004, 43.1 | 2016, 34.6 | **-8.5** | -7.1 |
| 45-54 | 2004, 77.2 | 2016, 69.3 | -7.9 | -7.7 |
| 55-64 | 2004, 81.7 | 2016, 75.0 | -6.7 | -6.4 |
| **65+** | **2012**, 81.2 | 2018, 78.5 | **-2.7** | -2.7 |

**The 65+ rate peaked in 2012, in the middle of the crash.** People who already held
a mortgage kept the house. People who needed a new one did not get one. **[I] A shift
in what young people want does not produce a clean monotonic gradient by age with the
oldest cohort still rising. A shift in who can borrow does.**

**c. The sharpest number is the cohort transition [P].** Same life stage, eight years
apart, under-35 into 35-44:

| Under-35 in | Rate | 35-44 in | Rate | Gain |
|---|---|---|---|---|
| 1994 | 37.4 | 2002 | 68.5 | **+31.1** |
| 1998 | 39.4 | 2006 | 68.9 | **+29.5** |
| 2004 | 43.1 | 2012 | 61.5 | **+18.4** |
| 2008 | 41.0 | 2016 | 58.6 | **+17.6** |
| 2018 | 36.3 | 2026 | 61.0 | +24.7 |

**The cohorts whose prime buying years fell inside the credit contraction converted
into ownership roughly twelve points below the two cohorts before them.** They did
not defer and catch up. They reached 44 not having made it. The 2018 starter's +24.7
says the shock is fading, and that is stated here rather than left out.

**d. Two limits, stated before anyone else states them.**
- **"Overreaction" is a judgment, not a measurement. PULLED 2026-08-31 at Puckett's
  instruction; see FINDING 04.** The contraction is confirmed on Fed primary data:
  the 10th-percentile credit score at origination rose ~70 points and never came
  back, and lending below 660 went from 24% of dollars in 2006 to never above 10.2%
  since 2010. Urban's HCAI has the government channel at 9.8% risk tolerance against
  a **pre-bubble** norm of 19-23%. **But realized default on the tight book is only
  modestly better than the normal pre-bubble book (0.13-0.17 vs 0.14-0.20 quarterly
  transition to 90+), that measure is a stock not a vintage, and it is endogenous.
  The vintage series that would settle it is behind a login and was not obtained.
  "Overreaction" therefore stays [U].** The contraction itself does not.
- **Credit is not the only candidate.** Price-to-income, student debt, and delayed
  household formation move the same way over the same window and are not separated
  here.

**e. Census's own data caveat [P],** `exhibits/housing/census_hvs_press_2026q2.pdf`:
*"Homeownership data from 2020 was impacted by data collection changes brought about
by the COVID-19 pandemic."* **The 2020 spike is not a recovery** and nothing above
depends on it.

**f. The outcome half — CORRECTED, and it moves toward H-11.** This hypothesis was
entered on the reading that 18-25 carries the highest SUD prevalence at 25.9% against
16.4% for "26 or older." **That reading came off a bucket spanning ages 26 to 100.**
SAMHSA's detailed Table 5.3B gives: **21-25 at 28.8%, 26-29 at 27.9%, 30-34 at
23.0%**, falling to **8.0%** at 65+. See **Finding 03**.

**The peak-prevalence bands are 21-25 and 26-29 — the first-time-buyer window** — and
they are the same bands whose ownership transition collapsed. **The two curves
overlap tightly, where at the published resolution they appeared not to.**

**This does not rescue H-11 and must not be read as doing so.** The trend half stays
contradicted: adolescent SUD is falling (9.2 -> 7.8) while ownership falls. The
ecological fallacy is untouched — two population curves overlapping says nothing
about individuals. **The individual-level test (renters vs owners at matched income
and age) remains the only version worth running, and the generational framing remains
rhetorically powerful and evidentially weak.**
