
# Building Permits Data

<img
    src="https://www.cascobayestuary.org/wp-content/uploads/2014/04/logo_sm.jpg"
    style="position:absolute;top:10px;right:50px;" />
    
Data on residential housing permits, ultimately from the U.S Census Building 
Permits Survey

# Introduction
Housing data and housing starts reflect economic activity and signal level of
land use change during a period of time.  Federal sources track and make public 
town by town data on housing permits.  We downloaded and reorganized
data on housing starts for Casco Bay Watershed towns.  The data is archived 
here.

# Statement of Purpose
CBEP is committed to the ideal of open science.  Our State of the Bay data
archives ensure the science underlying the 2020 State of the Bay report is
documented and reproducible by others. The purpose of these archives is to
release raw data and data analysis code whenever possible to allow others to
review, critique, learn from, and build upon CBEP science.

# Archive Structure
 CBEP 2020 State of the Bay data analysis repositories are divided into from two
 to four sub-folders.  All archives contain at least an "Original_Data" and a
 "Graphics" folder.  The other two folders are only included if strictly
 necessary.

- Original Data.  Original data, with a "DATA_SOURCES.md" or "READ ME.txt" file
that documents data sources.  
    **DATA IN THIS FOLDER IS AS ORIGINALLY PROVIDED OR ACCESSED.** 

- Derived Data.  Data derived from the original raw data.  Includes
documentation of data reorganization steps, either in the form of files (R
notebooks, Excel files, etc.) that embody data transformations, or via another
README.txt file. - Analysis.  Contains one or more R Notebooks proceeding
through the data analysis steps. - Graphics.  Contains R Notebooks stepping
through development of related graphics, and also raw copies of resulting
graphics, usually in \*.png and \*.pdf formats.  These graphics may differ from
graphics as they appear in final State of the Bay graphical layouts.

# Summary of Data Sources
Data was accessed via the U.S. Department of Housing and Urban Development, 
Office of Policy Development and Research, State of the Cities Data Systems 
(SOCDS). Data is from the SOCDS Building Permits Database.  Data provides 
information on number of residential building permits issues by jurisdiction.

