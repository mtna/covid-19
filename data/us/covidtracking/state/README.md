# The COVID Tracking Project: States' Historical Data

From the [COVID Tracking Website](https://covidtracking.com/about-project):

"The COVID Tracking Project obtains, organizes, and publishes high-quality data required to understand and respond to the COVID-19 outbreak in the United States. We will do this work until official national sources take over and publish comprehensive testing and outcomes data."

## States Historical Data:

This dataset documents the cumulative values that states are reporting via their state websitets. This dataset is updated daily on the COVID tracking website every day and pulled into our repository nightly at midnight EST via a bitbucket pipeline using this url to downloaad the csv: https://covidtracking.com/api/v1/states/daily.csv.  

The site provides a spreadsheet of their current data sources for each state [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRwAqp96T9sYYq2-i7Tj0pvTf6XVHjDSMIKBdZHXiCGGdNC0ypEU9NbngS8mxea55JuCFuua1MUeOj5/pubhtml#)

The source CSV file has the following structure:

| name                | generic meaning | type/coding |
|---------------------|---|---|
| date                     | Date of the record in format yyyyMMdd.                                                                                                            | Numeric
| state                    | State or territory postal code abbreviation.                                                                                                      | Text
| positive                 | Total cumulative positive test results.                                                                                                           | Numeric
| negative                 | Total cumulative negative test results.                                                                                                           | Numeric
| pending                  | Tests that have been submitted to a lab but no results have been report yet.                                                                      | Numeric
| hospitalizedCurrently    | Number of individuals currently hospitalized.                                                                                                     | Numeric
| hospitalizedCumulative   | Total number of individuals that have been hospitalized, including those that have been discharged.                                               | Numeric
| inIcuCurrently           | Number of individuals currently in an ICU.                                                                                                        | Numeric
| inIcuCumulative          | Total number of individuals that have been in the ICU.                                                                                            | Numeric
| onVentilatorCurrently    | Number of individuals currently on a ventilator.                                                                                                  | Numeric
| onVentilatorCumulative   | Total number of individuals that have been on a ventilator.                                                                                       | Numeric
| recovered                | Total number of individuals that have tested negative after a previous positive test.                                                             | Numeric
| hash                     | A records unique ID.                                                                                                                              | Text
| dateChecked              | ISO 8601 date of the time we saved visited their website.                                                                                         | Datetime
| death                    | Total cumulative number of people that have died.                                                                                                 | Numeric
| hospitalized             | Total cumulative number of people hospitalized.                                                                                                   | Numeric
| ~~total~~                | DEPRECATED Will be removed in the future. (positive + negative + pending). Pending has been an unstable value and should not count in any totals. | Numeric
| totalTestResults         | Calculated value (positive + negative) of total test results.                                                                                     | Numeric
| ~~posNeg~~               | DEPRECATED Renamed to totalTestResults.                                                                                                           | Numeric
| fips                     | Federal Information Processing Standard state code 2-digit numeric (these are numeric and therefore cannot be 0 padded)                           | Numeric
| deathIncrease            | Increase from the day before.                                                                                                                     | Numeric
| hospitalizedIncrease     | Increase from the day before.                                                                                                                     | Numeric
| negativeIncrease         | Increase from the day before.                                                                                                                     | Numeric
| positiveIncrease         | Increase from the day before.                                                                                                                     | Numeric
| totalTestResultsIncrease | Increase from the day before.                                                                                                                     | Numeric

## Data Curation & Transformation

We perform the following cleansing and transformations on the state historical file:

- Rename the variables to be aligned with the harmonized variable names that we use across files.
- Reformat the date variable to ISO 8601 format (YYYY-MM-DD).
- Make the 2 digit FIPS code a string and 0 pad the single digit values.
- Reorder the variables so the like variables are together. 
- The hospitalized and hospitalized cumulative were exact duplicates of each other in terms of values, so we have dropped the cumulative column and documented the change on the hospitalized variable.
- Dropped the deprecated values.

The cleansed file structure is as follows:

| name                | generic meaning | type/coding |
|---------------------|---|---|
| hash                     | The records unique identifier. This is generated every time the [current](https://covidtracking.com/api) formats are updated, but stay consistent per record in the historical files.                          | Text
| date_stamp               | The record date in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)                                                                                                                                   | Date
| datetime_checked         | ISO 8601 date of the time that covid tracker saved / visited the states website. This always seems to be at T20:00:00Z and we contemplated taking it out but it may be helpful to provide context about when the data was collected and clear up any questions about missing data due to a difference in time of data published vs data collected. | Datetime
| us_state_postal          | The [U.S. State 2-letter postal code](https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations) of the state this record represents.                                                                     | Text
| us_state_fips            | U.S. [FIPS 5-2 code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code) of the state this record represents.                                                                    | Text
| cnt_tested_pos           | Total cumulative positive test results.                                                                                                                                                                        | Numeric
| cnt_tested_pos_new       | Increase in positive test results (cnt_tested_pos) from the day before.                                                                                                                                        | Numeric
| cnt_tested_neg           | Total cumulative negative test results.                                                                                                                                                                        | Numeric
| cnt_tested_neg_new       | Increase in negative test results (cnt_tested_neg) from the day before.                                                                                                                                        | Numeric
| cnt_tested_pending       | Tests that have been submitted to a lab but no results have been report yet. This seems to be the total value of current pending tests as opposed to new tests that have been flagged as pending on this date. | Numeric
| cnt_recovered            | Total number of individuals that have tested negative after a previous positive test.                                                                                                                          | Numeric
| cnt_death                | Total cumulative number of individuals that have died.                                                                                                                                                         | Numeric
| cnt_death_new            | Increase in number of individuals that have died (cnt_death) from the day before.                                                                                                                              | Numeric
| cnt_hospitalized         | Total cumulative number of individuals hospitalized. The counts were duplicates of the hospitalizedCumulative variable, which indicated that this count includes individuals that have been discharged.        | Numeric
| cnt_hospitalized_new     | Increase in number of individuals that have been hospitalized (cnt_hospitalized) from the day before.                                                                                                          | Numeric
| cnt_hospitalized_current | Number of individuals currently hospitalized.                                                                                                                                                                  | Numeric
| cnt_icu_current          | Number of individuals currently in an ICU.                                                                                                                                                                     | Numeric
| cnt_icu_total            | Total number of individuals that have been in the ICU.                                                                                                                                                         | Numeric
| cnt_vent_current         | Number of individuals currently on a ventilator.                                                                                                                                                               | Numeric
| cnt_vent_total           | Total number of individuals that have been on a ventilator.                                                                                                                                                    | Numeric
| cnt_tested               | Calculated value (cnt_tested_pos + cnt_tested_neg) of total test results.                                                                                                                                      | Numeric
| cnt_tested_new           | Increase in number of total test results (cnt_tested) from the day before.                                                                                                                                     | Numeric