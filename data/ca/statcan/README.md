# Statistics Canada: Detailed confirmed cases of coronavirus disease (COVID-19) (Preliminary data), Canada
This data is pulled daily from the [Statistics Canada website](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310076601) which details the confirmed cases of COVID-19. This data is the [entire table](https://www150.statcan.gc.ca/n1/tbl/csv/13100766-eng.zip), which does not match the displayed HTML table in format. This seems to be a CSV file that is structured more like an SDMX cube. In the CSV file there are several columns of interest, REF_DATE, Case Identifier number, Case information, and VALUE.The REF_DATE and Case Identifier number are the same for a record, but a single record in the HTML table is spread out over 13 records, each with a different VALUE for a specific Case information. With this in mind the following items of interest are availble in the source file:

| Variable Name | Label | Data Type / Codes|
|---------------|-------|-----------|
| REF_DATE                             | The year the observations were made.            | Numeric
| Case identifier number               | Case identifier                                 | Numeric
| Date case was last updated - month   | Case update month (MM)                          | Numeric
| Date case was last updated - day     | Case update day (DD)                            | Numeric
| Episode date - month                 | Episode month (MM)                              | Numeric
| Episode date - day                   | Episode day (DD)                                | Numeric
| Gender                               | Gender                                          | 1 = Male, 2 = Female, 3 = Non-binary, 9 = Not stated
| Age group                            | Age group                                       | 1 = 0 to 19 years, 2 = 20 to 29 years, 3 = 30 to 39 years, 4 = 40 to 49 years, 5 = 50 to 59 years, 6 = 60 to 69 years, 7 = 70 to 79 years, 8 = 80 years or older, 99 = Not stated
| Transmission                         | Transmission mode                               | 1= Travel exposure – cases that had contact with a travel-related case or had travelled outside of Canada in the 14 days prior to illness onset. 2 = Community exposure – cases that had no known contact with a travel-related case and had not travelled outside of Canada in the 14 days prior to illness onset. 3 = Pending – confirmation on exposure setting is pending. 
| Hospitalization                      | Hospitalized                                    | 1 = Yes, 2 = No, 9 = Not Stated
| Intensive care unit                  | In ICU                                          | 1 = Yes, 2 = No, 9 = Not Stated
| Death                                | Death                                           | 1 = Yes, 2 = No, 9 = Not Stated
| Hospitalization, previous status     | Hospitalize (previous)                          | 1 = Yes, 2 = No, 9 = Not Stated. New cases loaded to the database each day will display ".." (Not available) for these previous status variables.
| Intensive care unit, previous status | Indicates the previous status for the variable. | 1 = Yes, 2 = No, 9 = Not Stated. New cases loaded to the database each day will display ".." (Not available) for these previous status variables.
| Death, previous status               | Indicates the previous status for the variable. | 1 = Yes, 2 = No, 9 = Not Stated. New cases loaded to the database each day will display ".." (Not available) for these previous status variables.

## Data Curation & Transformation

We perform the following cleansing and transformations on this file:

- Rename the columns to better match our other harmonized files.
- Combine the REF_DATE, Date case was last updated - month and day into a single date_stamp_update ISO 8601 date variable.
- Combine bring the REF_DATE, Episode date - month and day into a single date_stamp ISO 8601 date variable.
- Change the data types of the coded values to text.
- Recoded the age groups.
- The '..' in the previous status variables are replaced with empty values. 

The final data structure is as follows:

| Variable Name | Label | Data Type / Codes|
|---------------|-------|-----------|
| case_id                    | Case Identifier **Up until 2020-05-12 this was consistent and unique per case. On 2020-05-12 the identifier seemed to be used for a different case and no longer appears to be a trustworthy way to identify a case over multiple days** | Text
| episode_start_date         | Episode Start Date. This is created by combining REF_DATE, Episode date month and day together. This is obtained by Statistics Canada as the earliest date available from the following series: Symptom Onset Date, Specimen Collection Date and Laboratory Testing Date. | Date
| date_stamp                 | Last Update Date. The date the case was last updated. All the following metrics relate to this date with the exception of the *_previous variables. | Date
| gender                     | The gender of the individual                                                                                                                        | 1 = Male, 2 = Female, 3 = Non-binary, 9 = Not stated
| age_group                  | The age group the individual is a part of                                                                                                           | 00 = 0 to 19 years, 20 = 20 to 29 years, 30 = 30 to 39 years, 40 = 40 to 49 years, 50 = 50 to 59 years, 60 = 60 to 69 years, 70 = 70 to 79 years, 80 = 80 years or older, 99 = Not stated
| transmission_type          | How the individual was exposed to the virus. These values are corrected as the Public Health Agency of Canada (PHAC) receives new information.      | 1= Travel exposure – cases that had contact with a travel-related case or had travelled outside of Canada in the 14 days prior to illness onset. 2 = Community exposure – cases that had no known contact with a travel-related case and had not travelled outside of Canada in the 14 days prior to illness onset. 3 = Pending – confirmation on exposure setting is pending.
| is_hospitalized            | Indicates if the individual is currently hospitalized.                                                                                              | 1 = Yes, 2 = No, 9 = Not Stated
| is_hospitalized_previous   | Indicates the individuals previous hospitalization status if available. This indicates a change in status that could be due to data cleaning by provinces and territories and should not be interpreted to mean that the case had been discharged from the hospital. | 1 = Yes, 2 = No, 9 = Not Stated 
| is_intensive_care          | Indicates if the individual is currently in an intensive care unit.                                                                                 | 1 = Yes, 2 = No, 9 = Not Stated
| is_intensive_care_previous | Indicates the individuals previous intensive care unit status if available.                                                                         | 1 = Yes, 2 = No, 9 = Not Stated
| is_deceased                | Indicates if the individual is currently deceased.                                                                                                  | 1 = Yes, 2 = No, 9 = Not Stated
| is_deceased_previous       | Indicates the individuals previous deceased status if available.                                                                                    | 1 = Yes, 2 = No, 9 = Not Stated
