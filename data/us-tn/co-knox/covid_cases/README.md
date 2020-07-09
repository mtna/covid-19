# Knox County COVID Cases

The COVID cases data set provided by the Knox County health department is a data set containing the number of cases, recovered cases (This number is included in the number of positive cases.), active cases(The number of positive cases, excluding the number of recovered cases.), hospitalizations, currently hospitalized individuals, deaths, and probable cases.

The following definitions should be taken into account:

- Recovered refers to released from isolation.
- Information about hospitalization status is gathered at the time of diagnosis, therefore this information may be incomplete. This number indicates the number of Knox County residents that were ever hospitalized during their illness.
- This figure represents only Knox County residents currently hospitalized at any hospital.
- Probable cases are those that:
    ‐ Meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19
    ‐ Meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence.
- Probable cases are included in demographic data.

## Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| Number of Cases           | Total cumulative number of confirmed cases, including recovered cases.                               | Numeric
| Number of Recovered Cases | Total cumulative number of recovered cases.                                                         | Numeric
| Number of Active Cases    | The number of active cases (The number of positive cases, excluding the number of recovered cases). | Numeric
| Hospitalizations          | Total cumulative number of hospitalizations.                                                        | Numeric
| Currently Hospitalized    | Number of currently hospitalized individuals.                                                       | Numeric
| Deaths                    | Total cumulative number of deaths.                                                                  | Numeric
| Probable Cases            | Total cumulative number of probable cases. Probable cases are those that meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19 and meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence. | Numeric

## Clean File

We have added the date harvested to the record to build out a time series of this data. In addition we have transposed this into a single record where the variable names are not an entry in the record. 

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| date_stamp                | Date the data was harvested from the https://covid.knoxcountytn.gov/case-count.html website.                 | Date
| cnt_confirmed             | Total cumulative number of confirmed cases leading up to and including this date, including recovered cases. | Numeric
| cnt_recovered | Total cumulative number of recovered cases leading up to and including this date.                            | Numeric
| cnt_active   | The number of active cases (The number of positive cases, excluding the number of recovered cases) on this date. | Numeric
| cnt_hospitalized          | Total cumulative number of hospitalizations leading up to and including this date.                               | Numeric
| cnt_hospitalized_current  | Number of currently hospitalized individuals on this date.                                                       | Numeric
| cnt_death                 | Total cumulative number of deaths leading up to and including this date.                                         | Numeric
| cnt_probable              | Total cumulative number of probable cases leading up to and including this date. Probable cases are those that meet clinical criteria AND epidemiologic evidence with no confirmatory laboratory testing performed for COVID-19 and meet presumptive laboratory evidence AND either clinical criteria OR epidemiologic evidence. | Numeric