#!/bin/sh

# /bin/sh tools/covid19-scraper/scripts/statCanDownload.sh https://www150.statcan.gc.ca/n1/tbl/csv/13100766-eng.zip 13100766.csv ./data/ca/statcan/

# the URL to download should be the second
URL=$1
DIR=$3
DESIREDFILE=$2

# the output directory is the third
#DIR=$3
# pull the zip
if [ ! -z $URL ]
then
 	# todays date in ISO                            
	CSVFILE=$(date +%F).csv
	ZIPFILE=$DIR$(date +%F).zip
	
	#don't create the file if it already exists for today.
	if [ ! -f $ZIPFILE ]; then
    # create file name from input and date
    TEMPZIPFILE="13100766-eng.zip"
	                         
	wget -O $TEMPZIPFILE $URL
	
	
	#unzip and extract just the text to the file named with todays date
	# this is specific to the statcan dataset
	unzip -p $TEMPZIPFILE $DESIREDFILE > $CSVFILE
	unzip -l $TEMPZIPFILE
	
	#this file is big so we will rezip
	zip $ZIPFILE $CSVFILE
	
	# remove the temp files
	rm $TEMPZIPFILE
	rm $CSVFILE
	
	git pull
	git add $ZIPFILE
	git commit -m "Adding STATSCAN data for $(date +%F)."
	git push
	
	else
	    echo "File already exists for today's data, not pulling again"
	fi

fi