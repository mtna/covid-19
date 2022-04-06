import argparse
import datetime
import numpy as np
import pandas as pd
import re
import os

# record layout definitions
# note the we use Int64 data type for nullable integers
# see https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html
config = {
    "files": {
        "csse_covid_19_daily_reports_v20200122": {
            "variables": {
                "subdivision_name": {"dtype": "str"},
                "country_name": {"dtype": "str"},
                "last_updated": {"dtype": "str"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"},
            }
        },
        "csse_covid_19_daily_reports_v20200301": {
            "variables": {
                "subdivision_name": {"dtype": "str"},
                "country_name": {"dtype": "str"},
                "last_updated": {"dtype": "str"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"},
                "latitude": {"dtype": "float64"},
                "longitude": {"dtype": "float64"}
            }
        },
        "csse_covid_19_daily_reports_v20200322": {
            "variables": {
                "us_admin2_code": {"dtype": "str"},
                "us_admin2_name": {"dtype": "str"},
                "subdivision_name": {"dtype": "str"},
                "country_name": {"dtype": "str"},
                "last_updated": {"dtype": "str"},
                "latitude": {"dtype": "float64"},
                "longitude": {"dtype": "float64"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"},
                "cnt_active": {"dtype": "Int64"},
                "name_full": {"dtype": "str"}
            }
        },
        "csse_covid_19_daily_reports_v20200529": {
            "variables": {
                "us_admin2_code": {"dtype": "str"},
                "us_admin2_name": {"dtype": "str"},
                "subdivision_name": {"dtype": "str"},
                "country_name": {"dtype": "str"},
                "last_updated": {"dtype": "str"},
                "latitude": {"dtype": "float64"},
                "longitude": {"dtype": "float64"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"},
                "cnt_active": {"dtype": "Int64"},
                "name_full": {"dtype": "str"},
                "rate_incidence": {"dtype": "Float32"}, 
                "ratio_case_fatality": {"dtype": "Float32"}
            }
        },
        "country_all": {
            "variables": {
                "date_stamp": {"dtype": "str"},
                "iso3166_1": {"dtype": "str"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"},
                "cnt_active": {"dtype": "Int64"},
            }
        },
        "us_state_all": {
            "variables": {
                "date_stamp": {"dtype": "str"},
                "iso3166_1": {"dtype": "str"},
                "subdivision_code": {"dtype": "str"},
                "us_state_fips": {"dtype": "str"},
                "us_state_postal": {"dtype": "str"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"}
           }
        },
        "us_county_all": {
            "variables": {
                "date_stamp": {"dtype": "str"},
                "iso3166_1": {"dtype": "str"},
                "subdivision_code": {"dtype": "str"},
                "us_state_fips": {"dtype": "str"},
                "us_state_postal": {"dtype": "str"},
                "us_admin2_code": {"dtype": "str"},
                "us_county_fips": {"dtype": "str"},
                "cnt_confirmed": {"dtype": "Int64"},
                "cnt_deaths": {"dtype": "Int64"},
                "cnt_recovered": {"dtype": "Int64"}
           }
        }
    }
}
# GLOBALS
country_name_lookup_df = None
us_subdivision_name_lookup_df = None


def get_config():
    """Helper to get configuration information"""
    global config
    return config


def get_source_df(report_date):
    """Download the daily reports CSV file for specified date as a dataframe"""
    # init
    base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports"
    if report_date >= datetime.date(2020, 5, 29):
        df_info = get_config()[
            "files"]["csse_covid_19_daily_reports_v20200529"]
    elif report_date >= datetime.date(2020, 3, 22):
        df_info = get_config()[
            "files"]["csse_covid_19_daily_reports_v20200322"]
    elif report_date >= datetime.date(2020, 3, 1):
        df_info = get_config()[
            "files"]["csse_covid_19_daily_reports_v20200301"]
    else:
        df_info = get_config()[
            "files"]["csse_covid_19_daily_reports_v20200122"]
    # dataframe config
    df_url = base_url+"/"
    df_url += datetime.date.strftime(report_date, "%m-%d-%Y")
    df_url += ".csv"
    df_names = []
    df_dtypes = {}
    for key, value in df_info["variables"].items():
        df_names.append(key)
        df_dtypes[key] = value["dtype"]
    # download
    df = pd.read_csv(df_url, names=df_names, dtype=df_dtypes, header=0)
    # drop non-standard entities
    df = df[(df.country_name != 'Diamond Princess') & (df.country_name != 'Cruise Ship') 
        & (df.country_name != 'MS Zaandam') & (df.country_name != 'Channel Islands') 
        & (df.country_name != 'Others') & (df.country_name != 'Summer Olympics 2020') 
        & (df.country_name != 'Antarctica') & (df.country_name != 'Winter Olympics 2022')] 
    # remove leading/trailing spaces
    df.country_name = df.country_name.str.strip()
    return df


def generate_country_df(report_date, source_df):
    """
    Generate a country level dataset by filtering out subnational records from source data
    For the United States, the national counts are aggregated as a sum from lower level geographies
    """
    # patch country names
    if report_date >= datetime.date(2020, 3, 22):
        pass
    elif report_date == datetime.date(2020, 3, 21):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
        source_df.loc[(source_df.country_name == 'Gambia, The'),
                      'country_name'] = 'The Gambia'
        source_df.loc[(source_df.country_name == 'Bahamas, The'),
                      'country_name'] = 'The Bahamas'
        source_df.loc[(source_df.country_name == 'Cape Verde'),
                      'country_name'] = 'Cabo Verde'
    elif report_date == datetime.date(2020, 3, 20):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
        source_df.loc[(source_df.country_name == 'Gambia, The'),
                      'country_name'] = 'The Gambia'
        source_df.loc[(source_df.country_name == 'Bahamas, The'),
                      'country_name'] = 'The Bahamas'
    elif report_date == datetime.date(2020, 3, 19):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
        source_df.loc[(source_df.country_name == 'Gambia, The'),
                      'country_name'] = 'The Gambia'
        source_df.loc[(source_df.country_name == 'Bahamas, The'),
                      'country_name'] = 'The Bahamas'
    elif report_date == datetime.date(2020, 3, 18):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
        source_df.loc[(source_df.country_name == 'Gambia, The'),
                      'country_name'] = 'The Gambia'
    elif report_date == datetime.date(2020, 3, 17):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
    elif report_date == datetime.date(2020, 3, 16):
        source_df.loc[(source_df.country_name == 'Congo (Kinshasa)'),
                      'country_name'] = 'Republic of the Congo'
    elif report_date == datetime.date(2020, 3, 12):
        source_df.loc[(source_df.country_name == 'Mainland China'),
                      'country_name'] = 'China'
    elif report_date == datetime.date(2020, 3, 11):
        source_df.loc[(source_df.country_name == 'Mainland China'),
                      'country_name'] = 'China'
    elif report_date == datetime.date(2020, 3, 10):
        source_df.loc[(source_df.country_name == 'Hong Kong SAR'),
                      'country_name'] = 'Mainland China'
        source_df.loc[(source_df.country_name == 'Macao SAR'),
                      'country_name'] = 'Mainland China'
    elif report_date == datetime.date(2020, 3, 9):
        source_df.loc[(source_df.country_name == 'Hong Kong SAR'),
                      'country_name'] = 'Mainland China'
        source_df.loc[(source_df.country_name == 'Macao SAR'),
                      'country_name'] = 'Mainland China'
    elif report_date == datetime.date(2020, 3, 8):
        source_df = source_df[source_df.country_name != 'Republic of Ireland']
    elif report_date == datetime.date(2020, 2, 28):
        source_df.loc[(source_df.country_name == 'North Ireland'),
                      'country_name'] = 'UK'
    # aggregate at country level using country name
    agg_cols = {'cnt_confirmed': 'sum',
                'cnt_deaths': 'sum', 'cnt_recovered': 'sum'}
    if 'cnt_active' in source_df.columns:
        agg_cols['cnt_active'] = 'sum'
    country_df = source_df.groupby("country_name").agg(agg_cols)
    country_df.reset_index(inplace=True)
    # merge in country metadata
    country_df = pd.merge(country_df, get_country_name_lookup_df(),
                          left_on='country_name', right_on='country_name', how='left')
    # check for country matches errors
    unknown_country_df = country_df[country_df["iso3166_1"].isnull()]
    if unknown_country_df.shape[0] > 0:
        print(unknown_country_df)
        if os.path.isdir("temp"):
            country_df.to_csv("temp/country_error.csv")
        raise Exception("ERROR: one or more countries were not found")
    # compute derived variables
    country_df["date_stamp"] = report_date
    country_df["cnt_active"] = country_df["cnt_confirmed"] - \
        country_df["cnt_recovered"] - country_df["cnt_deaths"]
    # index and sort
    if os.path.isdir("temp"):
        country_df.to_csv("temp/country_temp.csv")
    country_df.set_index('iso3166_1', inplace=True, verify_integrity=True)
    country_df.sort_index(inplace=True)
    country_df.reset_index(inplace=True)
    # drop columns
    country_df = country_df.drop(
        ['subdivision_name', 'country_name', 'last_updated'],  axis=1, errors='ignore')
    # reorder columns
    ordered_cols = ['date_stamp', 'iso3166_1',
                    'cnt_confirmed', 'cnt_deaths', 'cnt_recovered','cnt_active']
    country_df = country_df[ordered_cols]
    return country_df

def generate_country_all():
    """Combine all countty datasets into a single file"""
    # setup country dataframe
    df_info = get_config()["files"]["country_all"]
    country_all_df = pd.DataFrame()
    # setup dataframe
    df_names = []
    df_dtypes = {}
    col_index = 0
    for key, value in df_info["variables"].items():
        df_names.append(key)
        df_dtypes[key] = value["dtype"]
    # iterate country reports
    regex = re.compile('country_\d{4}-\d{2}-\d{2}.csv')
    for entry in os.scandir('country'):
        match = regex.match(entry.name)
        if match:
            filepath = os.path.join('country', entry.name)
            # read file
            country_df = pd.read_csv(
                filepath, names=df_names, dtype=df_dtypes, header=0, keep_default_na=False)
            # add to all
            country_all_df = pd.concat(
                [country_all_df, country_df],  axis=0, ignore_index=True)
    # sort
    country_all_df = country_all_df.sort_values(by=['date_stamp', 'iso3166_1'])
    return country_all_df

def generate_us_county_df(report_date, source_df):
    """Generate U.S. County dataframe for specified date"""
    # patches
    if report_date == datetime.date(2020, 8, 11): # https://github.com/CSSEGISandData/COVID-19/issues/3019
        source_df.loc[(source_df.us_admin2_code == '31153') & (source_df.subdivision_name == 'Recovered'),'us_admin2_code'] = None
    # subset for US
    target_df = source_df[source_df.country_name == "US"]
    # drop colmns that are not needed
    target_df = target_df.drop(['last_updated','latitude','longitude','cnt_active','name_full'],  axis=1, errors='ignore')
    # set all null admin2 codes to 00000
    target_df.loc[ target_df.us_admin2_code.isna(), 'us_admin2_code'] = '00000'
    # make sure all codes have 5 digits
    target_df['us_admin2_code'] = target_df['us_admin2_code'].apply(lambda x: '{0:0>5}'.format(x))
    # move all 800nn and 900nn to 00000    
    target_df.loc[ target_df.us_admin2_code.str.startswith("800"), 'us_admin2_code'] = '00000'
    target_df.loc[ target_df.us_admin2_code.str.startswith("900"), 'us_admin2_code'] = '00000'
    if os.path.isdir("temp"):
        target_df.to_csv("temp/us_county_temp.csv")
    # change code for cruise ships
    target_df.loc[ target_df.us_admin2_code == '88888', 'us_admin2_code'] = '00000'
    target_df.loc[ target_df.us_admin2_code == '99999', 'us_admin2_code'] = '00000'
    # merge in subdivision metadata
    target_df = pd.merge(target_df, get_us_subdivision_name_lookup_df(),
                         left_on='subdivision_name', right_on='subdivision_name', how='left')
    # Change all 00000 to nn000
    loc = target_df.us_admin2_code == '00000'
    target_df.loc[loc,'us_admin2_code'] = target_df[loc].subdivision_code+'000'
    # aggregate
    agg_cols = {'cnt_confirmed': 'sum','cnt_deaths': 'sum', 'cnt_recovered': 'sum'}
    target_df = target_df.groupby(["us_admin2_code", 'subdivision_code','us_state_fips','us_state_postal']).agg(agg_cols)
    target_df.reset_index(inplace=True)
    # index and sort
    if os.path.isdir("temp"):
        target_df.to_csv("temp/us_county_temp.csv")
    target_df.set_index('us_admin2_code', inplace=True, verify_integrity=True)
    target_df.sort_index(inplace=True)
    target_df.reset_index(inplace=True)
    # compute derived variables
    target_df["date_stamp"] = report_date
    target_df['iso3166_1']='US'
    # set county fips (code does not end with 000)
    loc = ~target_df.us_admin2_code.str.endswith('000')
    target_df.loc[loc,'us_county_fips'] = target_df[loc].us_admin2_code
    # reorder columns 
    ordered_cols = ['date_stamp', 'iso3166_1','subdivision_code','us_state_fips','us_state_postal','us_admin2_code','us_county_fips','cnt_confirmed', 'cnt_deaths', 'cnt_recovered']
    target_df = target_df[ordered_cols]
    if os.path.isdir("temp"):
        target_df.to_csv("temp/us_county_temp.csv")
    return target_df

def generate_us_county_all():
    """Combine all US County datasets into a single file"""
    # setup country dataframe
    df_info = get_config()["files"]["us_county_all"]
    target_df = pd.DataFrame()
    # setup dataframe
    df_names = []
    df_dtypes = {}
    col_index = 0
    for key, value in df_info["variables"].items():
        df_names.append(key)
        df_dtypes[key] = value["dtype"]
    # iterate reports
    regex = re.compile('us_county_\d{4}-\d{2}-\d{2}.csv')
    for entry in os.scandir('us_county'):
        match = regex.match(entry.name)
        if match:
            filepath = os.path.join('us_county', entry.name)
            # read file
            country_df = pd.read_csv(
                filepath, names=df_names, dtype=df_dtypes, header=0, keep_default_na=False)
            # add to all
            target_df = pd.concat(
                [target_df, country_df],  axis=0, ignore_index=True)
    # sort
    target_df = target_df.sort_values(by=['date_stamp', 'iso3166_1','subdivision_code','us_admin2_code'])
    return target_df


def generate_us_state_df(report_date, source_df):
    # subset for US
    source_df = source_df[source_df.country_name == "US"]
    # patches
    if report_date > datetime.date(2020, 3, 19):
        pass
    elif report_date == datetime.date(2020, 3, 19):
        source_df.loc[(source_df.subdivision_name == 'United States Virgin Islands'),'subdivision_name'] = 'Virgin Islands'
    elif report_date == datetime.date(2020, 3, 18):
        source_df.loc[(source_df.subdivision_name == 'United States Virgin Islands'),'subdivision_name'] = 'Virgin Islands'
    # aggregate at US state data
    agg_cols = {'cnt_confirmed': 'sum',
                'cnt_deaths': 'sum', 'cnt_recovered': 'sum'}
    target_df = source_df.groupby(
        ["country_name", "subdivision_name"]).agg(agg_cols)
    target_df.reset_index(inplace=True)
    # merge in country metadata
    target_df = pd.merge(target_df, get_country_name_lookup_df(),
                         left_on='country_name', right_on='country_name', how='left')
    # merge in subdivision metadata
    target_df = pd.merge(target_df, get_us_subdivision_name_lookup_df(),
                         left_on='subdivision_name', right_on='subdivision_name', how='left')
    # check for country matches errors
    unknown_df = target_df[target_df["subdivision_code"].isnull()]
    if unknown_df.shape[0] > 0:
        print(unknown_df)
        if os.path.isdir("temp"):
            unknown_df.to_csv("temp/us_state_temp.csv")
        raise Exception("ERROR: one or more entries were not found")
    # compute derived variables
    target_df["date_stamp"] = report_date
    # index and sort
    if os.path.isdir("temp"):
        target_df.to_csv("temp/us_state_temp.csv")
    target_df.set_index('subdivision_code', inplace=True, verify_integrity=True)
    target_df.sort_index(inplace=True)
    target_df.reset_index(inplace=True)
    # drop columns
    target_df = target_df.drop(
        ['subdivision_name', 'country_name'],  axis=1, errors='ignore')
    # reorder columns 
    ordered_cols = ['date_stamp', 'iso3166_1','subdivision_code','us_state_fips','us_state_postal','cnt_confirmed', 'cnt_deaths', 'cnt_recovered']
    target_df = target_df[ordered_cols]
    return target_df

def generate_us_state_all():
    """Combine all US State datasets into a single file"""
    # setup country dataframe
    df_info = get_config()["files"]["us_state_all"]
    target_df = pd.DataFrame()
    # setup dataframe
    df_names = []
    df_dtypes = {}
    col_index = 0
    for key, value in df_info["variables"].items():
        df_names.append(key)
        df_dtypes[key] = value["dtype"]
    # iterate reports
    regex = re.compile('us_state_\d{4}-\d{2}-\d{2}.csv')
    for entry in os.scandir('us_state'):
        match = regex.match(entry.name)
        if match:
            filepath = os.path.join('us_state', entry.name)
            # read file
            country_df = pd.read_csv(
                filepath, names=df_names, dtype=df_dtypes, header=0, keep_default_na=False)
            # add to all
            target_df = pd.concat(
                [target_df, country_df],  axis=0, ignore_index=True)
    # sort
    target_df = target_df.sort_values(by=['date_stamp', 'iso3166_1','subdivision_code'])
    return target_df

def get_country_name_lookup_df():
    global country_name_lookup_df
    # load country metadata if necessary
    if country_name_lookup_df is None:
        # keep_default_na=False prevent Namibia NA to be interpreted as NaN
        country_name_lookup_df = pd.read_csv(
            "country_name_lookup.csv", dtype=str, keep_default_na=False)
    return country_name_lookup_df

def get_us_subdivision_name_lookup_df():
    global us_subdivision_name_lookup_df
    # load country metadata if necessary
    if us_subdivision_name_lookup_df is None:
        # keep_default_na=False prevent Namibia NA to be interpreted as NaN
        us_subdivision_name_lookup_df = pd.read_csv(
            "us_subdivision_name_lookup.csv", dtype=str, keep_default_na=False)
    return us_subdivision_name_lookup_df

def harvest(report_date):
    """Harvests data for specified date if needed"""
    print("Harvesting "+repr(report_date))
    if not(os.path.isfile(f"country/country_{report_date.strftime('%Y-%m-%d')}.csv")) or args.force:
        source_df = get_source_df(report_date)
        country_df = generate_country_df(report_date, source_df)
        country_df.to_csv(
            f"country/country_{report_date.strftime('%Y-%m-%d')}.csv", index=False)
    if report_date >= datetime.date(2020,3,10):
        if not(os.path.isfile(f"us_state/us_state_{report_date.strftime('%Y-%m-%d')}.csv")) or args.force:
            source_df = get_source_df(report_date)
            us_state_df = generate_us_state_df(report_date, source_df)
            us_state_df.to_csv(
                f"us_state/us_state_{report_date.strftime('%Y-%m-%d')}.csv", index=False)
    if report_date >= datetime.date(2020,3,22):
        if not(os.path.isfile(f"us_county/us_county_{report_date.strftime('%Y-%m-%d')}.csv")) or args.force:
            source_df = get_source_df(report_date)
            us_county_df = generate_us_county_df(report_date, source_df)
            us_county_df.to_csv(
                f"us_county/us_county_{report_date.strftime('%Y-%m-%d')}.csv", index=False)
    return
def show_df_info(df):
    """Helper to dump a data frame information"""
    print(df.info())
    print(df.describe())
    print(df.head(10))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-from", "--datefrom",
                        help="Start date, ISO format, inclusive (default is yesterday)")
    parser.add_argument(
        "-to", "--dateto", help="Report end date, ISO format, exclusive (default is today)")
    parser.add_argument("-c", "--combine", action='store_true',
                        help="Combine all datasets")
    parser.add_argument("-f", "--force", action='store_true',
                        help="Force overwrite")
    args = parser.parse_args()

    print(args)

    report_from = datetime.date.today() - datetime.timedelta(days=1)
    report_to = datetime.date.today()
    if args.datefrom:
        report_from = datetime.datetime.strptime(
            args.datefrom, '%Y-%m-%d').date()
    if args.dateto:
        report_to = datetime.datetime.strptime(args.dateto, '%Y-%m-%d').date()
    print(report_from, report_to)

    delta = (report_to - report_from).days

    for i in range(delta):
        harvest(report_from + datetime.timedelta(i))

    if args.combine:
        df = generate_country_all()
        df.to_csv("country/country_all.csv", index=False)
        df = generate_us_state_all()
        df.to_csv("us_state/us_state_all.csv", index=False)
        df = generate_us_county_all()
        county_filename = 'us_county_all'
        county_compression_options = dict(method='zip', archive_name=f'{county_filename}.csv')
        df.to_csv("us_county/"+f'{county_filename}.zip', compression=county_compression_options, index=False)
