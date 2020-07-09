# Knox County COVID Cases - Age

The COVID cases [age](https://covid.knoxcountytn.gov/includes/covid_age.csv) data set provided by the Knox County health department is a data set containing the frequencies (count and percentages) of the confirmed cases by age group. 

## Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
|     | Age group.            | Text
| | Count of confirmed cases that fall in this age group.                                         | Numeric
| Percent of Cases | The percentage of confirmed cases this age group represents. | Text


## Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the age groups. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| age_group     | The age group.                                           | Text
| cnt_confirmed | Total cumulative number of confirmed and probable cases for this age group leading up to and including this date | Numeric
| pct_confirmed | The percentage of confirmed and probable cases that this age group represents on this date. | Numeric
