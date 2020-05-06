# Standardization / Harmonization

One of our primary objectives is to provide access to data that facilitates analysis within and across multiple data sources. 

## Standardized Variables
Whenever possible, we use harmonized name for the dataset variables/fields/common. Note that this does not implies that they are directly comparable, as meaning will vary across sources due to differences in definitions, data collection methods, and other factors.

### COVID-19 Counts
| name            | generic meaning | type/coding |
|-----------------|---|---|
| cnt_active      | Number of active cases (expected to be total-recovered)
| cnt_confirmed   | Number of confirmed cases
| cnt_death       | Number of deaths
| cnt_recovered   | Number of recovered cases
| cnt_tested      | Number of tests conducted
| cnt_tested_pos  | Number of tests conducted that were positive
| cnt_tested_neg  | Number of tests conducted that were negative
| cnt_total       | Total number of cases

### Demographics
| name            | generic meaning | type/coding |
|-----------------|---|---|
| age             | Age 
| age_from        | Age from
| age_to          | Age to
| sex             | Sex | 1=Male, 2=Female

### Geospatial
| name            | generic meaning | type/coding |
|-----------------|---|---|
| geocode         | Local geography that varies depending on the dataset
| iso3166_1       | Country ISO 3166-1 alpha-2 code
| iso3166_1_a3    | Country ISO 3166-1 alpha-3 code 
| iso3166_1_nn    | Country ISO 3166-1 numeric code 
| iso3166_2       | Country subdivision ISO 3166-2 code
| iso3166_3       | Country subdivision ISO 3166-3 code
| ca_provterr     | Canada province/territory code
| ca_region       | Canada region code
| us_county_fips  | U.S. FIPS 6-4 County code (5-digit)
| us_division     | U.S. Census Bureau division code
| us_state_fips   | U.S. FIPS 5-2 state code
| us_state_postal | U.S. State Postal code
| us_state_ssa    | U.S. Social Security Administration state code
| us_region       | U.S. Census Bureau region code


### Time
| name            | generic meaning | type/coding |
|-----------------|---|---|
| date_stamp      | The record date (ISO 8601 YYYY-MM-DD) ||
| datetime_stamp  | The record date/time (ISO 8601) ||
| day_stamp       | The day of the record stamp (ISO-8601 DD) ||
| dow_stamp       | The day of the week (ISO 8601 YYYY-Www-n) ||
| doy_stamp       | The day of the year (ISO 8601 YYYY-DDD) ||
| month_stamp     | The month of the record stamp (ISO 8601 MM)||
| quarter_stamp   | The calendar quarter of the date stamp  (ISO 8601 YYYY-Qq)||
| week_stamp      | The week of the year (ISO 8601 YYYY-Www)||
| year_stamp      | The year of the record stamp (ISO 8601 YYYY)||
| yearmonth_stamp | The year+month of the record date stamp (ISO 8601 YYYY-MM) ||

References:
- https://en.wikipedia.org/wiki/ISO_week_date

## Standard Classifications

Whenever possible, categorical variables use coding schemes from the international and national classifications listed below.
- [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166)
- [FIPS 5-2](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code)
- [FIPS 6-4](https://en.wikipedia.org/wiki/FIPS_county_code)
- [U.S. Census regions/divisions](https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf)
