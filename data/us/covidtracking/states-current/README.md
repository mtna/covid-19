# The COVID Tracking Project: States' Current Data
From the [website](https://covidtracking.com/about-project):
"The COVID Tracking Project obtains, organizes, and publishes high-quality data required to understand and respond to the COVID-19 outbreak in the United States. We will do this work until official national sources take over and publish comprehensive testing and outcomes data."

## Data:
This dataset documents the current values that states are reporting via their state websitets, and is updated on the website periodically throughout the day. This dataset is pulled into this repository nightly at midnight EST via a bitbucket pipeline using this url to downloaad the csv: https://covidtracking.com/api/v1/states/current.csv.  
The site provides a spreadsheet of their current data sources for each state [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRwAqp96T9sYYq2-i7Tj0pvTf6XVHjDSMIKBdZHXiCGGdNC0ypEU9NbngS8mxea55JuCFuua1MUeOj5/pubhtml#)

### Variables:
* state - State or territory postal code abbreviation.
* positive - Total cumulative positive test results.
* positiveScore - +1 for reporting positives reliably.
* negative - Total cumulative negative test results.
* negativeScore - +1 for reporting negatives sometimes.
* negativeRegularScore - +1 for reporting negatives reliably.
* commercialScore - +1 for reporting all commercial tests.
* score - Total reporting quality score.
* grade - Letter grade based on score.
* totalTestResults - Calculated value (positive + negative) of total test results.
* hospitalized - Total cumulative number of people hospitalized.
* death - Total cumulative number of people that have died.
* dateModified - ISO 8601 date of the time the data was last updated by the state.
* dateChecked - ISO 8601 date of the time we last visited their website
* hash - A unique ID changed every time the data updates.
* total - DEPRECATED Will be removed in the future. (positive + negative + pending). Pending has been an unstable value and should not count in any totals.