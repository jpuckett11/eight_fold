# `exhibits/_blocked/` — what is in here and why

**Inherited from CASE SEVENFOLD 2026-08-31. The rules below carry over unchanged;
the file tables are SEVENFOLD's and are retained as worked examples until EIGHTFOLD
has its own.**

Written 2026-08-30. Until now the reason a file was quarantined lived **only in its
filename**, and one of them (`propublica_WRONG_ENTITY_...`) is documented in no
finding at all. That is fragile. Anyone picking this case up needs to know that
nothing in this directory may be cited, and why each item is here.

**Rule: nothing in `_blocked/` is evidence.** Not a single file here supports a
claim. They are kept because a failed capture and a rejected claim are both part of
the record, and because deleting them would make the corpus look cleaner than it is.

The directory holds **three different kinds of thing**, which have been conflated:

---

## A. Capture failures — the source was never retrieved

The file is a challenge page, denial page or rate-limit page. **The underlying
document has never been read.** Any claim that would rest on one of these is
unsourced.

| File | What happened |
|---|---|
| `dea_pr_20260701.blockpage.html` | HTTP 403, 514 bytes |
| `hhs_fda_commend_dea.blockpage.html` | Akamai "Access Denied", 450 bytes |
| `crs_lsb11457.blockpage.html` | congress.gov 403 |
| `publiccitizen_crackdown_that_wasnt.blockpage.html` | HTTP 403 |
| `publiccitizen_fake_crackdown.blockpage.html` | HTTP 403 |
| `missouri_ag_7oh_20260807.blockpage.html` | HTTP 403 |
| `fbi_quest_ceo_nine_years.blockpage.html` | archives.fbi.gov 403 |
| `basentinel_mullin_stake.blockpage.html` | HTTP 429 |
| `qz_mullin_hearing_20260615.blockpage.html` | Cloudflare "Just a moment...", 403. Added 2026-08-30 |
| `sec_complaint_21087_pdf.html` | SEC.gov **"Request Rate Threshold Exceeded"** |
| `sec_lr_21087_cash_grose.html` | SEC.gov **"Request Rate Threshold Exceeded"** |
| `sec_press_2009_139.html` | SEC.gov **"Request Rate Threshold Exceeded"** |

### Two of these are retryable, and nobody has retried them

- **The three SEC files are a RATE LIMIT, not a refusal.** SEC.gov serves these
  documents to a paced client. They relate to the J.W. Ross / Jerry D. Cash
  securities fraud record behind Finding 23. Re-run with a delay and a declared
  User-Agent and they will very likely come back.
- **`crs_lsb11457` may be reachable by another path.** On 2026-08-30 the
  congress.gov **HTML** page for H.R. 8000 returned 403 while
  `congress.gov/119/bills/hr8000/BILLS-119hr8000ih.pdf` returned **200**. The
  document-path pattern is not blocked even where the page path is. Worth trying for
  CRS products before treating them as unavailable. See `exhibits/federal/CAPTURED_AT.txt`.

---

## B. Retrieved successfully, but substantively WRONG — never cite

| File | Why it is rejected |
|---|---|
| `propublica_WRONG_ENTITY_kratos_not_kratom.html` | Retrieved fine. It is ProPublica FEC Itemizer data for **Kratos Defense & Security Solutions, Inc. PAC** — an aerospace and defense contractor. **"Kratos" is not "kratom."** Nothing in this file relates to this case. Kept as a record of the near-miss, because the two strings differ by one character and the mistake will be made again. |

---

## C. Quarantined claims — circulating assertions checked and refuted

| File | Claim |
|---|---|
| `CLAIM_60M_KRATOM_REFUTED.md` | "Mullin has north of $60 million in kratom." **False.** The OGE 278 shows one line at $500,001-$1,000,000; ~$60M is his total net worth. Overstates the position by 60x to 120x. Full working, including the limits of the refutation, is in that file. |

**Why claims get a file rather than a shrug.** Finding 01 is strong because it is
small, exact, and reproducible from a public PDF. An inflated version of it is worse
than useless: refuting the exaggeration in public discredits the accurate finding
sitting beside it. Recording the refutation *before* the claim circulates is cheaper
than correcting it after.

---

## Maintaining this directory

- A capture failure goes in as `<name>.blockpage.html` and gets a row in section A.
- Content that is retrievable but wrong gets `<source>_WHY_<detail>.<ext>` and a row
  in section B, with the reason spelled out — not left to the filename.
- A refuted claim gets `CLAIM_<short>_REFUTED.md` and a row in section C.
- Everything here is still hashed into `exhibits/SHA256SUMS.txt`. Quarantined is not
  untracked.
