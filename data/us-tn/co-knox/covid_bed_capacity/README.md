# Knox County COVID Cases - Capacity

The Knox county [bed capacity](https://covid.knoxcountytn.gov/includes/covid_bed_capacity.csv) data set provided by the Knox County health department is a data set containing the number of total and available beds and ventilators. 

## Original File

| name                      | generic meaning | type/coding |
|---------------------------|---|---|
| East Region Hospitals | I would think this would be hospitals, but it seems more the type of resource that is haveing its capacity measured. | Text
| Total Capacity | Total count of the resources available.                                         | Numeric
| Current Census | Count currently being used.| Text
| Available | The total count of resources that are available. | Text
| Current Utilization | The percentage of resources currently being used. | Text
| Available Capacity | The percentage of resources that is currently available. | Text


## Clean File

We have added the date_stamp (date of processing) to the record to build out a time series of this data. We have also coded the resource types. 

| name          | generic meaning | type/coding |
|---------------|---|---|
| date_stamp    | Date the data was harvested from the knox county website.                 | Date
| resource_type     | The type of resource being measured.                                     | Text
| cnt_used       | Count of resources currently being used. | Numeric
| cnt_capacity | The total capacity for this resource on this date. | Numeric
| cnt_available | The total avaiable for this resource on this date. | Numeric
| pct_used | The percentage of total resources being used for this resource type on this date. | Numeric
| pct_available | The percentage of total resources available for this resource type on this date. | Numeric
