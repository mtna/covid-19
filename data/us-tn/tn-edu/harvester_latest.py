import pandas as pd
import datetime
import time
import json


def recode_bool(df, col):
    for index, row in df.iterrows():
        value = row[col]
        if value == True:
            df.loc[index, col] = 1
        else:
            df.loc[index, col] = 0
    return df


if __name__ == "__main__":
    # opening files
    districts = pd.read_csv('./data/us-tn/tn-edu/raw/districts-latest.csv')
    schools = pd.read_csv('./data/us-tn/tn-edu/raw/schools-latest.csv')

    # create normalized district IDs for districts-latest
    district_ids_normalized = []
    for district_id in districts['district_id']:
        district_ids_normalized.append('TN-' + str(district_id).rjust(5, '0'))
    districts['district_id_normalized'] = district_ids_normalized

    # create normalized school IDs & date column for schools-latest
    school_ids_normalized = []
    for index, row in schools.iterrows():
        district_row = districts.loc[districts['district_id']
                                     == row['district_id']]
        district_id_normalized = district_row['district_id_normalized'].values[0]

        school_id = row['school_id']
        school_ids_normalized.append(
            district_id_normalized + '-' + str(school_id).rjust(4, '0'))
        schools.loc[index, 'district_id'] = district_id_normalized
    schools['school_id'] = school_ids_normalized

    # moving normalized district IDs to distrcit_id column
    districts['district_id'] = districts['district_id_normalized']
    districts = districts.drop(['district_id_normalized'], axis=1)
    districts = districts.drop(['student_cases'], axis=1)
    districts = districts.drop(['staff_cases'], axis=1)
    districts = districts.drop(['date_stamp'], axis=1)

    # merging district/school dataframes into latest dataframe
    full = districts.merge(schools)
    latest = districts.merge(schools)

    # cleaning up latest columns
    latest = latest.drop(['district_name'], axis=1)
    latest = latest.drop(['region_name'], axis=1)
    latest = latest.drop(['op_model_name'], axis=1)
    latest = latest.drop(['op_restrictions_reason'], axis=1)
    latest = latest.drop(['op_restrictions_active'], axis=1)
    latest = recode_bool(latest, 'can_submit_covid_data')
    latest = recode_bool(latest, 'op_has_restrictions')
    latest = recode_bool(latest, 'op_model_active')

    # reformat date time to SQL timestamp
    latest['student_cases_inferred'] = latest['student_cases_inferred'].astype(pd.Int32Dtype())
    latest['staff_cases_inferred'] = latest['staff_cases_inferred'].astype(pd.Int32Dtype())
    latest['student_cases_prev_week_inferred'] = latest['student_cases_prev_week_inferred'].astype(pd.Int32Dtype())
    latest['staff_cases_prev_week_inferred'] = latest['staff_cases_prev_week_inferred'].astype(pd.Int32Dtype())
    latest['op_restrictions'] = latest['op_restrictions'].astype(pd.Int32Dtype())
    latest['op_restrictions_end_date'] = pd.to_datetime(latest['op_restrictions_end_date']).dt.strftime('%Y-%m-%d %H:%M:%S')
    latest['op_last_update'] = pd.to_datetime(latest['op_last_update']).dt.strftime('%Y-%m-%d %H:%M:%S')
    latest['date_stamp'] = pd.to_datetime(latest['date_stamp']).dt.strftime('%Y-%m-%d')
    latest['date_cases_updated'] = pd.to_datetime(latest['date_cases_updated']).dt.strftime('%Y-%m-%d %H:%M:%S')

    # ordering df
    latest = latest[['district_id', 'region_id', 'school_id', 'can_submit_covid_data', 'student_cases', 'staff_cases', 'student_cases_prev_week', 'staff_cases_prev_week', 'student_cases_inferred', 'staff_cases_inferred',
                    'student_cases_prev_week_inferred', 'staff_cases_prev_week_inferred','date_stamp', 'op_model_id', 'op_has_restrictions', 'op_restrictions', 'op_restrictions_end_date', 'op_last_update', 'date_cases_updated']]

    # create clean files
    full.to_csv(
        './data/us-tn/tn-edu/clean/districts-schools-full-clean.csv', index=False)
    latest.to_csv(
        './data/us-tn/tn-edu/latest.csv', mode='a', header=False, index=False)
