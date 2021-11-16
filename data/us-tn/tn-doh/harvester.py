import addfips
import os
import pandas as pd
import datetime

ageVariables = {
	'DATE': 'date_stamp',
	'AGE_RANGE': 'age_group',
	'AR_TOTALCASES': 'cnt_confirmed',
	'AR_TOTALPERCENT': 'pct_confirmed',
	'AR_NEWCASES': 'cnt_confirmed_new',
	'AR_NEWPERCENT': 'pct_confirmed_new',
	'AR_TOTALDEATHS' : 'cnt_death',
	'AR_NEWDEATHS': 'cnt_death_new'
}

countyVariables = {
	'DATE': 'date_stamp',
	'COUNTY': 'us_county_fips',
	'TOTAL_CASES': 'cnt_total',
	'NEW_CASES': 'cnt_total_new',
	'TOTAL_CONFIRMED': 'cnt_confirmed',
	'NEW_CONFIRMED': 'cnt_confirmed_new',
	'TOTAL_PROBABLE': 'cnt_probable',
	'NEW_PROBABLE': 'cnt_probable_new',
	'POS_TESTS': 'cnt_tested_pos',
	'NEG_TESTS': 'cnt_tested_neg',
	'TOTAL_TESTS': 'cnt_tested',
	'NEW_TESTS': 'cnt_tested_new',
	'NEW_DEATHS': 'cnt_death_new',
	'TOTAL_DEATHS': 'cnt_death',
	'NEW_RECOVERED': 'cnt_recovered_new',
	'TOTAL_RECOVERED': 'cnt_recovered',
	'NEW_ACTIVE': 'cnt_active_new',
	'TOTAL_ACTIVE': 'cnt_active',
	'NEW_HOSPITALIZED': 'cnt_hospitalized_new',
	'TOTAL_HOSPITALIZED': 'cnt_hospitalized',
}

dailyVariables = {
	'DATE': 'date_stamp',
	'TOTAL_CASES': 'cnt_total',
	'NEW_CASES': 'cnt_total_new',
	'TOTAL_CONFIRMED': 'cnt_confirmed',
	'NEW_CONFIRMED': 'cnt_confirmed_new',
	'TOTAL_PROBABLE': 'cnt_probable',
	'NEW_PROBABLE': 'cnt_probable_new',
	'POS_TESTS': 'cnt_tested_pos',
	'NEG_TESTS': 'cnt_tested_neg',
	'TOTAL_TESTS': 'cnt_tested',
	'NEW_TESTS': 'cnt_tested_new',
	'NEW_DEATHS': 'cnt_death_new',
	'TOTAL_DEATHS': 'cnt_death',
	'NEW_RECOVERED': 'cnt_recovered_new',
	'TOTAL_RECOVERED': 'cnt_recovered',
	'NEW_ACTIVE': 'cnt_active_new',
	'TOTAL_ACTIVE': 'cnt_active',
	'NEW_HOSP': 'cnt_hospitalized_new',
	'TOTAL_HOSP': 'cnt_hospitalized',
}

raceEthSexVariables = {
	'Date': 'date_stamp',
	'Category': 'category_type',
	'Cat_Detail': 'category_name',
	'CAT_DETAIL': 'category_name',
	'Cat_CaseCount': 'cnt_confirmed',
	'Cat_Percent': 'pct_confirmed',
	'CAT_DEATHCOUNT' : 'cnt_death',
	'CAT_DEATHPERCENT': 'pct_death'
}

def cleanAgeData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df.rename(ageVariables, axis="columns", inplace=True)

	# Reformat dates
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m-%d-%y')

	# Code age ranges
	df['age_group'] = df['age_group'].map({ '0-10 years':'00', '11-20 years': '11', '21-30 years': '21', '31-40 years': '31', '41-50 years': '41', '51-60 years': '51', '61-70 years': '61', '71-80 years': '71', '81+ years': '81', 'Pending': '99' })

	# multiply the percentages by 100
	df['pct_confirmed'] = df['pct_confirmed'].apply(lambda x: round(x*100,4))
	df['pct_confirmed_new'] = df['pct_confirmed_new'].apply(lambda x: round(x*100, 4))
	
	#cast count variables to integers
	df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
	df['cnt_death_new'] = df['cnt_death_new'].astype(pd.Int32Dtype())
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())

	# reorder so that the cnt and new  are always next to each other in the same order
	df = df[['date_stamp', 'age_group', 'cnt_confirmed', 'cnt_confirmed_new', 'pct_confirmed', 'pct_confirmed_new', 'cnt_death', 'cnt_death_new']]

	# order the records by date
	df = df.sort_values(by=['date_stamp','age_group'], ascending=True)

	return df

def cleanCountyData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df.rename(countyVariables, axis="columns", inplace=True)

	# Reformat dates
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m-%d-%y')
	
	# Copy original county value to keep the pending and out of state values
	df['tn_covid_geo'] = df['us_county_fips']

	# Change county name to fips code
	af = addfips.AddFIPS()	
	fips = []
	for key, value in df['us_county_fips'].items():
		fips.append(af.get_county_fips(value, 'Tennessee'))
	df['us_county_fips'] = fips

	# Copy appropriate fips codes to covid geo
	df.loc[(df['tn_covid_geo'] != 'Pending') & (df['tn_covid_geo'] != 'Out of State'), 'tn_covid_geo'] = df['us_county_fips']
	df.loc[df['tn_covid_geo'] == 'Pending', 'tn_covid_geo'] = '47PEN'
	df.loc[df['tn_covid_geo'] == 'Out of State', 'tn_covid_geo'] = '47OOS'
	
	# format as Integers a none 
	df['cnt_total'] = df['cnt_total'].astype(pd.Int32Dtype())
	df['cnt_total_new'] = df['cnt_total_new'].astype(pd.Int32Dtype())
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())
	df['cnt_confirmed_new'] = df['cnt_confirmed_new'].astype(pd.Int32Dtype())
	if 'cnt_probable' in df.columns:
		df['cnt_probable'] = df['cnt_probable'].astype(pd.Int32Dtype())
		df['cnt_probable_new'] = df['cnt_probable_new'].astype(pd.Int32Dtype())
	df['cnt_tested_pos'] = df['cnt_tested_pos'].astype(pd.Int32Dtype())
	df['cnt_tested_neg'] = df['cnt_tested_neg'].astype(pd.Int32Dtype())
	df['cnt_tested'] = df['cnt_tested'].astype(pd.Int32Dtype())
	df['cnt_tested_new'] = df['cnt_tested_new'].astype(pd.Int32Dtype())
	df['cnt_death_new'] = df['cnt_death_new'].astype(pd.Int32Dtype())
	df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
	df['cnt_recovered_new'] = df['cnt_recovered_new'].astype(pd.Int32Dtype())
	df['cnt_recovered'] = df['cnt_recovered'].astype(pd.Int32Dtype())
	df['cnt_active_new'] = df['cnt_active_new'].astype(pd.Int32Dtype())
	df['cnt_active'] = df['cnt_active'].astype(pd.Int32Dtype())
	df['cnt_hospitalized_new'] = df['cnt_hospitalized_new'].astype(pd.Int32Dtype())
	df['cnt_hospitalized'] = df['cnt_hospitalized'].astype(pd.Int32Dtype())

	# reorder so that the total and new are always next to each other in the same order
	if 'cnt_probable' in df.columns:
		df = df[['date_stamp', 'us_county_fips', 'tn_covid_geo', 'cnt_total', 'cnt_total_new', 'cnt_confirmed', 'cnt_confirmed_new', 'cnt_probable', 'cnt_probable_new', 'cnt_active', 'cnt_active_new', 'cnt_hospitalized', 'cnt_hospitalized_new', 'cnt_recovered', 'cnt_recovered_new', 'cnt_death', 'cnt_death_new', 'cnt_tested_pos', 'cnt_tested_neg', 'cnt_tested', 'cnt_tested_new']]
	else:
		df = df[['date_stamp', 'us_county_fips', 'tn_covid_geo', 'cnt_total', 'cnt_total_new', 'cnt_confirmed', 'cnt_confirmed_new', 'cnt_active', 'cnt_active_new', 'cnt_hospitalized', 'cnt_hospitalized_new', 'cnt_recovered', 'cnt_recovered_new', 'cnt_death', 'cnt_death_new', 'cnt_tested_pos', 'cnt_tested_neg', 'cnt_tested', 'cnt_tested_new']]

	# order the records by date
	df = df.sort_values(by='date_stamp', ascending=True)
	return df

def cleanDailyData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df.rename(dailyVariables, axis="columns", inplace=True)

	# Reformat dates
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m-%d-%y')

	# format as Integers a none 
	df['cnt_total'] = df['cnt_total'].astype(pd.Int32Dtype())
	df['cnt_total_new'] = df['cnt_total_new'].astype(pd.Int32Dtype())
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())
	df['cnt_confirmed_new'] = df['cnt_confirmed_new'].astype(pd.Int32Dtype())
	if 'cnt_probable' in df.columns:
		df['cnt_probable'] = df['cnt_probable'].astype(pd.Int32Dtype())
		df['cnt_probable_new'] = df['cnt_probable_new'].astype(pd.Int32Dtype())
	df['cnt_tested_pos'] = df['cnt_tested_pos'].astype(pd.Int32Dtype())
	df['cnt_tested_neg'] = df['cnt_tested_neg'].astype(pd.Int32Dtype())
	df['cnt_tested'] = df['cnt_tested'].astype(pd.Int32Dtype())
	df['cnt_tested_new'] = df['cnt_tested_new'].astype(pd.Int32Dtype())
	df['cnt_death_new'] = df['cnt_death_new'].astype(pd.Int32Dtype())
	df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
	df['cnt_recovered_new'] = df['cnt_recovered_new'].astype(pd.Int32Dtype())
	df['cnt_recovered'] = df['cnt_recovered'].astype(pd.Int32Dtype())
	df['cnt_active_new'] = df['cnt_active_new'].astype(pd.Int32Dtype())
	df['cnt_active'] = df['cnt_active'].astype(pd.Int32Dtype())
	df['cnt_hospitalized_new'] = df['cnt_hospitalized_new'].astype(pd.Int32Dtype())
	df['cnt_hospitalized'] = df['cnt_hospitalized'].astype(pd.Int32Dtype())

	# reorder so that the total and new are always next to each other in the same order
	if 'cnt_probable' in df.columns:
		df = df[['date_stamp', 'cnt_total', 'cnt_total_new', 'cnt_confirmed', 'cnt_confirmed_new', 'cnt_probable', 'cnt_probable_new', 'cnt_active', 'cnt_active_new', 'cnt_hospitalized', 'cnt_hospitalized_new', 'cnt_recovered', 'cnt_recovered_new', 'cnt_death', 'cnt_death_new', 'cnt_tested_pos', 'cnt_tested_neg', 'cnt_tested', 'cnt_tested_new']]
	else:
		df = df[['date_stamp', 'cnt_total', 'cnt_total_new', 'cnt_confirmed', 'cnt_confirmed_new', 'cnt_active', 'cnt_active_new', 'cnt_hospitalized', 'cnt_hospitalized_new', 'cnt_recovered', 'cnt_recovered_new', 'cnt_death', 'cnt_death_new', 'cnt_tested_pos', 'cnt_tested_neg', 'cnt_tested', 'cnt_tested_new']]

	# order the records by date
	df = df.sort_values(by='date_stamp', ascending=True)
	return df
	
def cleanRaceEthSexData(data):
	df = pd.DataFrame(data)
	
	# Rename the file headers
	df.rename(raceEthSexVariables, axis="columns", inplace=True)

	# Reformat dates
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%m-%d-%y')

	# Code the category details. These will be split out eventually but we may 
	# also want to build a wide file, because of this we will add the coded 
	# variable alongside the original
	df['category_code'] = df['category_name'].map({ 'Pending':'9', 'Hispanic':'1', 'Not Hispanic or Latino': '0', 'Asian': '0', 'Black or African American': '1', 'White': '2', 'Other/Multiracial': '3', 'American Indian or Alaska Native': '4', 'Native Hawaiian or Other Pacific Islander':'5', 'Male': '1', 'Female': '2' })

	# multiply the percentages by 100
	df['pct_confirmed'] = df['pct_confirmed'].apply(lambda x: round(x*100,4))
	df['pct_death'] = df['pct_death'].apply(lambda x: round(x*100, 4))
	
	#cast count variables to integers
	df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
	df['cnt_confirmed'] = df['cnt_confirmed'].astype(pd.Int32Dtype())

	# order the records by date
	df = df.sort_values(by='date_stamp', ascending=True)

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
			    print('removing raw files that are more than a week old: ',path,filename)
			    os.remove(f"{path}/{filename}")
	return None

if __name__ == "__main__":
	path = os.path
	# Loop over the files within the age folder
	for filename in sorted(os.listdir('./data/us-tn/tn-doh/age/raw')):
		if filename.endswith('.csv') and path.exists(f'./data/us-tn/tn-doh/age/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-tn/tn-doh/age/raw/{filename}", float_precision='round_trip')
			df = cleanAgeData(data)
			df.to_csv(f"./data/us-tn/tn-doh/age/clean/{filename}", index=False)
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_age.csv'):
				open('./data/us-tn/tn-doh/latest_age.csv', 'w').close()
				df.to_csv(f"./data/us-tn/tn-doh/latest_age.csv", index=False)

	
	# Loop over the files within the county folder
	for filename in sorted(os.listdir('./data/us-tn/tn-doh/county_new/raw')):
		if filename.endswith('.csv') and path.exists(f'./data/us-tn/tn-doh/county_new/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-tn/tn-doh/county_new/raw/{filename}", float_precision='round_trip')
			df = cleanCountyData(data)
			df.to_csv(f"./data/us-tn/tn-doh/county_new/clean/{filename}", index=False)# Loop over the files within the county folder
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_county.csv'):
				open('./data/us-tn/tn-doh/latest_county.csv', 'w').close()
				df.to_csv(f"./data/us-tn/tn-doh/latest_county.csv", index=False)
				
	# Loop over the files within the daily folder
	for filename in sorted(os.listdir('./data/us-tn/tn-doh/daily_case_info/raw')):
		if filename.endswith('.csv') and path.exists(f'./data/us-tn/tn-doh/daily_case_info/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-tn/tn-doh/daily_case_info/raw/{filename}", float_precision='round_trip')
			df = cleanDailyData(data)
			df.to_csv(f"./data/us-tn/tn-doh/daily_case_info/clean/{filename}", index=False)
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_state.csv'):
				open('./data/us-tn/tn-doh/latest_state.csv', 'w').close()
				df.to_csv(f"./data/us-tn/tn-doh/latest_state.csv", index=False)

	# Loop over the demographic files
	for filename in sorted(os.listdir('./data/us-tn/tn-doh/race_eth_sex/raw')):
		if filename.endswith('.csv') and path.exists(f'./data/us-tn/tn-doh/race_eth_sex/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-tn/tn-doh/race_eth_sex/raw/{filename}", float_precision='round_trip')
			df = cleanRaceEthSexData(data)

			# Split into the three files and save

			# Race
			race = df.loc[df.category_type == 'RACE'][['date_stamp', 'category_code', 'cnt_confirmed', 'pct_confirmed', 'cnt_death', 'pct_death' ]]
			race.rename(columns = {'category_code' : 'race'}, inplace = True)
			race.to_csv(f"./data/us-tn/tn-doh/race_eth_sex/clean_race/{filename}", index=False)
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_race.csv'):
				open('./data/us-tn/tn-doh/latest_race.csv', 'w').close()
				race.to_csv(f"./data/us-tn/tn-doh/latest_race.csv", index=False)

			# Ethnicity
			ethnicity = df.loc[df.category_type == 'ETHNICITY'][['date_stamp', 'category_code', 'cnt_confirmed', 'pct_confirmed', 'cnt_death', 'pct_death' ]]
			ethnicity.rename(columns = {'category_code' : 'ethnicity'}, inplace = True)
			ethnicity.to_csv(f"./data/us-tn/tn-doh/race_eth_sex/clean_eth/{filename}", index=False)
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_eth.csv'):
				open('./data/us-tn/tn-doh/latest_eth.csv', 'w').close()
				ethnicity.to_csv(f"./data/us-tn/tn-doh/latest_eth.csv", index=False)
			
			# Sex
			sex = df.loc[df.category_type == 'SEX'][['date_stamp', 'category_code', 'cnt_confirmed', 'pct_confirmed', 'cnt_death', 'pct_death' ]]
			sex.rename(columns = {'category_code' : 'sex'}, inplace = True)
			sex.to_csv(f"./data/us-tn/tn-doh/race_eth_sex/clean_sex/{filename}", index=False)
			#write to the latest file (clear and rewrite)
			if path.exists(f'./data/us-tn/tn-doh/latest_sex.csv'):
				open('./data/us-tn/tn-doh/latest_sex.csv', 'w').close()
				sex.to_csv(f"./data/us-tn/tn-doh/latest_sex.csv", index=False)

	#delete old files
	deleteFiles('./data/us-tn/tn-doh/daily_case_info/raw')
	deleteFiles('./data/us-tn/tn-doh/daily_case_info/clean')
	deleteFiles('./data/us-tn/tn-doh/age/clean')
	deleteFiles('./data/us-tn/tn-doh/age/raw')
	deleteFiles('./data/us-tn/tn-doh/county_new/clean')
	deleteFiles('./data/us-tn/tn-doh/county_new/raw')
	deleteFiles('./data/us-tn/tn-doh/race_eth_sex/clean_eth')
	deleteFiles('./data/us-tn/tn-doh/race_eth_sex/clean_sex')
	deleteFiles('./data/us-tn/tn-doh/race_eth_sex/clean_race')
	deleteFiles('./data/us-tn/tn-doh/race_eth_sex/raw')

