# The COVID Tracking Project: US Historical Data
From the [website](https://covidtracking.com/about-project):
"The COVID Tracking Project obtains, organizes, and publishes high-quality data required to understand and respond to the COVID-19 outbreak in the United States. We will do this work until official national sources take over and publish comprehensive testing and outcomes data."

## Data:
This dataset documents the historical data gathered for the US, and the data is updated daily at 4pm. This dataset is pulled into this repository nightly at midnight EST via a bitbucket pipeline using this url to downloaad the csv: https://covidtracking.com/api/us/daily.csv.  
The site provides a spreadsheet of their current data sources for each state [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRwAqp96T9sYYq2-i7Tj0pvTf6XVHjDSMIKBdZHXiCGGdNC0ypEU9NbngS8mxea55JuCFuua1MUeOj5/pubhtml#)

### Variables:
* dateChecked - ISO 8601 date of when these values were valid.
* states - Quantity of states and territories that are reporting data.
* positive - Total cumulative positive test results.
* positiveIncrease - Increase from the day before.
* negative - Total cumulative negative test results.
* negativeIncrease - Increase from the day before.
* hospitalized - Total cumulative number of people hospitalized.
* hospitalizedIncrease - Increase from the day before.
* death - Total cumulative number of people that have died.
* deathIncrease - Increase from the day before.
* pending - Tests that have been submitted to a lab but no results have been reported yet.
* totalTestResults - Calculated value (positive + negative) of total test results.
* totalTestResultsIncrease - Increase from the day before.
* posNeg - DEPRECATED Renamed to totalTestResults.
* total - DEPRECATED Will be removed in the future. (positive + negative + pending). Pending has been an unstable value and should not count in any totals.