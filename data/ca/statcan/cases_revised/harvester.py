import os
import math
import pandas as pd
import numpy as np
import datetime

variables = {
	'Case identifier number':'case_id',
	'Age group': 'age_group',
	'Asymptomatic': 'asymptomatic',
	'Death': 'is_deceased',
	'Episode week': 'episode_week',
	'Episode week group': 'episode_week_group',
	'Episode year': 'episode_year',
	'Gender': 'gender',
	'Hospital status': 'is_hospitalized',
	'Occupation': 'occupation',
	'Onset week of symptoms': 'onset_week',
	'Onset year of symptoms': 'onset_year',
	'Recovered': 'is_recovered',
	'Recovery week': 'recovery_week',
	'Recovery year': 'recovery_year',
	'Region': 'region',
	'Symptom, chills': 'symptom_chills',
	'Symptom, cough': 'symptom_cough',
	'Symptom, diarrhea': 'symptom_diarrhea',
	'Symptom, fever': 'symptom_fever',
	'Symptom, headache':'symptom_headache',
	'Symptom, irritability':'symptom_irritability',
	'Symptom, nausea':'symptom_nausea',
	'Symptom, other':'symptom_other',
	'Symptom, pain':'symptom_pain',
	'Symptom, runny nose':'symptom_runny_nose',
	'Symptom, shortness of breath':'symptom_short_breath',
	'Symptom, sore throat':'symptom_sore_throat',
	'Symptom, weakness':'symptom_weakness',
	'Transmission':'transmission'
}

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
		if(filename.endswith('.zip')):
			newFilename = filename.replace('.zip', '');
			filedate = datetime.datetime.strptime(newFilename, '%Y-%m-%d')
			if(filedate < week_ago):
			    print('removing files that are more than a week old: ',path,'/',filename)
			    os.remove(f"{path}/{filename}")
	return None

def cleanData(df):
	
	# Rename the file headers
	df.rename(variables, axis="columns", inplace=True)
	
	#at some point there started to be a trailing .0 - we will slice this off and recode. keeping as string to preserve the double zero.
	df['age_group'] = df['age_group'].astype(str).str.slice(0, 1)
	#recode age groups: statcan's current groupings are 1=0-19, 2=20-29, 3=30-39, 4=40-49, 5=50-59, 6=60-69, 7=70-79, 8=80+, 99=Not stated
	df['age_group'] = df['age_group'].astype(str).apply(str).replace({ '1':'00', '2': '20', '3': '30', '4': '40', '5': '50', '6': '60', '7': '70', '8': '80', '99': '99', '9':'99' })

	df['asymptomatic'] = df['asymptomatic'].astype(int)
	df['is_deceased'] = df['is_deceased'].astype(int)
	df['is_hospitalized'] = df['is_hospitalized'].astype(int)
	df['occupation'] = df['occupation'].astype(int)
	df['is_recovered'] = df['is_recovered'].astype(int)
	df['region'] = df['region'].astype(int)
	df['symptom_chills'] = df['symptom_chills'].astype(int)
	df['symptom_cough'] = df['symptom_cough'].astype(int)
	df['symptom_diarrhea'] = df['symptom_diarrhea'].astype(int)
	df['symptom_fever'] = df['symptom_fever'].astype(int)
	df['symptom_headache'] = df['symptom_headache'].astype(int)
	df['symptom_irritability'] = df['symptom_irritability'].astype(int)
	df['symptom_nausea'] = df['symptom_nausea'].astype(int)
	df['symptom_other'] = df['symptom_other'].astype(int)
	df['symptom_pain'] = df['symptom_pain'].astype(int)
	df['symptom_runny_nose'] = df['symptom_runny_nose'].astype(int)
	df['symptom_short_breath'] = df['symptom_short_breath'].astype(int)
	df['symptom_sore_throat'] = df['symptom_sore_throat'].astype(int)
	df['symptom_weakness'] = df['symptom_weakness'].astype(int)
	df['transmission'] = df['transmission'].astype(int)

	
	#recode sex variable. we have not encountered any code 3(non-binary) but we have seen 7 which is not listed in the statcan documentation. We will adjust this to be 3. 
	df['gender'] = df['gender'].apply(str).replace({'7':'3'}).str.slice(0, 2)

	#create a weekstamp var for dates in the format of YYYY-WXX (ex: 2020-W04)
	df['recovered_weekstamp'] = df['recovery_year'].astype(str) + "-W"+df['recovery_week'].astype(str)
	df['onset_weekstamp'] = df['onset_year'].astype(str) + "-W"+df['onset_week'].astype(str)
	df['episode_weekstamp'] = df['episode_year'].astype(str) + "-W"+df['episode_week'].astype(str)
	#mark as null if either the year or week value contains 99
	df.loc[df.recovered_weekstamp.astype(str).str.contains('99'), 'recovered_weekstamp'] = np.nan
	df.loc[df.onset_weekstamp.astype(str).str.contains('99'), 'onset_weekstamp'] = np.nan
	df.loc[df.episode_weekstamp.astype(str).str.contains('99'), 'episode_weekstamp'] = np.nan

	#drop columns
	df = df.drop(['recovery_year','recovery_week','onset_week','onset_year','episode_week','episode_year', 'episode_week_group'], axis=1)
	#sort values by case id
	df = df.sort_values(by='case_id', ascending=True)
	
	return df


if __name__ == "__main__":
	path = os.path
	# Loop over the files within state folder
	for filename in sorted(os.listdir('./data/ca/statcan/cases_revised/raw')):
		#print(filename)
		csvFile = filename.replace('.zip','.csv')
		if filename.endswith('.zip') and path.exists(f'./data/ca/statcan/cases_revised/clean/{csvFile}') == False:
			print("creating clean file for "+filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/ca/statcan/cases_revised/raw/{filename}", dtype={"Age group":"string"})
			df = pd.DataFrame(data)
			#pivot the table to use case id as index and the case information values as column headers. reset_index keeps the index as a column instead of dropping.
			df = df.pivot_table(index='Case identifier number', columns='Case information', values='VALUE').reset_index()
			
			df = cleanData(df)
			df.to_csv(f"./data/ca/statcan/cases_revised/clean/{csvFile}", index=False)
			if path.exists(f'./data/ca/statcan/cases_revised/latest.csv'):
				#clear out the file's existing data and write to it
				#this is a copy of the data in the clean folder, so that the db loading script can look for an unchanging file name.
				open('./data/ca/statcan/cases_revised/latest.csv', 'w').close()
				df.to_csv(f"./data/ca/statcan/cases_revised/latest.csv", index=False)
	deleteFiles('./data/ca/statcan/cases_revised/raw')
	deleteFiles('./data/ca/statcan/cases_revised/clean')