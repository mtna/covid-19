# Tennessee Department of Health COVID-19 Data

## NOTE: This data is no longer being updated in our GitHub or RDS system. As of early May 2021, the TN Department of Health updated their reporting format which you can read about [here](https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/Covid-19-Data-Update.pdf), and the current datasets can be found [here](https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html).  

These datasets are pulled nightly from the Tennesee Department of Health (TDH) website at https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html. They are then converted them from xlsx format to csv using the python xlsx2csv utility (full script [here](https://bitbucket.org/mtnaus/covid-19/src/master/tools/covid19-scraper/scripts/xlsxDownload.sh)), and the resulting csv files are added to this directory.
The metadata for each of these datasets is taken from the provided data dictionary file, which is also pulled nightly from the TN DOH website. 

## Original TDH datasets are structured as follows:  
### Age:
|Variable | Description | Type/Coding |
|---|----|--|
| DATE            | Date of report                              |Date|
| AGE_RANGE       | Patient age at date of laboratory testing (or the date the patient was reported to public health if the laboratory testing date is not yet known). Categorized based on patient age at the date of laboratory testing or the date of report to public health if date of onset is not yet known| 0-10 years, 11-20 years, 21-30 years, 31-40 years, 41-50 years, 51-60 years, 61-70 years, 71-80 years, 81 + years, Pending |
| AR_CASECOUNT    | Number of cases by age range category.      |Numeric|
| AR_TOTALPERCENT | Percent of cases by age range category.     |Numeric|
| NEW_ARCASES     | Difference in number since previous day for the age range category. This is calculated as (AR_CASECOUNT (within age category today) - AR_CASECOUNT (within age category yesterday)). |Numeric|
| AR_NEWPERCENT   | Percent of new cases by age range category. |Numeric|
| AR_TOTALDEATHS  | Number of deaths by age range category.     |Numeric|
| AR_NEWDEATHS    | Difference in number of new deaths by age range since previous day. This is calculated as (AR_TOTALDEATHS (within age category today) - AR_TOTALDEATHS (within age category yesterday))|Numeric|

### County New
|Variable | Description | Type/Coding |
|---|----|--|
|DATE| Date of report |Date|
|COUNTY|County of residence of the patient|Categorical|
|TOTAL_CASES|Number of confirmed and probable cases of COVID reported to TDH, per the TDH case definition (TOTAL_CONFIRMED + TOTAL_PROBABLE)|Numeric|
|NEW_CASES|Difference in number of cases since previous day (TOTAL_Cases  (today) - TOTAL_Cases (yesterday))|Numeric|
|TOTAL_CONFIRMED|Total number of positive tests reported to TDH|Numeric|
|NEW_CONFIRMED|Difference in number of positive tests reported to TDH since previous day (TOTAL_Cases  (today) - TOTAL_Cases (yesterday))|Numeric|
|~~TOTAL_PROBABLE~~ - REMOVED 2020-05-08|TDH definition for a probable case can be found here: https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/COVID-Case-Definition.pdf|Numeric|
|~~NEW_PROBABLE~~ - REMOVED 2020-05-08|Difference in number of probable cases since previous day (TOTAL_PROBABLE (today) - TOTAL_PROBABLE (yesterday))|Numeric|
|POS_TESTS|Total number of positive tests reported to TDH (TOTAL_PROBABLE (today) - TOTAL_PROBABLE (yesterday))|Numeric|
|NEG_TESTS|Total number of negative tests reported to TDH|Numeric|
|TOTAL_TESTS|Total number of tests reported to TDH (POS_TESTS + NEW_TESTS)|Numeric|
|NEW_TESTS|Difference in number of tests reported to TDH since previous day (TOTAL_TESTS (today) - TOTAL_TESTS (yesterday))|Numeric|
|NEW_DEATHS|Difference in the number of deaths since previous day (TOTAL_Deaths (today) - TOTAL_Deaths (yesterday))|Numeric|
|TOTAL_DEATHS|Total number of COVID-related deaths reported to TDH. Some deaths may be reported by healthcare providers, hospitals, medical examiners, local health departments or others before they are included in the statewide count.|Numeric|
|NEW_RECOVERED|Difference in number of recovered patients since previous day (TOTAL_Recovered (today) - TOTAL_Recovered (yesterday))|Numeric|
|TOTAL_RECOVERED|TDH defines recovered as people included in total cases who (1) have been confirmed to be asymptomatic by their local or regional health department and have completed their required isolation period or (2) are at least 21 days beyond the first test confirming their illness.|Numeric|
|NEW_ACTIVE|Difference in number of active cases since previous day (TOTAL_Active (today) - TOTAL_Active (yesterday))|Numeric|
|TOTAL_ACTIVE|Active cases are COVID-19 confirmed or probable cases who are not classified as recovered and are not deceased. (TOTAL_CASES - TOTAL_RECOVERED - TOTAL_DEATHS)|Numeric|
|NEW_HOSPITALIZED|Difference in number of hospitalized patients among total cases since previous day (TOTAL_Hosp (today) - TOTAL_Host (yesterday))|Numeric|
|TOTAL_HOSPITALIZED|Total number of COVID patients who report ever being hospitalized for their illness. Hospitalization status is gathered at the time of diagnosis, therefore this information may be incomplete. This number indicates the number of patients that were ever hospitalized during their illness, it does not indicate the number of patients currently hospitalized. |Numeric|


### Daily Case Information
|Variable | Description | Type/Coding |
|---|----|--|
|DATE|Date of Report|Date|
|TOTAL_CASES|Number of confirmed and probable cases of COVID reported to TDH, per the TDH case definition (TOTAL_CONFIRMED + TOTAL_PROBABLE)|Numeric|
|NEW_CASES|Difference in number of cases since previous day (TOTAL_Cases  (today) - TOTAL_Cases (yesterday))|Numeric|
|TOTAL_CONFIRMED|Total number of positive tests reported to TDH|Numeric|
|NEW_CONFIRMED|Difference in number of positive tests reported to TDH since previous day (TOTAL_Cases  (today) - TOTAL_Cases (yesterday))|Numeric|
|~~TOTAL_PROBABLE~~ - REMOVED 2020-05-08|TDH definition for a probable case can be found here: https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/COVID-Case-Definition.pdf|Numeric|
|~~NEW_PROBABLE~~ - REMOVED 2020-05-08|Difference in number of probable cases since previous day (TOTAL_PROBABLE (today) - TOTAL_PROBABLE (yesterday))|Numeric|
|POS_TESTS|Total number of positive tests reported to TDH (TOTAL_PROBABLE (today) - TOTAL_PROBABLE (yesterday))|Numeric|
|NEG_TESTS|Total number of negative tests reported to TDH|Numeric|
|TOTAL_TESTS|Total number of tests reported to TDH (POS_TESTS + NEW_TESTS)|Numeric|
|NEW_TESTS|Difference in number of tests reported to TDH since previous day (TOTAL_TESTS (today) - TOTAL_TESTS (yesterday))|Numeric|
|NEW_DEATHS|Difference in the number of deaths since previous day (TOTAL_Deaths (today) - TOTAL_Deaths (yesterday))|Numeric|
|TOTAL_DEATHS|Total number of COVID-related deaths reported to TDH. Some deaths may be reported by healthcare providers, hospitals, medical examiners, local health departments or others before they are included in the statewide count.|Numeric|
|NEW_RECOVERED|Difference in number of recovered patients since previous day (TOTAL_Recovered (today) - TOTAL_Recovered (yesterday))|Numeric|
|TOTAL_RECOVERED|TDH defines recovered as people included in total cases who (1) have been confirmed to be asymptomatic by their local or regional health department and have completed their required isolation period or (2) are at least 21 days beyond the first test confirming their illness.|Numeric|
|NEW_ACTIVE|Difference in number of active cases since previous day (TOTAL_Active (today) - TOTAL_Active (yesterday))|Numeric|
|TOTAL_ACTIVE|Active cases are COVID-19 confirmed or probable cases who are not classified as recovered and are not deceased. (TOTAL_CASES - TOTAL_RECOVERED - TOTAL_DEATHS)|Numeric|
|NEW_HOSP|Difference in number of hospitalized patients among total cases since previous day (TOTAL_Hosp (today) - TOTAL_Host (yesterday))|Numeric|
|TOTAL_HOSP|Total number of COVID patients who report ever being hospitalized for their illness. Hospitalization status is gathered at the time of diagnosis, therefore this information may be incomplete. This number indicates the number of patients that were ever hospitalized during their illness, it does not indicate the number of patients currently hospitalized. |Numeric|


### Race, Ethnicity, & Sex
|Variable | Description | Type/Coding |
|---|----|--|
|Date|Date of report| Date|
|Category|Demographic category |One of: Race, Ethnicity, Sex |
|Cat_Detail| Detail about the demographic category (see below)|Categorical|
|Cat_CaseCount|Number of cases for the specific category|Numeric|
|Cat_Percent|Percent of cases for the specific category|Numeric
|CAT_DEATHCOUNT|Number of deaths for the specific category|Numeric
|CAT_DEATHPERCENT|Percent of deaths for the specific category|

### Cat_Detail information
*More information regarding the Category and Cat_Detail variables above. "Category" will be one of "Ethinicity", "Race", or "Sex", and "Cat_Detail" will be one of the corresponding categories listed in the table below.*

|"Category" value | Notes| Possible "Cat_Detail" values|
|---|---|---|
|Ethnicity| Patient Ethnicity   |Hispanic, Not Hispanic or Latino, Pending|
|Race|Patient Race Among Total Cases. Note: Those who select multiple race categories are grouped into the "Other/Multiracial" category. "Pending" category includes the following respnse options: refused to answer, unknwon, not asked, and null/blank. |Asian, Black or African American, Other/Multiracial, White|
|Sex|Patient Sex| Female, Male, Pending|

## Data Curation & Transformation

### Age

The following cleansing operations have been performed on the source age file:

- The variables have been renamed to align with the standard variable names we are using across the data sets:
	- `DATE` -> `date_stamp` 
	- `AGE_RANGE` -> `age_group` 
	- `AR_CASECOUNT` -> `cnt_confirmed` 
	- `AR_TOTALPERCENT` -> `pct_confirmed` 
	- `NEW_ARCASES` -> `cnt_confirmed_new` 
	- `AR_NEWPERCENT` -> `pct_confirmed_new` 
	- `AR_TOTALDEATHS`  -> `cnt_death` 
	- `AR_NEWDEATHS` -> `cnt_death_new`
- The date variable has been reformatted to be an ISO 8601 date. 
- The age goup has been coded.
- The percentage of cases and percentage of new cases were multiplied by 100 in order that the values add up to 100 rather than decimals that add up to 1.0.

### County

The following cleansing operations have been performed on the source county file:

- The variables have been renamed to align with the standard variable names we are using across the data sets:
	- `DATE` -> `date_stamp`
	- `COUNTY` -> `us_county_fips`
	- `TOTAL_CASES` -> `cnt_total`
	- `NEW_CASES` -> `cnt_total_new`
	- `TOTAL_CONFIRMED` -> `cnt_confirmed`
	- `NEW_CONFIRMED` -> `cnt_confirmed_new`
	- `POS_TESTS` -> `cnt_tested_pos`
	- `NEG_TESTS` -> `cnt_tested_neg`
	- `TOTAL_TESTS` -> `cnt_tested`
	- `NEW_TESTS` -> `cnt_tested_new`
	- `NEW_DEATHS` -> `cnt_death_new`
	- `TOTAL_DEATHS` -> `cnt_death`
	- `NEW_RECOVERED` -> `cnt_recovered_new`
	- `TOTAL_RECOVERED` -> `cnt_recovered`
	- `NEW_ACTIVE` -> `cnt_active_new`
	- `TOTAL_ACTIVE` -> `cnt_active`
	- `NEW_HOSPITALIZED` -> `cnt_hospitalized_new`
	- `TOTAL_HOSPITALIZED` -> `cnt_hospitalized`
	
- The date variable has been reformatted to be an ISO 8601 date. 
- The county name has been replaced with the 5 digit FIPS county code. The 'Pending' and 'Out of State' values have been removed from this variable. 
- A new variable `tn_covid_geo` has been added. This will be the 5 digit county FIPS code and will include codes for 'Pending' and 'Out of State'.
- The total and new variables have been placed side by side in the same order. 

### Daily Case

The following cleansing operations have been performed on the source daily case file:

- The variables have been renamed to align with the standard variable names we are using across the data sets:
	- `DATE` -> `date_stamp`
	- `TOTAL_CASES` -> `cnt_total`
	- `NEW_CASES` -> `cnt_total_new`
	- `TOTAL_CONFIRMED` -> `cnt_confirmed`
	- `NEW_CONFIRMED` -> `cnt_confirmed_new`
	- `POS_TESTS` -> `cnt_tested_pos`
	- `NEG_TESTS` -> `cnt_tested_neg`
	- `TOTAL_TESTS` -> `cnt_tested`
	- `NEW_TESTS` -> `cnt_tested_new`
	- `NEW_DEATHS` -> `cnt_death_new`
	- `TOTAL_DEATHS` -> `cnt_death`
	- `NEW_RECOVERED` -> `cnt_recovered_new`
	- `TOTAL_RECOVERED` -> `cnt_recovered`
	- `NEW_ACTIVE` -> `cnt_active_new`
	- `TOTAL_ACTIVE` -> `cnt_active`
	- `NEW_HOSP` -> `cnt_hospitalized_new`
	- `TOTAL_HOSP` -> `cnt_hospitalized`
- The date variable has been reformatted to be an ISO 8601 date. 
- The total and new variables have been placed side by side in the same order. 

### Race / Ethnicity / Sex

The following cleansing operations have been performed on the source daily case file:

- The variables have been renamed to align with the standard variable names we are using across the data sets:
	- `Date` -> `date_stamp` 
	- `Category` -> `category_type` 
	- `Cat_Detail` -> `category_name` 
	- `Cat_CaseCount` -> `cnt_confirmed` 
	- `Cat_Percent` -> `pct_confirmed` 
	- `CAT_DEATHCOUNT`  -> `cnt_death` 
	- `CAT_DEATHPERCENT` -> `pct_death`
- The date variable has been reformatted to be an ISO 8601 date. 
- Coded the category detail values
- The original file has been split into three separate files. We use the Category to split these out into dedicated Race, Ethnicity, and Sex files. 
