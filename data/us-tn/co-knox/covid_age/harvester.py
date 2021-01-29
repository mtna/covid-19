import os
import math
import pandas as pd
import datetime

variables = [
	'date_stamp',
    'age_group',
	'cnt_confirmed',
	'pct_confirmed'
]

def cleanData(data, fileName):
    # source data frame from csv file
    source = pd.DataFrame(data)
    source.columns = ['v1','v2','v3']
    print(source)
	
    # the target data frame
    df = pd.DataFrame(columns = variables)
    df['age_group'] = source['v1'].map({ '0-10':'00', '11-20': '11', '21-30': '21', '31-40': '31', '41-50': '41', '51-60': '51', '61-70': '61', '71-80': '71', '81-90': '81', '90+': '91', 'Age Unknown': '99' })
    df['cnt_confirmed'] = source['v2']
    df['pct_confirmed'] = list(map(lambda x: x[:-1], source['v3'].values))
    df['date_stamp'] = fileName[0:-4]

	# apply data types
    df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')
    df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())

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
			    print('removing files that are more than a week old: ',path,'/',filename)
			    os.remove(f"{path}/{filename}")
	return None

if __name__ == "__main__":
    path = os.path
    # Loop over the files within the folder
    for filename in sorted(os.listdir('./data/us-tn/co-knox/covid_age/raw')):
        if filename.endswith('.csv') and path.exists(f"./data/us-tn/co-knox/covid_age/clean/{filename}") == False:
            print(filename)

            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/us-tn/co-knox/covid_age/raw/{filename}")
            df = cleanData(data, filename)
            df.to_csv(f"./data/us-tn/co-knox/covid_age/clean/{filename}", index=False)
        
            # if there is no aggregate file create one, otherwise append to it. 
            if path.exists(f"./data/us-tn/co-knox/covid_age/latest.csv"):
                df.to_csv(f"./data/us-tn/co-knox/covid_age/latest.csv", mode='a', header=False, index=False)
            else:
                df.to_csv(f"./data/us-tn/co-knox/covid_age/latest.csv", index=False)
    deleteFiles('./data/us-tn/co-knox/covid_age/raw')
    deleteFiles('./data/us-tn/co-knox/covid_age/clean')
