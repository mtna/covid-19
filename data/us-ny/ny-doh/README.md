# New York State Statewide COVID-19 Testing Data

Pulled daily from the New York State Health Data page at https://health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Testing/xdss-u53e/data

### General Overview:

SARS-CoV2, a novel coronavirus, was first identified as the cause of an outbreak of respiratory illness in Wuhan, Hubei Province, China in 2019. There are many coronaviruses, all of which typically cause respiratory disease in humans. The World Health Organization (WHO) named the disease caused by SARS-CoV2 “COVID-19.” In March 2020, WHO declared COVID-19 a pandemic due to the number of countries affected by its rapid spread.
This dataset is composed of information on all of the tests of individuals for COVID-19 infection performed in New York State beginning March 1, 2020, when the first case of COVID-19 was identified in the state. The data is collected and maintained by the New York State Department of Health (NYSDOH) and includes the date each individual was tested and the county associated with the tested individual (see the Data Methodology section below f or more information about how county is assigned). The primary goal of publishing this dataset is to provide users timely information about local disease spread and reporting of positive cases. As of the publication of this document, the data is updated daily, covering all tests completed before 12:00am the day of the update (i.e., all tests completed by the end of the day on the day before the update, for example, the update for April 3, 2020, will reflect all tests completed by the end of the day on April 2, 2020).
The data captures all individuals tested for SARS-CoV2 virus reported to NYSDOH since March 1, 2020 that meet set laboratory result criteria (see Data Methodology). The data do not represent persons with COVID-19 clinical diagnoses by a provider without laboratory confirmation.
Additional information on COVID-19 can be found here:
https://coronavirus.health.ny.gov/home

### Data Methodology:

Reporting of SARS-CoV2 laboratory testing results is mandated under Part 2 of the New York State Sanitary Code. Clinical laboratories, as defined in Public Health Law (PHL) § 571 electronically report test results to the NYSDOH via the Electronic Clinical Laboratory Reporting System (ECLRS). The NYSDOH Division of Epidemiology’s Bureau of Surveillance and Data System (BSDS) monitors the reporting and ensures that all positives and negatives are accurately counted. Test counts reflect those completed on an individual each day. A person may have multiple specimens tested on one day, these would be counted one time —i.e., if two specimens are collected from an individual at the same time and then evaluated, the outcome of the evaluation of those two samples to diagnose the individual is counted as a single test of one person, even though the specimens may be tested separately . Conversely, if an individual is tested on more than one day, the data will show two tests of an individual, one for each date the person was tested.
Test counts are assigned to a county based on this order of preference: 1) the patient’s address, 2) the ordering healthcare provider’s address, or 3) the ordering facility’s address.

### Limitations of Use:

The SARS-CoV2 laboratory test result data on this site reflects the best information available to NYSDOH at the time the data is posted.
The total number of tests of individuals performed include all positive, negative, and inconclusive results. Despite the relatively small proportion of inconclusive results, it is not appropriate to subtract the number of individuals tested positive from the total number of individuals tested to calculate the total individuals tested negative.

## Original data file:
|variable name | description | type/coding|
|--------------|------------|-------------|
| Test Date 	|The date the test result was processed by the NYS Electronic Clinical Laboratory Reporting System (ECLRS). | date |
| County 		|  The county of residence for the person tested. | text|
| New positives | The number of new persons tested positive for COVID-19 infection on the test date in each county. | numeric |
| Cumulative number of positives | Running total for the number of persons tested positive for COVID- 19 infection in each county as of the test date. | numeric |
| Total number of tests performed | The number of tests of individuals performed on the test date in each county. This total includes positives, negatives, and inconclusive results. | numeric |
| Cumulative number of tests performed | Running total for the number of tests of individuals performed in each county as of the last update to the dataset. This total includes positives, negatives, and inconclusive results. | numeric |

### Data Curation & Transformations

The following issues are being taken into account by our data processing pipeline:  
- The data uses county names rather than codes. Our version converts to FIPS codes to facilitate analysis and linking.

### Clean data file
|variable name 		| description 									| type/coding|
|--------------		|------------									|-------------|
|date_stamp			|The record date in ISO 8601 format (YYYY-MM-DD)|date|
|us_county_fips		|U.S. FIPS 6-4 county code (5-digit)			|text|
|cnt_confirmed_new	|Number of cases confirmed since last entry		|numeric|
|cnt_confirmed		|Count of confirmed cases						|numeric|
|cnt_tested_new		|Number of tests performed since last entry		|numeric|
|cnt_tested			|Count of tests conducted						|numeric|


