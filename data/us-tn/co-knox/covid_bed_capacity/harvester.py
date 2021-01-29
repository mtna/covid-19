import os
import math
import pandas as pd
import datetime

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
    df['resource_type'] = df['resource_type'].map({ 'All Hospital Beds':'0', 'All Hospital Beds *':'0', 'ICU Beds': '1', 'Ventilators': '2', 'Adult Floor Beds/Non-ICU':'3' })
    df['pct_used'] = list(map(lambda x: x[:-1], df['pct_used'].values))
    df['pct_available'] = list(map(lambda x: x[:-1], df['pct_available'].values))
    df['pct_available'] = df.pct_available.str.replace('%','');
    df['date_stamp'] = fileName[0:-4]
    df['cnt_used'] = df['cnt_used']
    df['cnt_capacity'] = df['cnt_capacity']
    df['cnt_available'] = df['cnt_available']


	# apply data types
    df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')
    
    # order
    df = df[['date_stamp','resource_type','cnt_used','cnt_capacity','cnt_available','pct_used','pct_available']]
    print(df)

    return df

def deleteFiles(path):
	today = datetime.date.today();
	one_week = datetime.timedelta(days=7)
	week = today - one_week
	week_ago = datetime.datetime.combine(week, datetime.time(0, 0))
	for filename in os.listdir(path):
		if(filename.endswith('.csv')):
			newFilename = filename.replace('.csv', '');
			filedate = datetime.datetime.strptime(newFilename, '%Y-%m-%d')
			if(filedate < week_ago):
			    print('removing raw files that are more than a week old: ',path,'/',filename)
			    os.remove(f"{path}/{filename}")
	return None

if __name__ == "__main__":
    path = os.path
    # Loop over the files within the folder
    for filename in sorted(os.listdir('./data/us-tn/co-knox/covid_bed_capacity/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/us-tn/co-knox/covid_bed_capacity/clean/{filename}') == False:
            print(filename)

            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/us-tn/co-knox/covid_bed_capacity/raw/{filename}",thousands=',')
            df = cleanData(data, filename)
            df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/clean/{filename}", index=False)
        
            # if there is no aggregate file create one, otherwise append to it. 
            if path.exists(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv"):
                df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv", mode='a', header=False, index=False)
            else:
                df.to_csv(f"./data/us-tn/co-knox/covid_bed_capacity/latest.csv", index=False)
    deleteFiles('./data/us-tn/co-knox/covid_bed_capacity/raw')
    deleteFiles('./data/us-tn/co-knox/covid_bed_capacity/clean')
