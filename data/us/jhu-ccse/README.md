
# Johns Hopkins CSSE Coronavirus COVID-19 Data 

This repository contains processing tools and data sourced from the [2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19) GitHub project. 

## csse_covid_19_daily_reports
This dataset, released daily as CSV file, provides various COVID-19 cases and death counts at the national and subnational levels. 
This dataset was first published on January 22nd 2020, with daily counts at the country and selected first administrative levels for confirmed/recovered cases and deaths. 
On March 1st 2020, the dataset added latitude and longitude variables.
On March 22nd 2020, the dataset added reporting US county level.

### Data Curation Notes
- The following columns are dropped from the dataset: longitude/latitude, geography names, count of active cases (added on 2020-03-22, this gets recomputed), time stamp (replaced by date)
- The following columns are added to the dataset: iso3166_1, cnt_active, date_stamp
- For the US, the number of recovered cases are not provided at the state or lower levels (only at the national level)

### Country level
- On 2020-02-28, data was reported for North Ireland. This record was aggregated under United Kingdom (GB).
- On 2020-03-08, data was reported under both Ireland and Republic of Ireland. The latter record was dropped.
- The following columns are added to the dataset: iso3166_1, cnt_active, date_stamp
- For the US, the number of recovered cases are not provided at the state or lower levels (only at the national level)
- On 2020-02-28, data was reported for North Ireland. This record was aggregated under United Kingdom (GB).
- On 2020-03-08, data was reported under both Ireland and Republic of Ireland. The latter record was dropped.
- From 2020-03-09 to 2020-03-10, data was reported for Hong Kong SAR and Macao SAR. These were aggregated under China.
- On 2020-03-10, data was reported for Taipei and environs. This was renamed to Taiwan.
- From 2020-03-11 to 2020-03-12, data was reported under both China and Mainland China. These were aggregated.
- On 2020-03-10, data was reported for Taipei and environs. This was renamed to Taiwan.
- From 2020-03-16 to 2020-03-18, data was reported under both Congo (Kinshasa) and Republic of the Congo. These records were aggregated.
- From 2020-03-18 to 2020-03-19, data was reported under "Gambia, The" and "The Gambia". These records were aggregated.
- From 2020-03-19 to 2020-03-19, data was reported under "Bahamas, The" and "The Bahamas". These records were aggregated.
- From 2020-03-21 to 2020-03-21, data was reported under "Cape Verde" and "Cabo Verde". These records were aggregated.
- In March 2020, data is being reported for both Congo (Kinsahsa) and Republic of the Congo. These are merged as this is the same country

Our derived country level dataset is organized as follows: 

|variable name  | description 									| coding/type|
|---------------|-------------									|------------|
|date_stamp     |The record date in ISO 8601 format (YYYY-MM-DD)|date| 
|iso3166_1		|A country ISO 3166-1 alpha-2 code				|text|
|cnt_confirmed	|Count of confirmed cases						|numeric|
|cnt_deaths		|Count of deaths								|numeric|
|cnt_recovered	|Count of recovered cases						|numeric|
|cnt_active		|Count of active cases							|numeric|

### U.S. State level

Our derived state level dataset is organized as follows:

|variable name  | description 									| coding/type|
|---------------|-------------									|------------|
|date_stamp     |The record date in ISO 8601 format (YYYY-MM-DD)|date| 
|iso3166_1		|A country ISO 3166-1 alpha-2 code				|text|
|subdivision_code|A standardized categorization of geographies and categories found in the original file. Includes U.S. states as well as categories like "Recovered", "Wuhan Evacuee", and cruise ships.|text|
|us_state_fips|U.S. FIPS 5-2 state code|text|
|us_state_postal|U.S. State Postal code	|text|
|cnt_confirmed	|Count of confirmed cases						|numeric|
|cnt_deaths		|Count of deaths								|numeric|
|cnt_recovered	|Count of recovered cases						|numeric|


### U.S. County level
- Some admin2 FIPS codes only have 4 digits (missing their leading 0). These were patched.
- 800nn codes: entries are found with an admin2 FIPS code 800+State FIPS code and a label of "Out of XX" where XX is the state 2-letter code (e.g. Out of CO). These are aggregated into a "Other" category.
- 900nn codes: entries are found with an admin2  code 900+State FIPS code and county name "Unassigned". These are aggregated into a "Other" category.
- Missing code: A few entries have no admin2 FIPS codes to capture count their regional or specific entities (e.g. West Utah, TriHealth, etc.). These are aggregated into a "Other" category.

Our derived U.S. County level data is organized as follows.

|variable name  | description 									| coding/type|
|---------------|-------------									|------------|
|date_stamp		|The record date in ISO 8601 format (YYYY-MM-DD)|date|
|iso3166_1		|A country ISO 3166-1 alpha-2 code				|text|
|subdivision_code|												|text|
|us_state_fips	|U.S. FIPS 5-2 state code						|text|
|us_state_postal|U.S. State 2-letter Postal code				|text|
|cnt_confirmed	|Count of confirmed cases						|numeric|	
|cnt_death		|Count of deaths								|numeric|
|cnt_recovered	|Count of recovered cases						|numeric|
|cnt_active		|Count of active cases							|numeric|
|iso3166_1_a3	|A country ISO 3166-1 alpha-3 code				|text|
|iso3166_1_nn	|A country ISO 3166-1 numeric code				|text|
|day_stamp		|The record date day (DD)						|text|
|month_stamp	|The month of the record stamp (ISO 8601 MM)	|text|
|year_stamp		|The year of the record stamp (ISO 8601 YYYY)	|text|
|yearmonth_stamp|The year+month of the record date stamp (ISO 8601 YYYY-MM)|text|
|yearweek_stamp |The week of the year (ISO 8601 YYYY-Www)		|text|
|dow_stamp		|The day of the week (ISO 8601 YYYY-Www-n)		|text|
|doy_stamp		|The day of the year (ISO 8601 YYYY-DDD)		|text|
|quarter_stampe	|The calendar quarter of the date stamp  (ISO 8601 YYYY-Qq)|text|


