# Knox County COVID Cases - Gender

The Knox county [gender](https://covid.knoxcountytn.gov/includes/covid_gender.csv) data set provided by the Knox County health department is a data set containing the frequencies (count and percentages) of the confirmed cases by gender. 

## Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| | Sex.          | Text
| | Count of confirmed cases that fall in this sex.                                         | Numeric
| Percent of Cases | The percentage of confirmed cases this sex represents. | Text



## Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the resource types. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| sex           | The sex of the individuals.                                           | Text
| cnt_confirmed | Total cumulative number of confirmed and probable cases for this sex leading up to and including this date | Numeric
| pct_confirmed | The percentage of confirmed and probable cases that this sex represents on this date. | Numeric
