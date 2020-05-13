# The COVID Tracking Project: States' Information Data
From the [website](https://covidtracking.com/about-project):
"The COVID Tracking Project obtains, organizes, and publishes high-quality data required to understand and respond to the COVID-19 outbreak in the United States. We will do this work until official national sources take over and publish comprehensive testing and outcomes data."

## Data:
This dataset contains information about data sources for each state, along with notes aobut the data. This dataset is pulled nightly at midnight EST via a bitbucket pipeline using this url to downloaad the csv: https://covidtracking.com/api/v1/states/info.csv.  
The site provides a spreadsheet of their current data sources for each state [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRwAqp96T9sYYq2-i7Tj0pvTf6XVHjDSMIKBdZHXiCGGdNC0ypEU9NbngS8mxea55JuCFuua1MUeOj5/pubhtml#)

### Variables:
* state
* covid19SiteOld
* covid19Site
* covid19SiteSecondary
* twitter
* pui
* pum
* notes
* fips
* name


