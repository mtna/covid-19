import os
import pandas as pd
import math
import datetime

variables = {
	'pruid': 'ca_provterr',
	'prname': 'province_name',
	'prnameFR': 'province_name_fr',
	'date': 'date_stamp',
	'numconf': 'cnt_confirmed',
	'numprob': 'cnt_probable',
	'numdeaths': 'cnt_death',
	'numtotal': 'cnt_total',
	'numtested': 'cnt_tested',
	'numrecover': 'cnt_recovered',
	'percentrecover': 'pct_recovered',
	'ratetested': 'rate_tested',
	'numtoday': 'cnt_total_new',
	'percentoday': 'pct_total_new'
	
}

def convertDateTimes(df):
	dates = df.filter(like='date')
	for (label, content) in dates.iteritems():
		df[label] = pd.to_datetime(content, format="%d-%m-%Y").dt.strftime('%Y-%m-%d')

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

def cleanData(data):
	df = pd.DataFrame(data)

	# Rename the file headers
	df.rename(variables, axis="columns", inplace=True)

	# Remove all the rows that have the aggregate values for Canada as a whole
	df = df[df.ca_provterr != 1]
	
	# Duplicate province to non standard field where 99 can be persisted
	df['ca_covid19_geo'] = df['ca_provterr']

	# Remove 99 from the standard provinces where == 99
	df['ca_provterr'] = df['ca_provterr'].replace({99 : None})

	# drop the "update" column before converting the dates bc df.filter(like"date") will pick this up and throw an error
	df = df.drop(columns=['update'])
	# convert all date columns into proper format
	df = convertDateTimes(df)

	# fill out missing values with 0
	df['cnt_confirmed'] = df['cnt_confirmed'].fillna(0)
	df['cnt_probable'] = df['cnt_probable'].fillna(0)
	df['cnt_death'] = df['cnt_death'].fillna(0)
	df['cnt_total'] = df['cnt_total'].fillna(0)
	df['cnt_tested'] = df['cnt_tested'].fillna(0)
	df['cnt_recovered'] = df['cnt_recovered'].fillna(0)
	df['cnt_total_new'] = df['cnt_total_new'].fillna(0)

	# ensure the counts are all integers (not decimals)
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(int)
	df['cnt_probable'] = df['cnt_probable'].astype(int)
	df['cnt_death'] = df['cnt_death'].astype(int)
	df['cnt_total'] = df['cnt_total'].astype(int)
	df['cnt_tested'] = df['cnt_tested'].astype(int)
	df['cnt_recovered'] = df['cnt_recovered'].astype(int)
	df['cnt_total_new'] = df['cnt_total_new'].astype(int)
	
	#cast to float
	df['pct_total_new'] = df['pct_total_new'].astype(float)
	#round the pct vars up to three decimal places to comply with db limitations
	df["pct_total_new"]=df["pct_total_new"].round(decimals=3)
	# reorder and drop columns
	df = df[['date_stamp','ca_provterr','ca_covid19_geo','cnt_confirmed','cnt_probable','cnt_death','cnt_total','cnt_total_new','pct_total_new','cnt_tested','cnt_recovered','pct_recovered']]
	
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
	# Loop over the files within state folder
	for filename in os.listdir('./data/ca/gov/cases/raw'):
		if filename.endswith('.csv') and path.exists(f'./data/ca/gov/cases/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/ca/gov/cases/raw/{filename}", float_precision='round_trip')
			df = cleanData(data)
			df.to_csv(f"./data/ca/gov/cases/clean/{filename}", index=False)
			#also add to the latest.csv
			if path.exists(f'./data/ca/gov/cases/latest.csv'):
				#clear out the file's existing data and write to it
				#this is a copy of the data in the clean folder, so that the db loading script can look for an unchanging file name.
				open('./data/ca/gov/cases/latest.csv', 'w').close()
				df.to_csv(f"./data/ca/gov/cases/latest.csv", index=False)
	
	deleteFiles('./data/ca/gov/cases/raw')
	deleteFiles('./data/ca/gov/cases/clean')
