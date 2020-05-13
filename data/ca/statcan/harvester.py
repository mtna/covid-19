import os
import math
import pandas as pd

variables = [
	'case_id',
	'episode_start_date',
	'date_stamp',
	'gender',
	'age_group',
	'transmission_type',
	'is_hospitalized',
	'is_hospitalized_previous',
	'is_intensive_care',
	'is_intensive_care_previous',
	'is_deceased',
	'is_deceased_previous'
]

def cleanData(data):
	# The source is has multiple records around a single case, transposing will not work easily 
	# (at least with my limited python knowledge) so we will iterate through all the records and 
	# create a new record as needed and just construct an entirely new data frame.
	source = pd.DataFrame(data)

	# the target structure we will be getting to.
	df = pd.DataFrame(columns = variables)

	# iterate over the source rows and create the target rows, one per case id
	caseNumber = 0
	record = {}
	for index, row in source.iterrows():
		caseId = row['Case identifier number']
		caseInfo = row['Case information']
		value = row['VALUE']
		if(math.isnan(value)):
			value = None
		else:
			value = str(int(value))

		if(caseNumber != caseId):
			# if the record is not empty, add to the target data frame
			if(bool(record)):
				df = df.append(record, ignore_index=True)
			
			# create a fresh record and start bringing the information into it. 
			record = {}
			lastUpdate = row['REF_DATE']
			episodeDate = row['REF_DATE']
			caseNumber = caseId
			record['case_id'] = caseNumber

		# Build last update
		if(caseInfo == 'Date case was last updated - month'):
			lastUpdate = str(lastUpdate) + '-' + value
		if(caseInfo == 'Date case was last updated - day'):
			lastUpdate = str(lastUpdate) + '-' + value
			if(lastUpdate.find('-99') != -1):
				lastUpdate = None
			record['date_stamp'] = lastUpdate
		
		# Build episode date - some episode dates have indicating unknown.
		if(caseInfo == 'Episode date - month'):
			episodeDate = str(episodeDate) + '-' + value
		if(caseInfo == 'Episode date - day'):
			episodeDate = str(episodeDate) + '-' + value
			if(episodeDate.find('-99') != -1):
				episodeDate = None
			record['episode_start_date'] = episodeDate

		# Gender
		if(caseInfo == 'Gender'):
			# we have not encountered any code 3(non-binary) but we have seen 7 which is not listed in the statcan documentation. We will adjust this to be 3. 
			if(value == '7'):
				value = '3'
			record['gender'] = value
		
		# Age range
		if(caseInfo == 'Age group'):
			if(value == '1'):  
				value = '00'
			elif(value == '2'):  
				value = '20'
			elif(value == '3'):
				value = '30'
			elif(value == '4'):
				value = '40'
			elif(value == '5'):
				value = '50'
			elif(value == '6'):
				value = '60'
			elif(value == '7'):
				value = '70'
			elif(value == '8'):
				value = '80'
			else:
				value = '99'
			record['age_group'] = value

		# Transmission
		if(caseInfo == 'Transmission'):
			record['transmission_type'] = value

		# Hospitalization
		if(caseInfo == 'Hospitalization'):
			record['is_hospitalized'] = value
		if(caseInfo == 'Hospitalization, previous status'):
			record['is_hospitalized_previous'] = value

		# Intensive Care
		if(caseInfo == 'Intensive care unit'):
			record['is_intensive_care'] = value
		if(caseInfo == 'Intensive care unit, previous status'):
			record['is_intensive_care_previous'] = value

		# Death
		if(caseInfo == 'Death'):
			record['is_deceased'] = value
		if(caseInfo == 'Death, previous status'):
			record['is_deceased_previous'] = value

	# reformat dates
	df['episode_start_date'] = pd.to_datetime(df['episode_start_date']).dt.strftime('%Y-%m-%d')
	df['date_stamp'] = pd.to_datetime(df['date_stamp']).dt.strftime('%Y-%m-%d')

	print(df)
	return df

if __name__ == "__main__":
	path = os.path
	# Loop over the files within state folder
	for filename in os.listdir('./data/ca/statcan/raw'):
		csvFile = filename.replace('.zip','.csv')
		if filename.endswith('.zip') and path.exists(f'./data/ca/statcan/clean/{csvFile}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/ca/statcan/raw/{filename}")
			df = cleanData(data)
			df.to_csv(f"./data/ca/statcan/clean/{csvFile}", index=False)