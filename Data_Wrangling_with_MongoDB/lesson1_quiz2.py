#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import os
import xlrd
from zipfile import ZipFile

DATADIR = "./data"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"

#
def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    data = {}

    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    coast_vals = sheet.col_values(1,1)
    min_coast = min(coast_vals)
    max_coast = max(coast_vals)
    min_time = xlrd.xldate_as_tuple(sheet.cell_value(coast_vals.index(min_coast)+1,0),0)
    max_time = xlrd.xldate_as_tuple(sheet.cell_value(coast_vals.index(max_coast)+1,0),0)

    data['maxtime'] = max_time
    data['maxvalue'] = max_coast
    data['mintime'] = min_time
    data['minvalue'] = min_coast
    data['avgcoast'] = sum(coast_vals)/len(coast_vals)

    return data


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    #open_zip(datafile) #already extracted the file..
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()

