import os
import math
import pandas as pd

variables = {
	'East Region Hospitals': 'resource_type',
	'Current Census': 'cnt_used',
	'Total Capacity': 'cnt_capacity',
	'Available': 'cnt_available',
	'Current Utilization': 'pct_used',
	'Available Capacity': 'pct_available'
}


def cleanData(data, fileName):
    # source data frame from csv file
    df = pd.DataFrame(data)
    df.rename(variables, axis="columns", inplace=True)
    print(df)
	
    # the target data frame
    df['resource_type'] = df['resource_type'].map({ 'All Hospital Beds':'0', 'ICU Beds': '1', 'Ventilators': '2' })
    df['pct_used'] = list(map(lambda x: x[:-1], df['pct_used'].values))
    df['pct_available'] = list(map(lambda x: x[:-1], df['pct_available'].values))
    df['date_stamp'] = fileName[0:-4]

	# apply data types
    df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')
    
    # order
    df = df[['date_stamp','resource_type','cnt_used','cnt_capacity','cnt_available','pct_used','pct_available']]
    print(df)

    return df

if __name__ == "__main__":
    path = os.path
    # Loop over the files within the folder
    for filename in sorted(os.listdir('./data/us-tn/co-knox/covid_bed_capacity/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/us-tn/co-knox/covid_bed_capacity/clean/{filename}') == False:
            print(filename)

            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/us-tn/co-knox/covid_bed_capacity/raw/{filename}")
            df = cleanData(data, filename)
            df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/clean/{filename}", index=False)
        
            # if there is no aggregate file create one, otherwise append to it. 
            if path.exists(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv"):
                df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv", mode='a', header=False, index=False)
            else:
                df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv", index=False)