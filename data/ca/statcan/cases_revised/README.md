# Statistics Canada: Detailed preliminary information on confirmed cases of COVID-19 (Revised), Public Health Agency of Canada
*From website:*  
Given that the COVID-19 pandemic is rapidly evolving, these data are considered preliminary. The data published by Statistics Canada only account for those where a detailed case report was provided by the provincial or territorial jurisdiction to the Public Health Agency of Canada (PHAC). Statistics Canada’s detailed preliminary confirmed cases will not match the total case reporting done at the provincial and territorial levels which are reported daily by each jurisdiction and compiled by the PHAC. The discrepancy is due to delays associated with the submission of the detailed information, its capture and coding. Hence, Statistics Canada’s file on detailed case reporting is a subset of the total counts reported by the health authorities across Canada.   

On May 22nd, 2020, this data file of detailed confirmed cases from the Public Health Agency of Canada (PHAC) replaced data published in table 13-10-0766-01. This covers all of the detailed confirmed cases up to May 13th, but with new Statistics Canada Case identifier numbers.  

*MTNA Note:*
This data is pulled daily from the [Statistics Canada website](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310078101) which details the confirmed cases of COVID-19. This data is the [entire table](https://www150.statcan.gc.ca/n1/tbl/csv/13100766-eng.zip), which does not match the displayed HTML table in format. This seems to be a CSV file that is structured more like an SDMX cube. In the CSV file there are several columns of interest, REF_DATE, Case Identifier number, Case information, and VALUE.The REF_DATE and Case Identifier number are the same for a record, but a single record in the HTML table is spread out over 13 records, each with a different VALUE for a specific Case information. With this in mind the following items of interest are available in the source file:

*Metadata obtained from the [COVID-19 Data Dictionary and User Guide](https://www150.statcan.gc.ca/n1/pub/13-26-0002/132600022020001-eng.htm)*

| Variable Name | Label | Data Type / Codes|
|---------------|-------|-----------|
| REF_DATE                             | The year the observations were made.            | Numeric
| Case identifier number             | Statistics Canada generated case identifier number.   | Numeric - Continuous value from 1 to 99999999
| Region   							 | Province/Territory where the case resides, grouped by regions.	                          | 1 = Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador), 2 = Quebec, 3 = Ontario and Nunavut, 4 = Prairies (Alberta, Saskatchewan, and Manitoba) and the Northwest Territories, 5 = British Columbia and Yukon.
| Episode week     					 | Week of the episode, derived using symptom onset date or the closest date available. The episode date is created from the earliest date available from the following series: Symptom Onset Date, Specimen Collection Date and Laboratory Testing Date. When no date is available, this field is considered 'Not stated' and given the value 99. "0" represents the first days of the year leading up to, but not including the first Sunday. "1" represents the first full week of the year, beginning on the first Sunday, and so on. | Numeric -  Continuous value from 0 to 52, 99=Not stated
| Episode year						 |Year of the episode, derived using symptom onset date or the closest date available. The episode date is created from the earliest date available from the following series: Symptom Onset Date, Specimen Collection Date and Laboratory Testing Date. When no date is available, this field is considered 'Not stated' and given the value 99.		| Numeric - Only year 2020 at this point, 9999=Not stated
| Gender                              | The gender of the case	. It should be noted that the French form uses the term 'sex' contrary to the English form that uses the term 'gender'. In the context of this table, the term gender is also used in French. The cases that have reported 'other' for sex or 'non-binary' for gender have been reclassified as 'not stated' gender.  | 1 = Male, 2 = Female, 9 = Not stated
| Age group                           | Age group corresponding to the age of the case	                                       | 1 = 0 to 19 years, 2 = 20 to 29 years, 3 = 30 to 39 years, 4 = 40 to 49 years, 5 = 50 to 59 years, 6 = 60 to 69 years, 7 = 70 to 79 years, 8 = 80 years or older, 99 = Not stated
| Occupation						| Indicates the case's occupation<sup>1</sup>					|1 = Health care worker, 2 = School or daycare worker/attendee, 3 = Long term care resident, 4 = Other, 9 = Not stated.
|Asymptomatic						| Indicates if the case was asymptomatic. Derived from the symptoms. If no symptoms were experienced, then asymptomatic is yes. If any symptoms were experienced then asymptomatic is no. 				| 1= Yes, 2 = No, 9 = Not Stated.
| Onset week of symptoms			| Week of symptom(s) onset. "0" represents the first days of the year leading up to, but not including the first Sunday. "1" represents the first full week of the year, beginning on the first Sunday, and so on.	| Numeric - Continuous value from 0 to 52, 99=Not stated or Not applicable
| Onset year of symptoms			|Year of symptom(s) onset		| Numeric - Only year 2020 at this point, 9999=Not stated or Not applicable
| Symptom, cough	| Case reported cough	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, fever	|Case reported fever (≥38°C)	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, chills	|Case reported feverish/chills (temperature not taken)	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, sore throat	|Case reported sore throat	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, runny nose	|Case reported runny nose	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, shortness of breath	|Case reported shortness of breath/difficulty breathing	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, nausea	|Case reported nausea/vomiting	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, headache	|Case reported headache	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, weakness	|Case reported general weakness	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, pain		|Case reported pain (muscular, chest, abdominal, joint)	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, irritability	|Case reported irritability/confusion	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, diarrhea	|Case reported diarrhea	|1=Yes, 2=No, 9=Not Stated/Unknown
| Symptom, other	|Case reported other symptoms	|1=Yes, 2=No, 9=Not Stated/Unknown
| Hospital status                      | Indicates if the case was hospitalized and if the case was admitted to the intensive care unit. | 1=Hospitalized - ICU, 2=Hospitalized - Non-ICU, 3=Not Hospitalized, 9=Not stated/Unknown
| Recovered 							| Indicates if the case has recovered. 	|1 = Yes, 2 = No, 9 = Not Stated/Unknown.
| Recovery week							| Week of recovery date. "0" represents the first days of the year leading up to, but not including the first Sunday. "1" represents the first full week of the year, beginning on the first Sunday, and so on.	| Numeric - Continuous value from 0 to 52, 99=Not stated/Not applicable
| Recovery year							| Year of recovery date | Numeric = Only year 2020 at this point, 9999=Not stated/Not applicable
| Death                                | Indicates if the case died while infected by COVID-19.	                                           | 1 = Yes, 2 = No, 9 = Not Stated
| Transmission                         | Location where exposure occurred<sup>2</sup>	                             | 1 = Domestic acquisition - Contact of COVID case, contact with traveller, or unknown source, 2 = International travel, 9 = Not stated.

## Data Curation & Transformation

We perform the following cleansing and transformations on this file:

- Rename the columns to better match our other harmonized files.
- Combine episode year and week into a single weekstamp variable, "episode_weekstamp"
- Combine recovery year and week into a single weekstamp variable, "recovery_weekstamp"
- Combine onset year and week into a single weekstamp variable, "onset_weekstamp"
- Change the data types of the coded values to text.
- Recoded the age groups.


The final data structure is as follows:

| Variable Name | Label | Data Type / Codes|
|---------------|-------|-----------|
| case_id                    | Case Identifier **Up until 2020-05-12 this was consistent and unique per case. On 2020-05-12 the identifier seemed to be used for a different case and no longer appears to be a trustworthy way to identify a case over multiple days** | Text
| age_group                  | The age group the individual is a part of                                                                                                           | 00 = 0 to 19 years, 20 = 20 to 29 years, 30 = 30 to 39 years, 40 = 40 to 49 years, 50 = 50 to 59 years, 60 = 60 to 69 years, 70 = 70 to 79 years, 80 = 80 years or older, 99 = Not stated
| asymptomatic					|Indicates if the case was asymptomatic. Derived from the symptoms. If no symptoms were experienced, then asymptomatic is yes. If any symptoms were experienced then asymptomatic is no.													|1= Yes, 2 = No, 9 = Not Stated.
| is_deceased                | Indicates if the case died while infected by COVID-19.	                                                                                                 | 1 = Yes, 2 = No, 9 = Not Stated
| gender                     | The gender of the individual                                                                                                                        | 1 = Male, 2 = Female, 3 = Non-binary, 9 = Not stated
| is_hospitalized            | Indicates if the individual is currently hospitalized.                                                                                              | 1=Hospitalized - ICU, 2=Hospitalized - Non-ICU, 3=Not Hospitalized, 9=Not stated/Unknown
| occupation				| The individual's occupation. <sup>1</sup>													|1 = Health care worker, 2 = School or daycare worker/attendee, 3 = Long term care resident, 4 = Other, 9 = Not stated.
| is_recovered				| Indicates if the case has recovered. 	|1 = Yes, 2 = No, 9 = Not Stated/Unknown.
| region					|Province/Territory where the case resides, grouped by regions.	                          | 1 = Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador), 2 = Quebec, 3 = Ontario and Nunavut, 4 = Prairies (Alberta, Saskatchewan, and Manitoba) and the Northwest Territories, 5 = British Columbia and Yukon.
| symptom_chills			|Case reported feverish/chills (temperature not taken)	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_cough				|Case reported cough	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_diarrhea			|Case reported diarrhea	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_fever				|Case reported fever (≥38°C)	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_headache			|Case reported headache	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_irritability		|Case reported irritability/confusion	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_nausea			|Case reported nausea/vomiting	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_other				|Case reported other symptoms	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_pain				|Case reported pain (muscular, chest, abdominal, joint)	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_runny_nose		|Case reported runny nose	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_short_breath		|Case reported shortness of breath/difficulty breathing	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_sore_throat		|Case reported sore throat	|1=Yes, 2=No, 9=Not Stated/Unknown
| symptom_weakness			|Case reported general weakness	|1=Yes, 2=No, 9=Not Stated/Unknown
| transmission          | How the individual was exposed to the virus. These values are corrected as the Public Health Agency of Canada (PHAC) receives new information.<sup>2</sup>      | 1=Domestic Acquisition: “Contact of COVID Case” or “Contact with traveler” or “Unknown Source”, 2=International Travel, 9=Not stated/Pending
| recovered_weekstamp	|The week and year of recovery date. This is obtained by combining the "Recovery week" and "Recovery year" variables. |YYYY-Www (ex: 2020-W01)
| onset_weekstamp		|The week and year of symptom(s) onset.														|YYYY-Www (ex: 2020-W01)
| episode_weekstamp		|Week of the episode, derived using symptom onset date or the closest date available. The episode date is created from the earliest date available from the following series: Symptom Onset Date, Specimen Collection Date and Laboratory Testing Date.	|YYYY-Www (ex: 2020-W01)


Notes:  
1. **Occupation**: Healthcare workers include those with and without direct patient contact. Long-term care residents may include residents of senior's homes, assisted living facilities, and retirement communities, as well as nursing homes. Long-term care facilities may be privately run or under provincial authority. Laboratory worker handling biological specimens, Veterinary/animal worker and Farm worker have been categorized with the "Other" due to low frequencies.  
2. **Transmission**:    
	 * Domestic acquisition – Contact of COVID case: Includes cases who reported having close contact with a confirmed or probable COVID-19 case in the 14 days prior to symptom onset. Domestic acquisition– Contact with traveler: Includes cases who reported having close contact with a symptomatic person who had traveled to an affected area in the 14 days prior to their illness onset. Domestic acquisition – Unknown source: Includes cases who had not travelled, and 1) who had reported no contact with a COVID-19 case or symptomatic traveller, or 2) whose information on contact with a case or contact with a symptomatic traveler was unknown or missing.  
	 * International travel: Includes cases who reported having travelled outside of their province / territory of residence or outside of Canada within the 14 days prior to symptom onset.  
	 * Information pending: Includes cases for which information on contact with a case, contact with a symptomatic traveler, and travel history were all missing or unknown.  