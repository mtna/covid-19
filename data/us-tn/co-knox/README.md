# Knox County Data 

This directory contains several data sets pulled from the Knox County Health Department's [COVID-19 website](https://covid.knoxcountytn.gov).

This data is updated daily at 15:15 UTC (11:15am eastern time (DST)), as the Knox County COVID data updates daily at 11am.

## Age
The COVID cases [age](https://covid.knoxcountytn.gov/includes/covid_age.csv) data set provided by the Knox County health department is a data set containing the frequencies (count and percentages) of the confirmed cases by age group. 

### Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
|[empty]     | Age group.            | Text
|[empty] | Count of confirmed cases that fall in this age group.                                         | Numeric
| Percent of Cases | The percentage of confirmed cases this age group represents. | Text


### Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the age groups. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| age_group     | The age group.                                           | Text
| cnt_confirmed | Total cumulative number of confirmed and probable cases for this age group leading up to and including this date | Numeric
| pct_confirmed | The percentage of confirmed and probable cases that this age group represents on this date. | Numeric



## Bed Capacity
The Knox county [bed capacity](https://covid.knoxcountytn.gov/includes/covid_bed_capacity.csv) data set provided by the Knox County health department is a data set containing the number of total and available beds and ventilators. 

### Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| East Region Hospitals | I would think this would be hospitals, but it seems more the type of resource that is haveing its capacity measured. | Text
| Total Capacity | Total count of the resources available.                                         | Numeric
| Current Census | Count currently being used.| Text
| Available | The total count of resources that are available. | Text
| Current Utilization | The percentage of resources currently being used. | Text
| Available Capacity | The percentage of resources that is currently available. | Text


### Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the resource types. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| resource_type     | The type of resource being measured.                                     | Text
| cnt_used       | Count of resources currently being used. | Numeric
| cnt_capacity | The total capacity for this resource on this date. | Numeric
| cnt_available | The total avaiable for this resource on this date. | Numeric
| pct_used | The percentage of total resources being used for this resource type on this date. | Numeric
| pct_available | The percentage of total resources available for this resource type on this date. | Numeric


## Cases
The COVID cases data set provided by the Knox County health department is a data set containing the number of cases, recovered cases (This number is included in the number of positive cases.), active cases(The number of positive cases, excluding the number of recovered cases.), hospitalizations, currently hospitalized individuals, deaths, and probable cases.

The following definitions should be taken into account:

- Recovered refers to released from isolation.
- Information about hospitalization status is gathered at the time of diagnosis, therefore this information may be incomplete. This number indicates the number of Knox County residents that were ever hospitalized during their illness.
- This figure represents only Knox County residents currently hospitalized at any hospital.
- Probable cases are those that:
    ‐ Meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19
    ‐ Meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence.
- Probable cases are included in demographic data.

### Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| Number of Cases           | Total cumulative number of confirmed cases, including recovered cases.                               | Numeric
| Number of Recovered Cases | Total cumulative number of recovered cases.                                                         | Numeric
| Number of Active Cases    | The number of active cases (The number of positive cases, excluding the number of recovered cases). | Numeric
| Hospitalizations          | Total cumulative number of hospitalizations.                                                        | Numeric
| Currently Hospitalized    | Number of currently hospitalized individuals.                                                       | Numeric
| Deaths                    | Total cumulative number of deaths.                                                                  | Numeric
| Probable Cases            | Total cumulative number of probable cases. Probable cases are those that meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19 and meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence. | Numeric

### Clean File

We have added the date harvested to the record to build out a time series of this data. In addition we have transposed this into a single record where the variable names are not an entry in the record. 

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| date_stamp                | Date the data was harvested from the https://covid.knoxcountytn.gov/case-count.html website.                 | Date
| cnt_confirmed             | Total cumulative number of confirmed cases leading up to and including this date, including recovered cases. | Numeric
| cnt_recovered | Total cumulative number of recovered cases leading up to and including this date.                            | Numeric
| cnt_active   | The number of active cases (The number of positive cases, excluding the number of recovered cases) on this date. | Numeric
| cnt_hospitalized          | Total cumulative number of hospitalizations leading up to and including this date.                               | Numeric
| cnt_hospitalized_current  | Number of currently hospitalized individuals on this date.                                                       | Numeric
| cnt_death                 | Total cumulative number of deaths leading up to and including this date.                                         | Numeric
| cnt_probable              | Total cumulative number of probable cases leading up to and including this date. Probable cases are those that meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19 and meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence. | Numeric


## Gender
The Knox county [gender](https://covid.knoxcountytn.gov/includes/covid_gender.csv) data set provided by the Knox County health department is a data set containing the frequencies (count and percentages) of the confirmed cases by gender. 

### Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
|[empty] | Sex.          | Text
|[empty] | Count of confirmed cases that fall in this sex.                                         | Numeric
| Percent of Cases | The percentage of confirmed cases this sex represents. | Text



### Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the resource types. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| sex           | The sex of the individuals.                                           | Text
| cnt_confirmed | Total cumulative number of confirmed and probable cases for this sex leading up to and including this date | Numeric
| pct_confirmed | The percentage of confirmed and probable cases that this sex represents on this date. | Numeric



