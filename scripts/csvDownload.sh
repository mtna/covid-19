#!/bin/sh

# the state code should be the first input
stateCode=$1

# the URL to download should be the second
url=$2

# todays date in ISO
date=`date -I`

# the output directory
DIR=$3

# pull the csv
if [ ! -z $url ]
then
	
	
    # create file name from input and date
    FILE=$DIR"/"$date".csv"
	
	# don't create the file if it already exists for today.
	if [ ! -f $FILE ]; then
    	touch $FILE
    
    	# retrieve the web page using curl. time the process with the time command.
   	  curl -k --connect-timeout 100 $url >> $FILE
    	
	    git remote add github "https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/$GITHUB_REPOSITORY.git"
	    git pull github ${GITHUB_REF} --ff-only
      git add $FILE
      git commit -m "Adding "$stateCode" data for "$date"."
 	    git push github HEAD:${GITHUB_REF}
        
	else
	    echo "File already exists for today's data, not pulling again"
	fi 
fi
