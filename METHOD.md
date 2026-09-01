# EIGHTFOLD method

Carried from SEVENFOLD. Each rule below was written after the failure it prevents.

## 1. Tag as you write

**[P]** primary · **[S]** secondary · **[I]** inference · **[U]** unverified.

Retro-tagging does not work. By the time you go back you no longer remember which
sentence came from the document and which came from your reading of it.

## 2. Never report a negative without a control

Run a known-present term against the same corpus and record the result next to the
negative.

> FDA CAERS, "9-hydroxycorynantheidine": **0 reports**. Control: "kratom" returns
> **879**. The search works, the zero is real.

Without the right-hand column that is not a finding, it is a broken query.

## 3. Verify the instrument before believing the output

Ask whether the command could have produced a complete answer at all. SEVENFOLD's
actual failures, all caught by this rule and all of which had produced confident
wrong output first:

- A manifest checker reported **273 corrupted exhibits**. The manifest was a
  three-column format and `sha256sum -c` was parsing the byte count as part of the
  filename. Nothing was corrupted.
- An FEC employer search returned 63 rows for a kratom company. **29 of them were
  "Johnsonville Foods"**, a Wisconsin sausage maker, with contributions back to 1988.
- A candidate lookup for "LEE, MIKE" resolved to **J Lee Castillo for Congress** and
  returned a tidy set of zeros that would have read as "Senator Mike Lee takes no
  industry money."
- A bill sweep across 18,317 files returned **zero kratom bills**. The one that
  exists is titled "END 7-OH Act" and its status record contains the word kratom
  zero times.
- A patent's claims were reported as coming from the description. They were in the
  claims; only part of the document had been extracted.

**Pattern: every one produced a plausible answer.** None of them errored.

## 4. Retain failures

Capture failures go to `exhibits/_blocked/` with the reason recorded in a file, not
only in a filename. They are never counted as evidence of absence and never cited.

## 5. Refuted claims get written down

When something circulating is wrong, record the refutation before it propagates.
See SEVENFOLD's `_blocked/CLAIM_60M_KRATOM_REFUTED.md` — a claim that a cabinet
secretary held "north of $60 million in kratom" when the filing shows one line at
$500,001-$1,000,000, the $60M being his total net worth.

**Note what that file also does: it records that the explanatory source could not
be captured**, and marks the explanation `[U]` rather than quoting a search-engine
rendering as though it were the article.

## 6. Correct in place, preserve the original

Copy to `<file>.bak-<timestamp>` before editing. Write the correction as a marked
block inside the finding. Never silently overwrite.

**And correct your own corrections.** Three "errors" flagged in SEVENFOLD's Finding
25 on 2026-08-31 turned out to be two false alarms and one internal inconsistency.
All three outcomes are recorded.

## 7. Chain of custody is not optional

Everything cited is hashed in `exhibits/SHA256SUMS.txt`. Regeneration **aborts** if
a previously-hashed file changed without a named exception. A manifest that quietly
re-hashes an altered exhibit destroys the only record that it was altered.

## 8. Write for a hostile reader

State the weakness before they find it. SEVENFOLD does this throughout: the Utah
budget comparison names its own funding-stream caveat, the rat study is labeled a
rat study, and the one non-trivial step in a chemistry argument is stated out loud
rather than omitted.

## 9. Do not become the story

The investigator's credibility is the asset. Nothing is worth more than it and
nothing else is irreplaceable.

## Cross-sections describe populations. They never describe people.
**Added 2026-08-31 at Jay Puckett's objection, and it corrected live work.**

> *"a mortgage borrower at 18-29 has a bad divorce at 30 and spirals. Breaking this
> into an age range does and proves nothing, because addiction can start at any
> point."*

**The rule.** An age band in year X and the same age band in year Y hold different
people. A person who crosses a band boundary between the cause and the effect is
invisible to the design: the event, the sequence and the individual are all lost, and
what remains is one box getting worse while another gets better with no way to know
whether anyone moved.

**Therefore:** no EIGHTFOLD claim about what happens to a person over time may rest
on age-banded cross-sectional data. Such a claim needs panel data following the same
individuals — NESARC, Add Health, NLSY97, PSID — or it must be stated as a
population description and nothing more.

**This rule was written because it had already been broken**, in FINDING_04 section
9d, which is marked withdrawn rather than edited away. See also FINDING_05.
