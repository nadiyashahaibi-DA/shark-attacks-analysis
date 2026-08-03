# Shark Attack Risk Analysis — Mini Project

## Dataset

Global Shark Attack File (GSAF) — https://www.sharkattackfile.net/spreadsheets/GSAF5.xls

## Business Case

Research team at OKinsurance proposing a water-sport risk insurance product for US hotels & Resorts.


## Hypotheses

| ## | Hypothesis | Status | ✅ Done

The analysis was guided by three core hypotheses:

- H1: Risk is concentrated in a small number of countries.
- H2: Risk varies significantly by month/season.
- H3: Unprovoked attacks dominate — risk is environmental, not behavioral.

All three hypotheses were supported by the data.


## MVP (Minimum Viable Product)

**In scope for MVP (minimum deliverable):**
- Cleaning of the essential fields: `Location`, `Date`/`Month`, `Activity`
- Answering H1 (country hotspots) and H2 (seasonality)
- A direct recommendation: months/country with historically higher swimming-related incidents

**Out of MVP (only if time allows):**
- H3 (swimming vs. surfing vs. diving comparison)
- Refined time-window filter (e.g. last 10-15 years)
- Data visualizations / dashboard

## Scope

**In scope:** ✅
- Cleaning of `Date`/`Month`, `Country`, `Activity`, `Type`
- Testing H1, H2, H3 using GSAF data only

**Out of scope (explicitly documented):**❌
- External data (tourism, climate, population density)
- Predictive models / machine learning (this project is EDA, not modeling)
- Shark species, injury severity — not part of the defined hypotheses

## Roadmap

| Phase | Description | Owner | Status |
|---|---|---|---|
| 1 | Initial dataset exploration and hypothesis formulation | Group | ✅ Done |
| 2 | Cleaning — Dates (Month, NaT, regex) | — | ✅ Done |
| 3 | Cleaning — Country / Activity / Type | — | ✅ Done |
| 4 | EDA — Hypothesis testing (counts by month/region/activity) | Group | ✅ Done |
| 5 | Conclusions and final recommendation | Group | ✅ Done |
| 6 | Presentation | Group | ✅ Done |

## Data Cleaning

### Problem identified (Dates / Seasonality) 

The `Date` column in the original file was partially auto-converted to `datetime` by pandas when reading the Excel file — around 86% of rows were converted correctly, but ~13.5% remained as `NaT` (free-text, non-standard format, e.g. "23rd June", with no year in the same cell).

### Cleaning techniques applied
1. **Extraction of the `Month` column** from the already-converted `Date` column (`.dt.month`)
2. **Regex** to recover the month on rows where the original date was free text (e.g. `"23rd June"` → captures the last word of the string as the month name)
3. **Conversion of month names to numbers** (`pd.to_datetime(..., format='%B')`)
4. **Null value handling**: `dropna(subset=['Month'])` applied only for the seasonality analysis, without altering the original dataset
5. **Detection and removal of a structural outlier**: an artificial spike in January was identified, caused by incomplete dates (year only) that pandas/Excel defaulted to `January 1st`. Confirmed by comparing the proportion of "day 1" entries in January (41%) vs. other months, and these rows were excluded from the seasonality analysis specifically

## Data Cleaning — (Country/Activity/Type)

### Problem identified Country: 

The original Country field was badly populated and had several data‑quality problems that made geographic analysis unreliable:
Inconsistent formatting: entries appeared in mixed casing (e.g., Australia, AUSTRALIA, AUstralia), requiring normalization.
Non‑country values: many rows contained oceans (“Pacific Ocean”), regions (“Asia”), or vague descriptors (“Between Portugal and India”).
Missing or corrupted entries: some rows contained question marks or partial text.

### Cleaning techniques applied:

Standardized all valid country names to title case for consistency.
Implemented a validation step to detect non‑country entities and grouped them under a unified label: “Unknown”.
Removed stray symbols and replaced ambiguous entries with a controlled vocabulary.


## Problem identified Activity: 

The Activity column was one of the messiest fields in the dataset:
Over 1,613 unique free‑text descriptions, including typos, multi‑activity combinations, and overly specific phrases.
Examples ranged from simple terms (“Swimming”) to highly detailed descriptions (“Standing on a boat while holding a fishing net”).
Many entries described the same activity but used different wording (free diving, scuba diving, pearl diving).


### Cleaning techniques applied

Designed a mapping dictionary to consolidate all variants into 20 standardized activity categories.
Applied regex and keyword extraction to identify core activity types (e.g., swimming, surfing, diving, fishing).
Grouped ambiguous or multi‑activity entries into the closest matching category.


## Problem identified Type: 

The Type field contained multiple issues that prevented reliable classification:
Numerous spelling and casing variants of the main categories (“Unprovoked”, “Provoked”, “invalid”, “UNPROVOKED”).
Some entries were partially missing or mislabeled.


### Cleaning techniques applied

Standardized all known variants into a controlled set of labels:
Unprovoked, Provoked, Invalid, Sea Disaster, Watercraft, Other.
Consolidated rare or ambiguous types into a single “Other” category to avoid noise.
Ensured consistent casing and removed trailing symbols or formatting artifacts.


### Documented limitations

- ~12.4% of rows don't have a clear enough date to determine the month, and are excluded only from the seasonality analysis (not from the overall dataset)
- The incident count by month is currently **global** (not filtered by `Swimming` activity or by region) — this depends on the `Activity` column cleanup
- A time-window filter (e.g. last 10-15 years) has not yet been applied — decision pending, to be justified based on data volume per year

### Result (incident count by month, global, before activity filter)

| Month | Incidents |
|---|---|
| January* | 812 (includes outlier to be corrected) |
| February | 391 |
| March | 430 |
| April | 454 |
| May | 426 |
| June | 507 |
| July | 706 |
| August | 608 |
| September | 547 |
| October | 462 |
| November | 423 |
| December | 453 |

*January corrected after removing the structural outlier (see limitations section).


### Result (incident count by month, global, after activity filter)

| Month | Incidents |
|---|---|
| January* | 53 |
| February | 65 |
| March | 113 |
| April | 173 |
| May | 181 |
| June | 273 |
| July | 409 |
| August | 345 |
| September | 313 |
| October | 227 |
| November | 125 |
| December | 79|


* 41 % of January rows had the exact date "Jan 1st" — a signature of incomplete original dates (year only), defaulted by Excel/pandas.

* 812 → 478 Corrected January incident count


## Next Steps
- Repeat the monthly count filtering for `Activity == 'Swimming'` only (once the column is cleaned)
- Cross seasonality with `Country`/`Location` to identify safer region+month combinations
- Decide on and apply a time window for the final analysis
- Translate numerical results into a final recommendation for the presentation
