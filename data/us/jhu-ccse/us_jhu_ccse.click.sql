
create database if not exists covid19;

-- TRUNCATE TABLE us_jhu_ccse_country_live;
-- TRUNCATE TABLE us_jhu_ccse_us_state_live;
-- TRUNCATE TABLE us_jhu_ccse_us_county_live;

/*
insert into us_jhu_ccse_country_bak select * from us_jhu_ccse_country_live;

cat /efs/mtna-archive/covid19/us/jhu-ccse/country_all.csv | docker run -i --rm yandex/clickhouse-client -m --host clickhouse.vpc.mtna.us -d covid19 --query="INSERT INTO us_jhu_ccse_country_live FORMAT CSVWithNames"

cat /efs/mtna-archive/covid19/us/jhu-ccse/us_state_all.csv | docker run -i --rm yandex/clickhouse-client -m --host clickhouse.vpc.mtna.us -d covid19 --query="INSERT INTO us_jhu_ccse_us_state_live FORMAT CSVWithNames"

cat /efs/mtna-archive/covid19/us/jhu-ccse/us_county_all.csv | docker run -i --rm yandex/clickhouse-client -m --host clickhouse.vpc.mtna.us -d covid19 --query="INSERT INTO us_jhu_ccse_us_county_live FORMAT CSVWithNames"

 */

/*---------*/
/* country */
/*---------*/
create table if not exists us_jhu_ccse_country_live (
"date_stamp" Date,
"iso3166_1" String,
"cnt_confirmed" Int32,
"cnt_death" Int32,
"cnt_recovered" Int32,
"cnt_active" Int32
)
ENGINE = MergeTree()
ORDER BY ("date_stamp","iso3166_1")
; 


/*
clickhouse-client -d covid19 --query "INSERT INTO us_jhu_ccse_country_dev FORMAT CSVWithNames" < /archive/covid19/us/jhu-ccse/country_all.csv;

*/

-- View
create or replace view rds_us_jhu_ccse_country as
select date_stamp, iso3166_1, cnt_confirmed, cnt_death, cnt_recovered, cnt_active,
-- null as iso3166_1_a3,
-- null as iso3166_1_nn,
formatDateTime(date_stamp,'%Y') as year_stamp,
formatDateTime(date_stamp,'%m') as month_stamp,
formatDateTime(date_stamp,'%d') as day_stamp,
concat(formatDateTime(date_stamp,'%Y-Q'),toString(toQuarter(date_stamp))) as quarter_stamp,
formatDateTime(date_stamp,'%Y-%m') as yearmonth_stamp,
formatDateTime(date_stamp,'%Y-W%V') as week_stamp,
formatDateTime(date_stamp,'%Y-W%V-%u') as dow_stamp,
formatDateTime(date_stamp,'%Y-%j') as doy_stamp
from us_jhu_ccse_country_live
order by date_stamp, iso3166_1
;

/*----------*/
/* US State */
/*----------*/

create table if not exists  us_jhu_ccse_us_state_live (
"date_stamp" Date,
"iso3166_1" String,
"subdivision_code" String,
"us_state_fips" String,
"us_state_postal" String,
"cnt_confirmed" Int32,
"cnt_death" Int32,
"cnt_recovered" Int32
)
ENGINE = MergeTree()
ORDER BY ("date_stamp","iso3166_1","subdivision_code")
; 

/*
clickhouse-client -d covid19 --query "INSERT INTO us_jhu_ccse_us_state_dev FORMAT CSVWithNames" < /archive/covid19/us/jhu-ccse/us_state_all.csv;
*/

-- View
create or replace view rds_us_jhu_ccse_us_state as
select date_stamp, iso3166_1, subdivision_code, us_state_fips, us_state_postal, cnt_confirmed, cnt_death, cnt_recovered,
-- null as iso3166_1_a3,
--- null as iso3166_1_nn,
formatDateTime(date_stamp,'%Y') as year_stamp,
formatDateTime(date_stamp,'%m') as month_stamp,
formatDateTime(date_stamp,'%d') as day_stamp,
concat(formatDateTime(date_stamp,'%Y-Q'),toString(toQuarter(date_stamp))) as quarter_stamp,
formatDateTime(date_stamp,'%Y-%m') as yearmonth_stamp,
formatDateTime(date_stamp,'%Y-W%V') as week_stamp,
formatDateTime(date_stamp,'%Y-W%V-%u') as dow_stamp,
formatDateTime(date_stamp,'%Y-%j') as doy_stamp
from us_jhu_ccse_us_state_live
order by date_stamp, subdivision_code
;



/*----------------------*/
/* us_jhu_ccse_us_county */
/*----------------------*/

create table if not exists  us_jhu_ccse_us_county_live (
"date_stamp" Date,
"iso3166_1" String,
"subdivision_code" String,
"us_state_fips" String,
"us_state_postal" String,
"us_admin2_code" String,
"us_county_fips" String,
"cnt_confirmed" Int32,
"cnt_death" Int32,
"cnt_recovered" Int32
)
ENGINE = MergeTree()
ORDER BY ("date_stamp","iso3166_1","subdivision_code")
; 


/*
clickhouse-client -d covid19 --query "INSERT INTO us_jhu_ccse_us_county_dev FORMAT CSVWithNames;" < /archive/covid19/us/jhu-ccse/us_county_all.csv;
docker container run -it --rm yandex/clickhouse-client -h clickhouse.vpc.mtna.us
*/

-- View
create or replace view rds_us_jhu_ccse_us_county as
select date_stamp, iso3166_1, subdivision_code, us_state_fips, us_state_postal, us_admin2_code, us_county_fips, cnt_confirmed, cnt_death, cnt_recovered,
-- null as iso3166_1_a3,
-- null as iso3166_1_nn,
formatDateTime(date_stamp,'%Y') as year_stamp,
formatDateTime(date_stamp,'%m') as month_stamp,
formatDateTime(date_stamp,'%d') as day_stamp,
concat(formatDateTime(date_stamp,'%Y-Q'),toString(toQuarter(date_stamp))) as quarter_stamp,
formatDateTime(date_stamp,'%Y-%m') as yearmonth_stamp,
formatDateTime(date_stamp,'%Y-W%V') as week_stamp,
formatDateTime(date_stamp,'%Y-W%V-%u') as dow_stamp,
formatDateTime(date_stamp,'%Y-%j') as doy_stamp
from us_jhu_ccse_us_county_live
order by date_stamp, subdivision_code, us_admin2_code
;




