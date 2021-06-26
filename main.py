#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import boto3
import csv
import argparse
import sys
import logging
import datetime
from datetime import datetime
from logging import critical, error, info, warning, debug

#resources
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO, stream=sys.stdout)

# validate date
def validate_date(str_date):
    debug("validate_date - |{0}|".format(str_date))

    try:
        datetime.strptime(str_date, "%Y-%m-%d")
    except ValueError as e:
        debug("ValueError: {0}.".format(e))
        raise Exception("This is the incorrect date format. It should be YYYY-MM-DD")


# process
def process(filename, input_date):
    debug("process '{0}', '{1}'".format(filename, input_date))

    try:
        with open(filename, 'r') as file:
            next(file, None)
            reader = csv.reader(file)
            for row in reader:
                row_cookie = row[0]
                row_date = datetime.fromisoformat(row[1]).strftime("%Y-%m-%d")
                if input_date == row_date:
                    print(row_cookie)


    except Exception as e:
        debug("Exception: {0}.".format(e))
        raise Exception("File does not exist or it was not possible to read the data")

if __name__ == '__main__':
    debug("Start process")

    # Create the parser
    parser = argparse.ArgumentParser(description="List of cookies")

    # Add the arguments file
    parser.add_argument('-f', type=str, 
                              help='File name', 
                              nargs=1, 
                              action='store', 
                              required=True, 
                              dest="file",  
                              metavar="FILE")

    # Add the arguments date
    parser.add_argument('-d',  type=str, 
                               help='Date cookie',  
                               nargs=1, 
                               action='store', 
                               required=True, 
                               dest="date",  
                               metavar="DATE")

    args = parser.parse_args()
    debug("Arguments: {0}, {1}".format( args.file[0], args.date[0] ))

    # validation
    try:
        # validate date
        validate_date(args.date[0])
        # begin process
        process(args.file[0], args.date[0])
    except Exception as e:
        print(e)



