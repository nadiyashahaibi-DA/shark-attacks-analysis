## Business Case Proposal: Water‑Sport Risk Insurance for Hotels & Resorts


## Dataset

Global Shark Attack File (GSAF) — https://www.sharkattackfile.net/spreadsheets/GSAF5.xls

## Business Case
We are part of the research team at an insurance company 'Okinsurance'. Our goal is to propose the launching of a new water-sport risk insurance product targeting hotels, resorts, surf schools, and water-excursion organisers.

These businesses are increasingly offering activities such swimming, surfing and shark-intraction experiences. While these activities are attracting more guest this can expose hotels to liability and operational risk.


## Our goal is to use shark attack incident data to identify: 

- High-risk months
- High-risk activities
- Environmental vs behavioral risk (unprovoked vs provoked)

## As a result, we can design the offer as a new revenue stream for insurance company to hotels:  

- Seasonal premium
- Travel / Geographic risk tiers
- Activity specifi pricing
- "Adrenaline Thrill Seeker" for shark interaction excursions


## Hypotheses

- H1 - Shark‑incident risk is concentrated in a small number of countries
- H2 - Shark‑incident risk varies significantly by month/season
- H3 - Unprovoked attacks dominate and represent environmental risk


## MVP (Minimum Viable Product)

- Cleaning of essential fields:
- Country, Date/Month, Activity, Type
- Testing H1 (regional hotspots)
- Testing H2 (seasonality)
- Testing H3 (activity risk)
- Testing H4 (attack type relevance)


## out of scope

- Fatality/injury severity analysis
- Time‑window filtering (e.g., last 10–15 years)
- Dashboard or advanced visualization
- Predictive modeling


## Roadmap

| Phase | Description | Owner | Status |
|---|---|---|---|
| 1 | Initial dataset exploration and hypothesis formulation | Group | ✅ Done |
| 2 | Cleaning — Dates (Month, NaT, regex) | — | ✅ Done |
| 3 | Cleaning — Country / Activity / Type | — | 🔲 In progress |
| 4 | EDA — Hypothesis testing (counts by month/region/activity) | Group | 🔲 Pending |
| 5 | Conclusions and final recommendation | Group | 🔲 Pending |
| 6 | Presentation | Group | 🔲 Pending |


## Data Cleaning — Progress (Dates / Seasonality)


### Problem identified

The `Date` column in the original file was partially auto-converted to `datetime` by pandas when reading the Excel file — around 86% of rows were converted correctly, but ~13.5% remained as `NaT` (free-text, non-standard format, e.g. "23rd June", with no year in the same cell).


###############

## Country 

- Many entries contained:
	- Regions instead of countries
	- Question marks
	- Ocean/sea names
	- Mixed casing
- Required harmonization and removal of invalid entries


## Activity 

- Free‑text descriptions
- Typos (e.g., “swmming”, “surf sking”)
- Mixed formats (“Swimming, towing kayak”)
- Needed mapping to core categories (Surfing, Swimming, Fishing, Diving, etc.)

## Type 

- Mixed casing
- Punctuation
- Variants of “Unprovoked”, “Provoked”, “Invalid”
- Needed standardization


######################

### Cleaning techniques applied

1. **Extraction of the `Month` column** from the already-converted `Date` column (`.dt.month`)
2. **Regex** to recover the month on rows where the original date was free text (e.g. `"23rd June"` → captures the last word of the string as the month name)
3. **Conversion of month names to numbers** (`pd.to_datetime(..., format='%B')`)
4. **Null value handling**: `dropna(subset=['Month'])` applied only for the seasonality analysis, without altering the original dataset
5. **Detection and removal of a structural outlier**: an artificial spike in January was identified, caused by incomplete dates (year only) that pandas/Excel defaulted to `January 1st`. Confirmed by comparing the proportion of "day 1" entries in January (41%) vs. other months, and these rows were excluded from the seasonality analysis specifically


$$$$$$$$$$$$$$$$$$$$$$$$$

## Country
- Lowercasing → title case
- Removing punctuation
- Replacing invalid entries (oceans, seas, question marks)
- Grouping rare or unclear entries into “Unknown” or “Other”

## Activity
- Lowercasing
- Removing punctuation
- Stripping whitespace
- Fixing typos
- Mapping free‑text descriptions to core categories
- Grouping rare activities into “Other”

## Type
- Lowercasing
- Removing punctuation
- Standardizing categories
- Mapping variants to canonical labels


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

### Documented limitations

- ~12.4% of rows don't have a clear enough date to determine the month, and are excluded only from the seasonality analysis (not from the overall dataset)
- The incident count by month is currently **global** (not filtered by `Swimming` activity or by region) — this depends on the `Activity` column cleanup
- A time-window filter (e.g. last 10-15 years) has not yet been applied — decision pending, to be justified based on data volume per year


### Current result (incident count by month, global, before activity filter)


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


## Next Steps
- Repeat the monthly count filtering for `Activity == 'Swimming'` only (once the column is cleaned)
- Cross seasonality with `Country`/`Location` to identify safer region+month combinations
- Decide on and apply a time window for the final analysis
- Translate numerical results into a final recommendation for the presentation


## If only we could in future: 

- Analyze fatality and injury severity
→ supports premium pricing
- Apply a time‑window filter (last 10–15 years)
→ improves modern relevance
- Cross‑reference swimming‑only seasonality
→ supports hotel partnerships
- Build a risk scoring model combining:
	- Country
	- Month
	- Activity
	- Type
	- Severity
