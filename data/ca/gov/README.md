# Government of Canada COVID-19 Updates

This repository contains processing tools and data sourced from the Government of [Coronavirus disease (COVID-19): Outbreak update](https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html) page on the Government of Canada web site. 

The following datasets can be found there:
- The embedded visualization tool has a button allowing the download of the underlying time series data in CSV format.
- A link is also provided to a time series on the [Detailed confirmed cases of coronavirus disease (COVID-19) (Preliminary data), Canada](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310076701)

## Case statistics

The case daily case statistics can be download in CSV format [from this link](https://health-infobase.canada.ca/src/data/covidLive/covid19.csv)

The dataset provides daily counts at the national and province/territoty levels

| variable | description | type/coding |
|---|---|---|
| pruid | National/Province/Territory geo-level identifier | numeric |
| prname | Geography name (en) 								|text|
| prnameFR  | Geography name (fr) 							|text|
| date | Date that the case data was reported to the Government of Canada, in ISO YYYY-MM-DD format 						|date|
| numconf | Total number of confirmed COVID-19 cases reported to the Government of Canada 						|numeric|
| numprob | Total number of probable COVID-19 cases reported to the Government of Canada					 |numeric|
| numdeaths| Total number of COVID-19 deaths reported to the Government of Canada								|numeric|
| numtotal | Sum of numconf and numprob 					|numeric|
| numtested | Total number of people tested for COVID-19 							| numeric|
| numrecorvered | Total number of individuals who have met the criteria for recovery after testing positive for COIVD-19 in Canada. 			| numeric|
| percentrecover | The percent of individuals that have recovered |numeric|
| ratetested | People tested per 1,000,000 					|numeric|
| numtoday | The amount numtotal has increased since last entry |numeric|
| percentoday | The percentage numtotal has increased since last entry | numeric|
| ratetotal | ? Added 2020-05-08 with no data in the column | numeric|

--
### Data Curation & Transformations

The following issues are being taken into account by our data processing pipeline:  
- The original data includes aggregate records for all of Canada. These are removed as these values can be computed.   
- There were a number of "N/A" values in the numrecovered and percentrecovered fields, these have been replaced with NULL.   
- The pruid has an extra code (99 Repatriated travellers) that keeps it from lining up with the standard geographic codes published by StatsCanada. The alleviate this the pruid field has been split into a province code where 99 is null, and a geocode field that preserves the original code.   
- The original dates are formatted as DD-MM-YYYY, these are reformatted to YYYY-MM-DD (ISO 8601). 
- As of 2020-05-08 there was a "ratetotal" added but the column contained no data. We will check back in on this in the future if there are values populated. what   

## Clean Data File
|variable 		| description 									| type/coding |
---------------|---------------|-------------|
| date_stamp	 | Date that the case data was reported to the Government of Canada in ISO 8601 format (YYYY-MM-DD) |date|
| ca_provterr	 | Canadian province or territory reporting the data.		|text|
| ca_covid19_geo | Canadian province or territory reporting the data, with an additional category for repatriated travellers.						|text|
| cnt_confirmed	 | Total cumulative number of confirmed COVID-19 cases reported to the Government of Canada for this province leading up to and including this date.									|numeric|
| cnt_probable	 | Number of probable COVID-19 cases reported to the Government of Canada for this province on this date.								|numeric|
| cnt_death		 | Total cumulative number of COVID-19 deaths reported to the Government of Canada for this province leading up to and including this date.										|numeric|
| cnt_total		 | The sum of confirmed (cumulative) and probable (non-cumulative) COVID-19 cases reported to the Government of Canada for this province on this date.				|numeric|
| cnt_total_new	 | Increase in total cases (confirmed + probable) since the last date. In most cases this is a single day, however, there are a few cases when there are dates wiithout an entry for a province. |numeric|
| pct_total_new	 | The percentage increase in total cases (confirmed + probable). This is calculated by dividing the increase in total cases (cnt_total_new) by the number of total cases (cnt_total) of the previous date. In most cases this is a single day, however, there are a few cases when there are dates wiithout an entry for a province. |numeric|
| cnt_tested	 | Total cumulative number of individuals tested for COVID-19 for this province leading up to and including this date. |numeric|
| cnt_recovered	 | Total cumulative number of individuals who have met the criteria for recovery after testing positive for COIVD-19 for this province leading up to and including this date. |numeric|
| pct_recovered	 | Percentage of recovered individuals. This is calculated by dividing the count of recovered individuals (cn_recovered) by the total count of cases (cnt_total).  |numeric|

