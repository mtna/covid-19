import os
import math
import pandas as pd
import datetime

variables = [
	'date_stamp',
	'cnt_confirmed',
	'cnt_recovered',
	'cnt_active',
	'cnt_hospitalized',
	'cnt_hospitalized_current',
	'cnt_death',
	'cnt_probable'
]
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
			    print('removing files that are more than a week old: ',path,'/',filename)
			    os.remove(f"{path}/{filename}")
	return None

def cleanData(data, fileName):
	# The source is has multiple records that make a single record. 
    # We will use the first value in the record to map to the appropriate variables.
    source = pd.DataFrame(data)

	# the target structure we will be getting to.
    df = pd.DataFrame(columns = variables)

	# iterate over the source rows and create the target row
    record = {}
    record['date_stamp'] = fileName[0:-4]
	
    for index, row in source.iterrows():
        variable = row[0]
        value = row[1]
        if(type(variable) != str and math.isnan(variable)):
            continue
        if(math.isnan(value)):
            value = None

        if('Number of Cases' in variable):
            record['cnt_confirmed'] = value
        elif('Recovered Cases' in variable):
            record['cnt_recovered'] = value  
        elif('Number of Active Cases' in variable):  
            record['cnt_active'] = value
        elif('Hospitalizations' in variable):  
            record['cnt_hospitalized'] = value
        elif('Currently Hospitalized' in variable): 
            record['cnt_hospitalized_current'] = value 
        elif('Deaths' in variable):  
            record['cnt_death'] = value
        elif('Probable Cases' in variable): 
            record['cnt_probable'] = value 

    # add record to df
    df = df.append(record, ignore_index=True)

	# apply data types
    df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')
    df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())
    df['cnt_recovered'] = df['cnt_recovered'].astype(pd.Int32Dtype())
    df['cnt_active'] = df['cnt_active'].astype(pd.Int32Dtype())
    df['cnt_hospitalized'] = df['cnt_hospitalized'].astype(pd.Int32Dtype())
    df['cnt_hospitalized_current'] = df['cnt_hospitalized_current'].astype(pd.Int32Dtype())
    df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
    df['cnt_probable'] = df['cnt_probable'].astype(pd.Int32Dtype())

    return df

if __name__ == "__main__":
    path = os.path
    # Loop over the files within the folder
    for filename in sorted(os.listdir('./data/us-tn/co-knox/covid_cases/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/us-tn/co-knox/covid_cases/clean/{filename}') == False:
            print(filename)

            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/us-tn/co-knox/covid_cases/raw/{filename}")
            df = cleanData(data, filename)
            df.to_csv(f"./data/us-tn/co-knox/covid_cases/clean/{filename}", index=False)
        
            # if there is no aggregate file create one, otherwise append to it. 
            if path.exists(f"./data/us-tn/co-knox/covid_cases/latest.csv"):
                df.to_csv(f"./data/us-tn/co-knox/covid_cases/latest.csv", mode='a', header=False, index=False)
            else:
                df.to_csv(f"./data/us-tn/co-knox/covid_cases/latest.csv", index=False)

    deleteFiles('./data/us-tn/co-knox/covid_cases/raw')
    deleteFiles('./data/us-tn/co-knox/covid_cases/clean')
