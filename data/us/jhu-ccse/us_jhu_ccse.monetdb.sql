
/*---------------------*/
/* us_jhu_ccse_country */
/*---------------------*/
create table if not exists  us_jhu_ccse_country_dev (
"date_stamp" date,
"iso3166_1" varchar(2),
"cnt_confirmed" int,
"cnt_death" int,
"cnt_recovered" int,
"cnt_active" int
)

--import
delete from us_jhu_ccse_country_dev;
COPY offset 2 INTO "us_jhu_ccse_country_dev" FROM '/var/monetdb5/dbfarm/country_all.csv' USING DELIMITERS ',','\n','"' NULL AS '';

-- View
create or replace view rds_us_jhu_ccse_country as
select date_stamp, iso3166_1, cnt_confirmed, cnt_death, cnt_recovered, cnt_active,
cast(null as varchar(3)) as iso3166_1_a3,
cast(null as varchar(3)) as iso3166_1_nn,
cast(date_to_str(date_stamp,'%Y') as varchar(4)) as year_stamp,
cast(date_to_str(date_stamp,'%m') as varchar(2)) as month_stamp,
cast(date_to_str(date_stamp,'%d') as varchar(2)) as day_stamp,
cast(date_to_str(date_stamp,'%Y-Q')||quarter(date_stamp ) as varchar(7)) as quarter_stamp,
cast(date_to_str(date_stamp,'%Y-%m') as varchar(7)) as yearmonth_stamp,
cast(date_to_str(date_stamp,'%Y-W%V') as varchar(8)) as week_stamp,
cast(date_to_str(date_stamp,'%Y-W%V-%u') as varchar(10)) as dow_stamp,
cast(date_to_str(date_stamp,'%Y-%j') as varchar(8)) as doy_stamp
from us_jhu_ccse_country_dev
order by date_stamp, iso3166_1
;

/*----------------------*/
/* us_jhu_ccse_us_state */
/*----------------------*/

create table if not exists  us_jhu_ccse_us_state_dev (
"date_stamp" date,
"iso3166_1" varchar(2),
"subdivision_code" varchar(2),
"us_state_fips" varchar(2),
"us_state_postal" varchar(2),
"cnt_confirmed" int,
"cnt_death" int,
"cnt_recovered" int
)
;

--import
delete from us_jhu_ccse_us_state_dev;
COPY offset 2 INTO "us_jhu_ccse_us_state_dev" FROM '/var/monetdb5/dbfarm/us_state_all.csv' USING DELIMITERS ',','\n','"' NULL AS '';

-- View
create or replace view rds_us_jhu_ccse_us_state as
select date_stamp, iso3166_1, subdivision_code, us_state_fips, us_state_postal, cnt_confirmed, cnt_death, cnt_recovered,
cast(null as varchar(3)) as iso3166_1_a3,
cast(null as varchar(3)) as iso3166_1_nn,
cast(date_to_str(date_stamp,'%Y') as varchar(4)) as year_stamp,
cast(date_to_str(date_stamp,'%m') as varchar(2)) as month_stamp,
cast(date_to_str(date_stamp,'%d') as varchar(2)) as day_stamp,
cast(date_to_str(date_stamp,'%Y-Q')||quarter(date_stamp ) as varchar(7)) as quarter_stamp,
cast(date_to_str(date_stamp,'%Y-%m') as varchar(7)) as yearmonth_stamp,
cast(date_to_str(date_stamp,'%Y-W%V') as varchar(8)) as week_stamp,
cast(date_to_str(date_stamp,'%Y-W%V-%u') as varchar(10)) as dow_stamp,
cast(date_to_str(date_stamp,'%Y-%j') as varchar(8)) as doy_stamp
from us_jhu_ccse_us_state_dev
order by date_stamp, subdivision_code
;



/*----------------------*/
/* us_jhu_ccse_us_state */
/*----------------------*/

create table if not exists  us_jhu_ccse_us_county_dev (
"date_stamp" date,
"iso3166_1" varchar(2),
"subdivision_code" varchar(2),
"us_state_fips" varchar(2),
"us_state_postal" varchar(2),
"us_admin2_code" varchar(5),
"us_county_fips" varchar(5),
"cnt_confirmed" int,
"cnt_death" int,
"cnt_recovered" int
)
;

--import
delete from us_jhu_ccse_us_county_dev;
COPY offset 2 INTO "us_jhu_ccse_us_county_dev" FROM '/var/monetdb5/dbfarm/us_county_all.csv' USING DELIMITERS ',','\n','"' NULL AS '';

-- View
create or replace view rds_us_jhu_ccse_us_county as
select date_stamp, iso3166_1, subdivision_code, us_state_fips, us_state_postal, us_admin2_code, us_county_fips, cnt_confirmed, cnt_death, cnt_recovered,
cast(null as varchar(3)) as iso3166_1_a3,
cast(null as varchar(3)) as iso3166_1_nn,
cast(date_to_str(date_stamp,'%Y') as varchar(4)) as year_stamp,
cast(date_to_str(date_stamp,'%m') as varchar(2)) as month_stamp,
cast(date_to_str(date_stamp,'%d') as varchar(2)) as day_stamp,
cast(date_to_str(date_stamp,'%Y-Q')||quarter(date_stamp ) as varchar(7)) as quarter_stamp,
cast(date_to_str(date_stamp,'%Y-%m') as varchar(7)) as yearmonth_stamp,
cast(date_to_str(date_stamp,'%Y-W%V') as varchar(8)) as week_stamp,
cast(date_to_str(date_stamp,'%Y-W%V-%u') as varchar(10)) as dow_stamp,
cast(date_to_str(date_stamp,'%Y-%j') as varchar(8)) as doy_stamp
from us_jhu_ccse_us_county_dev
order by date_stamp, subdivision_code, us_admin2_code
;



