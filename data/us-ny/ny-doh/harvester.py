import addfips
import os
import pandas as pd

def transformData(data):
	df = pd.DataFrame(data)
	# Rename the file headers
	df.rename({'Test Date': 'date_stamp', 'County': 'us_county_fips', 'New Positives': 'cnt_confirmed_new', 'Cumulative Number of Positives': 'cnt_confirmed', 'Total Number of Tests Performed': 'cnt_tested_new', 'Cumulative Number of Tests Performed': 'cnt_tested'}, axis="columns", inplace=True)
	
	# Convert the date format
	df['date_stamp'] = pd.to_datetime(df['date_stamp'])

	# order by date ascending to match other files
	df = df.sort_values(by='date_stamp', ascending=True)

	# Replace the county name with its Fips code
	af = addfips.AddFIPS()
	for key, value in df['us_county_fips'].items():
		df.at[key, 'us_county_fips'] = af.get_county_fips(value, 'New York')

	return df

if __name__ == "__main__":
	path = os.path
	# Loop over the files within state folder
	for filename in os.listdir('./data/us-ny/ny-doh/raw'):
		if filename.endswith('.csv') and path.exists(f'./data/us-ny/ny-doh/clean/{filename}') == False:
			print(filename)
			# For each csv file, map the transformed data to its respective file in the harvested folder
			data = pd.read_csv(f"./data/us-ny/ny-doh/raw/{filename}")
			df = transformData(data)
			df.to_csv(f"./data/us-ny/ny-doh/clean/{filename}", index=False)
			#add the latest clean file as latest.csv for db loading
			if path.exists(f'./data/us-ny/ny-doh/latest.csv'):
				#clear out the file's existing data and write to it
				open('./data/us-ny/ny-doh/latest.csv', 'w').close()
				df.to_csv(f"./data/us-ny/ny-doh/latest.csv", index=False)


