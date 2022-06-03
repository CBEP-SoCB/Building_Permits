# Residential Building Permits Data

## Source
Data was accessed August 21, 2019 from the  U.S. Department of Housing and Urban
Development, Office of Policy Development and Research, State of the Cities Data
Systems (SOCDS). Data is from the SOCDS Building Permits Database. Data
provides information on number of residential building permits issued by
jurisdiction.

Data was accessed via the SOCDS web page, at: 
https://socds.huduser.gov/permits/

The data are most readily downloaded one town at a time. Data is delivered in a
table for each town, with rows for data types, and columns for years.  We copied
data  by hand from the website and pasted it into a spreadsheet. We wrote
a small python script to reformat the data for automated data
analysis.

Specifics on the data format are available in a help file at:
https://www.census.gov/const/C40/Sample/placeprt.pdf

The HUD data data is  itself derived from the U.S. Census building permits 
survey.  https://www.census.gov/construction/bps/.
