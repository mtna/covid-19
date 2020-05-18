## State of Ohio Coronavirus Summary Data

Data pulled daily from the Ohio Department of Health's Coronavirus overview page at https://coronavirus.ohio.gov/wps/portal/gov/covid-19/dashboards . The website is updated daily at 2pm. 

## Description

The State of Ohio COVID-19 Dashboard displays the most recent preliminary data reported to the Ohio Department of Health (ODH) about cases, hospitalizations and deaths in Ohio by selected demographics and county of residence

## Limitations of Use

All data displayed is preliminary and subject to change as more information is reported to ODH. Trends are based on the date of illness onset. If onset date is unknown, the earliest known date associated with the case is used as a substitute for the date of illnes onset.
A note on total deaths: Definitive cause of death can take weeks to determine. Data displayed illustrates current status. 

## Source Data

The source data includes aggregate counts of confirmed cases, deaths, and hospitalizations grouped by some demographic information (county, sex, age range). The data is aggregated by demographics, onset date, and date of death. The source file is structured as follows:

| name               | generic meaning | type/coding |
|--------------------|---|---|
| County             | County name               | Text
| Sex                | Sex of individual         | Male / Female / Unknown
| Age Range          | Age range of individual   | Text
| Onset Date         | Onset date                | Date
| Date of Death      | Date of death             | Date
| Case Count         | Count of confirmed cases  | Numeric
| Death Count        | Count of deaths           | Numeric
| Hospitalized Count | Count of hospitalizations | Numeric

## Data Curation & Transformation

We transform the incoming file into two files. A clean version of the original file and an aggregate file with counts by county. 

## Clean Data

The first is a clean version of the source data. This differs from the source in the following ways:
- The county names are dropped and recoded as their 5 digit FIPS code and their code labels will be a part of the metadata.
- The sex column has been coded. 
- The date variables have been converted to ISO 8601 format (YYYY-MM-DD)
- The variables have been renamed and reordered.
- The age range in has been coded with Unknown being coded as 99. 
- The records are ordered by date_stamp. 

The clean file is structured as follows:

| name             | generic meaning | type/coding |
|------------------|---|---|
| date_stamp       | Date of the report (Onset date)                     | Date
| us_county_fips   | 5-digit county FIPS code                            | Text
| sex              | Sex of individual                                   | 1 (Male) / 2 (Female) / 9 (Unknown)
| age_group        | Age group of the individual                         | 00 (0-19), 20 (20-29), 30 (30-39), 40 (40-49), 50 (50-59), 60 (60-69), 70 (70-79), 80 (80+), 99 (Unknown),
| cnt_confirmed    | The total number of confirmed cases for the record  | Numeric
| cnt_hospitalized | The total number of hospitalizations for the record | Numeric
| cnt_death        | The total number of deaths for the record           | Numeric
| date_stamp_death | Date of the death of the individuals                | Date

### Aggregate File

In addition to the cleansed data, an aggregated file has been created aggregating the counts of confirmed, hospitalized, and deaths by county. The aggregate file was computed as follows:
- The county names are dropped and recoded as their 5 digit FIPS code and their code labels will be a part of the metadata.
- The records are ordered by onset date.
- The aggregates were first computed on each date, county, and then a cumulative sum was produced over the county field. 

The aggregated file ends up having the following structure. 

| name               | generic meaning | type/coding |
|--------------------|---|---|
| date_stamp         | Date of the report (Onset date)      | Date
| us_county_fips     | 5-digit county FIPS code             | Text
| cnt_confirmed      | The total number of confirmed cases  | Numeric
| cnt_hospitalized   | The total number of hospitalizations | Numeric
| cnt_death          | The total number of deaths           | Numeric
