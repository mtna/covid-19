import os
import requests
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    # get the district info
    response = requests.get("https://districtinformation.tnedu.gov/api/districts")
    if response.status_code != 200:
        print("Request failed ["+response.status_code+"]")

    # date collected
    today = datetime.date(datetime.now()).isoformat()

    # add the results to a data frame
    df = pd.DataFrame(columns = ['district_id', 'district_name', 'region_id', 'region_name', 'student_cases', 'staff_cases', 'date_stamp']) 
    districtArr = response.json()
    for district in districtArr:
        region = district['region']
        covid = district['covidData']
        df = df.append({'district_id' : district['id'], 'district_name' : district['name'], 'region_id' : region['id'], 'region_name' : region['name'], 'student_cases' : covid['studentCases'], 'staff_cases' : covid['staffCases'], 'date_stamp' : today}, ignore_index = True)

    df = df.sort_values(by=['district_id','region_id'], ascending=True)
    
    # write the data frame to a dated snapshot and to latest
    date = datetime.now().strftime('%Y-%m-%d')
    snapshot = './data/us-tn/tn-edu/raw/districts-'+date+'.csv'
    df.to_csv(f'{snapshot}', index=False)
    df.to_csv(f'./data/us-tn/tn-edu/raw/districts-latest.csv', index=False)