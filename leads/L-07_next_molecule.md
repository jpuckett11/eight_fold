# L-07 — The replacement engine

**Status: OPEN, unworked. Opened 2026-08-31.** Not citable.

## The question

SEVENFOLD Finding 55 establishes the loop at national scale and Finding 20 catches
it mid-turn on one scaffold. **L-07 asks whether the loop can be watched in advance,
across all drug classes rather than one plant.**

Finding 20 s8a measured the lead time available: the manufacturing claim on the
unscheduled successor to 7-OH was filed **2023-09-20**, and the federal record still
holds **zero** assessments of it. **Roughly three years of warning, unused.**

## The premise being tested

**A compound's chemistry is hardest to see when its market is mature.** Nobody asks
how 7-OH is made because it is in every gas station. By the time a consumer can
evaluate a substance it is already distributed, and the preventive window is shut.

Adverse-event systems need casualties. Lobbying disclosures need a commercial
interest to already exist. Retail observation needs a product on a shelf. **All
three are downstream of the decision to manufacture. A patent filing is upstream of
it.**

## What would answer it

1. **Generalize the patent sweep beyond kratom.** SEVENFOLD searched compound names
   on one scaffold. The general form is: for each controlled substance class, which
   uncontrolled analogues have manufacturing claims filed against them.
2. **Watch scheduling actions as triggers.** Each new control action names the
   compounds it covers. The compounds structurally adjacent to those, and NOT named,
   are the forward-indicator set.
3. **NPS monitoring.** EU EMCDDA / EUDA early warning and UNODC early warning
   advisory publish new psychoactive substance notifications. Compare against US
   scheduling to measure the lag.
4. **Watchers.** SEVENFOLD's `tools/` pattern. A patent or docket watcher is cheap;
   the cost is choosing what to watch.

## Controls that must be run

- Any "no analogue found" result requires a known-present control on the same index,
  as in SEVENFOLD Finding 20 s3.
- Patent-office searches by **compound name only** will miss a process patent that
  does not name its product. SEVENFOLD's own 18-document corpus has this limit and
  states it. Search transformations as well as names.
