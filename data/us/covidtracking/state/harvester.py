import addfips
import os
import pandas as pd

variables = {
	'hash': 'hash',
	'date': 'date_stamp',
	'dateChecked': 'datetime_checked',
	'state': 'us_state_postal',
	'fips': 'us_state_fips',
	'positive': 'cnt_tested_pos',
	'positiveIncrease': 'cnt_tested_pos_new',
	'negative': 'cnt_tested_neg',
	'negativeIncrease': 'cnt_tested_neg_new',
	'pending': 'cnt_tested_pending',
	'recovered': 'cnt_recovered',
	'death': 'cnt_death',
	'deathIncrease': 'cnt_death_new',
	'hospitalized': 'cnt_hospitalized',
	'hospitalizedIncrease': 'cnt_hospitalized_new',
	'hospitalizedCurrently': 'cnt_hospitalized_current',
	'hospitalizedCumulative': 'cnt_hospitalized_total',
	'inIcuCurrently': 'cnt_icu_current',
	'inIcuCumulative': 'cnt_icu_total',
	'onVentilatorCurrently': 'cnt_vent_current',
	'onVentilatorCumulative': 'cnt_vent_total',
	'totalTestResults': 'cnt_tested',
	'totalTestResultsIncrease': 'cnt_tested_new'
}

def convertDateTimes(df):
	dates = df.filter(like='date')
	for (label, content) in dates.iteritems():
		df[label] = pd.to_datetime(content).dt.strftime('%Y-%m-%d')
		# have found some dates to be 1900-01-01 for death / recovery / hospitalization, we will clean these up
		df[label].replace({ '1900-01-01': None},inplace =True)

	return df

def convertStateFIPS(name):
	af = addfips.AddFIPS()
	codes = []
	for index, value in name.items():
		codes.append(af.get_state_fips(value))

	return pd.Series(codes)

def cleanData(data):
	df = pd.DataFrame(data)

	# Rename the file headers
	df.rename(variables, axis="columns", inplace=True)

	# Reformat date as ISO 8601 date
	df['date_stamp'] = pd.to_datetime(df['date_stamp'], format='%Y%m%d').dt.strftime('%Y-%m-%d')

	# Reformat datetime to SQL timestamp
	df['datetime_checked'] = pd.to_datetime(df['datetime_checked']).dt.strftime('%Y-%m-%d %H:%M:%S')
	
	# get the 0 padded fips codes
	df['us_state_fips'] = convertStateFIPS(df['us_state_postal'])

	# convert to integers as these will never be decimals and should be integers in the database
	df['cnt_tested_pos'] = df['cnt_tested_pos'].astype(pd.Int32Dtype())
	df['cnt_tested_pos_new'] = df['cnt_tested_pos_new'].astype(pd.Int32Dtype())
	df['cnt_tested_neg'] = df['cnt_tested_neg'].astype(pd.Int32Dtype())
	df['cnt_tested_neg_new'] = df['cnt_tested_neg_new'].astype(pd.Int32Dtype())
	df['cnt_tested_pending'] = df['cnt_tested_pending'].astype(pd.Int32Dtype())
	df['cnt_recovered'] = df['cnt_recovered'].astype(pd.Int32Dtype())
	df['cnt_death'] = df['cnt_death'].astype(pd.Int32Dtype())
	df['cnt_death_new'] = df['cnt_death_new'].astype(pd.Int32Dtype())
	df['cnt_hospitalized'] = df['cnt_hospitalized'].astype(pd.Int32Dtype())
	df['cnt_hospitalized_new'] = df['cnt_hospitalized_new'].astype(pd.Int32Dtype())
	df['cnt_hospitalized_current'] = df['cnt_hospitalized_current'].astype(pd.Int32Dtype())
	df['cnt_icu_current'] = df['cnt_icu_current'].astype(pd.Int32Dtype())
	df['cnt_icu_total'] = df['cnt_icu_total'].astype(pd.Int32Dtype())
	df['cnt_vent_current'] = df['cnt_vent_current'].astype(pd.Int32Dtype())
	df['cnt_vent_total'] = df['cnt_vent_total'].astype(pd.Int32Dtype())
	df['cnt_tested'] = df['cnt_tested'].astype(pd.Int32Dtype())
	df['cnt_tested_new'] = df['cnt_tested_new'].astype(pd.Int32Dtype())

	# reorder and drop columns
	df = df[['hash','date_stamp','datetime_checked','us_state_postal','us_state_fips','cnt_tested_pos','cnt_tested_pos_new','cnt_tested_neg','cnt_tested_neg_new','cnt_tested_pending','cnt_recovered','cnt_death','cnt_death_new','cnt_hospitalized','cnt_hospitalized_new','cnt_hospitalized_current','cnt_icu_current','cnt_icu_total','cnt_vent_current','cnt_vent_total','cnt_tested','cnt_tested_new']]

	return df

if __name__ == "__main__":
	path = os.path
	# Loop over the files within state folder
	for filename in os.listdir('./data/us/covidtracking/state/raw'):
		if filename.endswith('.csv') and path.exists(f'./data/us/covidtracking/state/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us/covidtracking/state/raw/{filename}")
			df = cleanData(data)
			df.to_csv(f"./data/us/covidtracking/state/clean/{filename}", index=False)
			


