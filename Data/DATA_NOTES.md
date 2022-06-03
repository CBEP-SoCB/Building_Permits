# Building Permits Data

"CBEP Building Permits Data.xlsx" and 
"CBEP Building Permits Data.xlsx" 

## Access
The Spreadsheet was assembled from on-line sources by copying and pasting blocks 
of data town-by-town into Excel.

## Data Structure in Downloaded Files
To facilitate programmatic reorganization of the data, it is worth reviewing the 
structure of the data as accessed:

The data is organized as continuous blocks of data in Excel. Each block 
represents data from one township.  Columns are Years, rows are sizes of 
buildings.

Each block is structured as follows:

Three rows of Location Data
     Header
     Town
     County
One row of Dates (Years)
Six rows of Data
     Total Units
     Units in Single-Family Structures
     Units in All Multi-Family Structures
     Units in 2-unit Multi-Family Structures
     Units in 3- and 4-unit Multi-Family Structures
     Units in 5+ Unit Multi-Family Structures
One Empty Row

# Missing Towns
Three Towns are missing, presumably because they did not or do not report
building permit activity seperately:

*  Albany Twp
*  Greenwood
*  Mason Twp

# Reformatted Data
"bldpermits.csv"

We used a tiny python script to reorganize the data into a "Tidy" format 
suitable for automated data analysis and graphics.

The python script reads in a block of eleven lines, records the data into
internal lists, and outputs the data to a CSV in a "tidy" data format, with
observations (Years by Towns) on rows and data types in columns.

The Data Columns have the following meanings (approximate -- see metadata for
the original data source for original wording).:
    
|    Variable Name  |          Contents                                      |
|-------------------|--------------------------------------------------------|
|  Town             |  Name of the Town/location for which data is reported  |
|  County           |  Name of the County                                    |
|  Year             |  Year of related data                                  |
|  Total            |  Total housing units permitted                         |
|  Single           |  Single Family Homes permitted                         |
|  Multifamily      |  All units in multi family structures permitted        |
|  Duplex           |  nits permitted in two-family structures               |
|  TripQuad         |  Units permitted in three or four family structures    |
|  QuintPlus        |  Units permitted in structures with five or more units |
