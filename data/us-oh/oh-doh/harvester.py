import datetime
import os
import pandas as pd
import addfips

variables = {
	'Sex': 'sex',
	'Onset Date': 'date_stamp',
	'Date Of Death': 'date_stamp_death',
	'Case Count': 'cnt_confirmed',
	'Death Due to Illness Count': 'cnt_death',
	'Hospitalized Count': 'cnt_hospitalized',
	'Age Range': 'age_group'
}

def cleanData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df = df.rename(variables, axis="columns")
	
	# Remove the footer
	df = df[df['County'] != 'Grand Total']

	# Remove unknown dates (if its unknown why isnt it just empty)
	df['date_stamp'] = df['date_stamp'].replace({'Unknown': None})
	df['date_stamp_death'] = df['date_stamp_death'].replace({'Unknown': None})

	# Convert the date formats
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m/%d/%Y')
	df['date_stamp_death'] = pd.to_datetime(df['date_stamp_death'], format='%m/%d/%Y')

	# Add the county fips code
	af = addfips.AddFIPS()
	fips = []
	for key, value in df['County'].items():
		fips.append(af.get_county_fips(value, 'Ohio'))
	df['us_county_fips'] = fips

	# Convert the sex string values to numeric
	df['sex'] = df['sex'].map({ 'Male': '1', 'Female': '2', 'Unknown':'9' })

	# Code age range
	df['age_group'] = df['age_group'].map({ '0-19': '00', '20-29': '20', '30-39': '30', '40-49': '40', '50-59': '50', '60-69': '60', '70-79': '70', '80+': '80', 'Unknown': '99'  })

	# drop columns that are not needed
	df = df.drop(['County'], axis=1)

	#reorder the columns
	df = df[['date_stamp','us_county_fips','sex','age_group','cnt_confirmed','cnt_death','cnt_hospitalized', 'date_stamp_death']]

	# order the records by date
	df = df.sort_values(by='date_stamp', ascending=True)

	return df

def transformData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df = df.rename(variables, axis="columns")
	
	# Remove the footer
	df = df[df['County'] != 'Grand Total']

	# Remove unknown dates (if its unknown why isnt it just empty)
	df['date_stamp'] = df['date_stamp'].replace({'Unknown': None})
	df['date_stamp_death'] = df['date_stamp_death'].replace({'Unknown': None})

	# Convert the date formats
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m/%d/%Y')
	df['date_stamp_death'] = pd.to_datetime(df['date_stamp_death'], format='%m/%d/%Y')

	# Add the county fips code
	af = addfips.AddFIPS()
	fips = []
	for key, value in df['County'].items():
		fips.append(af.get_county_fips(value, 'Ohio'))
	df['us_county_fips'] = fips

	# drop columns that are not needed
	df = df.drop(['County','sex','age_group','date_stamp_death'], axis=1)

	# order the records by date
	df = df.sort_values(by='date_stamp', ascending=True)

	#reorder the columns
	df = df[['date_stamp','us_county_fips','cnt_confirmed','cnt_hospitalized','cnt_death']]

	# ensure they are all numeric columns
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(int)
	df['cnt_death'] = df['cnt_death'].astype(int)
	df['cnt_hospitalized'] = df['cnt_hospitalized'].astype(int)

	# we will sum by date and county, and then run a cumulative sum over the county.
	df = df.groupby(['date_stamp','us_county_fips']).sum().groupby(['us_county_fips']).cumsum().reset_index()

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
	for filename in os.listdir('./data/us-oh/oh-doh/raw'):
		
		if filename.endswith('.csv') and path.exists(f'./data/us-oh/oh-doh/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-oh/oh-doh/raw/{filename}")
			df = cleanData(data)
			df.to_csv(f"./data/us-oh/oh-doh/clean/{filename}", index=False)
			if path.exists(f'./data/us-oh/oh-doh/latest_clean.csv'):
				#clear out the file's existing data and write to it
				open('./data/us-oh/oh-doh/latest_clean.csv', 'w').close()
				df.to_csv(f"./data/us-oh/oh-doh/latest_clean.csv", index=False)
		if filename.endswith('.csv') and path.exists(f'./data/us-oh/oh-doh/transformed/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-oh/oh-doh/raw/{filename}")
			df = transformData(data)
			df.to_csv(f"./data/us-oh/oh-doh/transformed/{filename}", index=False)
			if path.exists(f'./data/us-oh/oh-doh/latest_agg.csv'):
				#clear out the file's existing data and write to it
				open('./data/us-oh/oh-doh/latest_agg.csv', 'w').close()
				df.to_csv(f"./data/us-oh/oh-doh/latest_agg.csv", index=False)

	#delete old files
	deleteFiles('./data/us-oh/oh-doh/raw')
	deleteFiles('./data/us-oh/oh-doh/clean')
	deleteFiles('./data/us-oh/oh-doh/transformed')
