import os
import requests
import pandas as pd
import time
from datetime import datetime

def infer(value):
    inferredValue = None
    if value == None:
        inferredValue = 0
    elif str(value).startswith('>') == True or str(value).startswith('<') == True:
        inferredValue = str(value)[1:]
    else:
        inferredValue = value

    return inferredValue;

if __name__ == "__main__":
    # read the district data and iterate over ever district
    districts = pd.read_csv(
        f"./data/us-tn/tn-edu/raw/districts-latest.csv", float_precision='round_trip')

    # define schools data frame
    df = pd.DataFrame(columns=['district_id', 'school_id', 'can_submit_covid_data', 'student_cases', 'staff_cases', 'student_cases_prev_week', 'staff_cases_prev_week', 'student_cases_inferred', 'staff_cases_inferred', 'student_cases_prev_week_inferred', 'staff_cases_prev_week_inferred', 'date_stamp', 'date_cases_updated',
                               'op_has_restrictions', 'op_restrictions', 'op_restrictions_reason', 'op_restrictions_active', 'op_restrictions_end_date', 'op_last_update', 'op_model_id', 'op_model_name', 'op_model_active'])

    # date collected
    today = datetime.date(datetime.now()).isoformat()

    # iterate over all districts
    for index, row in districts.iterrows():
        district = row['district_id']

        # get the schools info
        print("Getting school data for district "+str(district))
        response = requests.get(
            "https://districtinformation.tnedu.gov/api/districts/"+str(district)+"/schools")
        if response.status_code != 200:
            print("Request failed ["+str(response.status_code)+"] for district "+str(district))
            continue;

        schoolArr = response.json()
        for school in schoolArr:
            schoolOperatingModel = school['schoolOperatingModel']
            operatingModel = schoolOperatingModel['operatingModel']
            cases = school['covidData']

            opRestrictionCode = None
            opRestrictionReason = None
            opRestrictionActive = None
            if(schoolOperatingModel['restrictions'] == True and schoolOperatingModel.get('restrictionReason')):
                opRestrictionModel = schoolOperatingModel['restrictionReason']
                opRestrictionCode = opRestrictionModel['id']
                opRestrictionReason = opRestrictionModel['reason']
                opRestrictionActive = opRestrictionModel['active']
            df = df.append({'district_id': school['districtId'], 'school_id': school['id'], 'can_submit_covid_data': school['canSubmitCovidData'], 'student_cases': cases['studentCases'],
                            'staff_cases': cases['staffCases'], 'student_cases_prev_week': cases['lastWeekStudentCases'], 'staff_cases_prev_week': cases['lastWeekStaffCases'], 'student_cases_inferred': infer(cases['studentCases']),
                            'staff_cases_inferred': infer(cases['staffCases']), 'student_cases_prev_week_inferred': infer(cases['lastWeekStudentCases']), 'staff_cases_prev_week_inferred': infer(cases['lastWeekStaffCases']), 'date_stamp': today, 'date_cases_updated': cases['updatedDate'],
                            'op_has_restrictions': schoolOperatingModel['restrictions'], 'op_restrictions': opRestrictionCode, 'op_restrictions_reason': opRestrictionReason, 'op_restrictions_active': opRestrictionActive, 'op_restrictions_end_date': schoolOperatingModel['restrictionEndDate'],
                            'op_last_update': schoolOperatingModel['lastUpdatedDate'], 'op_model_id': operatingModel['id'], 'op_model_name': operatingModel['name'], 'op_model_active': operatingModel['active']}, ignore_index=True)
        time.sleep(.5)

    df = df.sort_values(by=['district_id', 'school_id'], ascending=True)

    # write the data frame to a dated snapshot
    date = datetime.now().strftime('%Y-%m-%d')
    snapshot = './data/us-tn/tn-edu/raw/schools-'+date+'.csv'
    df.to_csv(f'{snapshot}', index=False)
    df.to_csv(f'./data/us-tn/tn-edu/raw/schools-latest.csv', index=False)
