import os
import requests
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    # get the district info
    response = requests.get("https://districtinformation.tnedu.gov/api/districts")
    if response.status_code != 200:
        print("Request failed ["+response.status_code+"]")

    # add the results to a data frame
    df = pd.DataFrame(columns = ['district_id', 'district_name', 'region_id', 'region_name']) 
    districtArr = response.json()
    for district in districtArr:
        region = district['region']
        df = df.append({'district_id' : district['id'], 'district_name' : district['name'], 'region_id' : region['id'], 'region_name' : region['name']}, ignore_index = True)

    df = df.sort_values(by=['district_id','region_id'], ascending=True)
    
    # write the data frame to a dated snapshot
    date = datetime.now().strftime('%Y-%m-%d')
    snapshot = './data/us-tn/tn-edu/raw/districts-'+date+'.csv'
    df.to_csv(f'{snapshot}', index=False)
