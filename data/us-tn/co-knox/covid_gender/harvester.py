import os
import math
import pandas as pd
import datetime

variables = ['sex','cnt_confirmed','pct_confirmed']

def cleanData(data, fileName):
    # source data frame from csv file
    df = pd.DataFrame(data)
    df.columns = variables
    print(df)
	
    # the target data frame
    df['sex'] = df['sex'].map({ 'Male':'1', 'Female': '2', 'Sex Unknown': '9' })
    df['pct_confirmed'] = list(map(lambda x: x[:-1], df['pct_confirmed'].values))
    df['date_stamp'] = fileName[0:-4]   

	# apply data types
    df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')
    
    # order
    df = df[['date_stamp','sex','cnt_confirmed','pct_confirmed']]
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
    for filename in sorted(os.listdir('./data/us-tn/co-knox/covid_gender/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/us-tn/co-knox/covid_gender/clean/{filename}') == False:
            print(filename)

            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/us-tn/co-knox/covid_gender/raw/{filename}")
            df = cleanData(data, filename)
            df.to_csv(f"./data/us-tn/co-knox/covid_gender/clean/{filename}", index=False)
        
            # if there is no aggregate file create one, otherwise append to it. 
            if path.exists(f"./data/us-tn/co-knox/covid_gender/latest.csv"):
                df.to_csv(f"./data/us-tn/co-knox/covid_gender/latest.csv", mode='a', header=False, index=False)
            else:
                df.to_csv(f"./data/us-tn/co-knox/covid_gender/latest.csv", index=False)

    deleteFiles('./data/us-tn/co-knox/covid_gender/raw')
    deleteFiles('./data/us-tn/co-knox/covid_gender/clean')

