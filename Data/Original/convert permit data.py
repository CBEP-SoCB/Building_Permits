# -*- coding: utf-8 -*-
"""
This simple script takes U.S. Census building permit data as downloaded from
the HUD source (and edited by Tyler during download to limit to only CB towns),
and reformats it into a more useable form.

The logic is straight forward.  Each TOWN is represented in the downloaded data
by eleven lines of data (including blank lines, etc.), organized with data
types in rows and years in columns. 

Here we read in a block of eleven lines, record the data into internal lists,
and output the data to a CSV in a "tidy" data format, with observations (Years
by towns) on rows and data types in columns.

The Data Columns have the following meanings (approximate -- see metadata for
the original data source for original wording).:
    
    
    'Town':        Name of the Town/location for which data is reported
    'County':      Name of the COunty
    'Year':        Year of related data
    'Total':       Total housing units permitted
    'Single':      Single Family Homes permitted
    'Multifamily': All units in multi family structures permitted
    'Duplex':      Units permitted in two-family structures
    'TripQuad':    Units permitted in three or four family structures
    'QuintPlus':   Units permitted in structures with five or more units
    
"""

import csv
with open('bldgpermits.csv', 'w', newline = '') as outfile:
    thewriter = csv.writer(outfile)
    thewriter.writerow(['Town', 'County', 'Year',
                         'Total', 
                         'Single',
                         'Multifamily',
                         'Duplex',
                         'TripQuad',
                         'QuintPlus'])
    with open('CBEP Building Permits Data.csv', 'r') as infile:
        for line in range(494):
            which = line % 11
            if which == 0:
                l = next(infile)[:-1]
            elif which == 1:
                l = next(infile)[:-1]
                town = l.split(',')[0].strip('"')
            elif which == 2:
                l = next(infile)[:-1]
                county = l.split(',')[0].strip('()')
            elif which == 3:
                l = next(infile)[:-1]
            elif which == 4:
                l = next(infile)[:-1]
                total= l.split(',')[1:]
            elif which == 5:
                l = next(infile)[:-1]
                single= l.split(',')[1:]
            elif which == 6:
                l = next(infile)[:-1]
                multi= l.split(',')[1:]
            elif which == 7:
                l = next(infile)[:-1]
                duplex = l.split(',')[1:]
            elif which == 8:
                l = next(infile)[:-1]
                tripquad= l.split(',')[1:]
            elif which == 9:
                l = next(infile)[:-1]
                quintplus = l.split(',')[1:]
            elif which == 10:
                l = next(infile)[:-1]
                for year in range(1980,2018):
                    theline = [town, county, year,
                               total[year-1980],
                               single[year-1980],
                               multi[year-1980],
                               duplex[year-1980],
                               tripquad[year-1980],
                               quintplus[year-1980]]
                    thewriter.writerow(theline)

            
            
        
