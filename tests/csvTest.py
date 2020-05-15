import sys
import unittest
import xmlrunner
import csv
import os
from datetime import datetime, date, timedelta

class TestCovidCsvData(unittest.TestCase):
    #first argument: defines where to look for the data
    DIRECTORY = "./data/us-ak/ak-dhss"
    #second arg: line to start reading headers at
    HEADER_LINE = 1

    #check that the headers remain the same from yesterday to today
    def test_header_changes(self):
        print('running test for directory : {}'.format(self.DIRECTORY))
        
        path = os.path
        #get today's and yesterday's files to compare headers 
        todays_file = []
        today = datetime.today().strftime('%Y-%m-%d')
        todays_file.append(today)
        todays_file.append('.csv')
        todays_file_name = ''.join(todays_file)

        # get yesterday's date name
        yesterdays_file = []
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        yesterdays_file.append(yesterday)
        yesterdays_file.append('.csv')
        yesterdays_file_name = ''.join(yesterdays_file)
        for filename in os.listdir(self.DIRECTORY):
            if filename == todays_file_name:
                with open(f'{self.DIRECTORY}/{filename}', 'r') as file1:
                    reader1 = csv.DictReader(file1)
                    headers1 = reader1.fieldnames
                    if int(self.HEADER_LINE) ==2 :
                        next(reader1)
                        headers1 = next(reader1) 
                    print(headers1)
                    self.assertIsNotNone(headers1, "No headers found in today's data file "+f'{self.DIRECTORY}/{filename}')

            if filename == yesterdays_file_name:
                 with open(f'{self.DIRECTORY}/{filename}', 'r') as file2:
                    if int(self.HEADER_LINE) ==2 :
                        next(file2)
                    reader2 = csv.DictReader(file2)
                    #get fieldnames from DictReader object and store in list
                    headers2 = reader2.fieldnames
                    print(headers2)
                    self.assertIsNotNone(headers2, "No headers found in yesterday's file"+f'{self.DIRECTORY}/{filename}')


       #creates a set of items that are found in only one of the header lists
        diff = set(headers1).symmetric_difference(set(headers2))
        msg = []
        msg.append("these headers were found in one file but not the other: ")
        for d in diff:
            msg.append(d)
            msg.append(',')
        result = ''.join(msg)
        self.assertEqual(len(diff),0, result)

    #check that today's file was imported
    def test_todays_file_exists(self):
        todays_file = []
        today = datetime.today().strftime('%Y-%m-%d')
        todays_file.append(today)
        todays_file.append('.csv')
        todays_file_name = ''.join(todays_file)
        self.assertTrue(todays_file_name in os.listdir(self.DIRECTORY),"today's file has not been imported")
        

if __name__ == '__main__':
    #pass in an argument that tells where to find the data dir to test (in this fomrat: './data/us-ak/ak-dhss'),
    #and, optionally, if the first line should be skipped to find the header row 
    if len(sys.argv) > 0:
        TestCovidCsvData.HEADER_LINE = sys.argv.pop()
        TestCovidCsvData.DIRECTORY = sys.argv.pop()

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
