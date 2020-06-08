#!/bin/sh

# the state code should be the first input
stateCode=$1

# the URL to download should be the second
url=$2

# todays date in ISO
date=`date +%F`

# the output directory
DIR=$3

# pull the html
if [ ! -z $url ]
then
    # create file name from input and date
    FILE=$DIR"/"$date".xlsx"
    touch $FILE
	
	CSVFILE=$DIR"/"$date".csv"
    touch $CSVFILE
    
    # retrieve the web page using curl. time the process with the time command.
    curl -k --connect-timeout 100 $url >> $FILE
    # in2csv $FILE > file.csv
	xlsx2csv $FILE $CSVFILE
    
    #remove the .xlsx file so it doesn't get committed
    rm $FILE

    # git pull
    git add $CSVFILE
    git commit -m "Adding "$stateCode" data for "$date"."
    git push
fi