## Background
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This project aims to look at services provided by UMD, produce summary statistics and plots useful for PR and storytelling, as well as discover trends that might help UMD respond better to changing needs in the future.   

# Questions to be addressed
##Part A. Summary statistics and plots for PR and storytelling 
1. How many counts of services did UMD provide for the duration of this dataset, total and by year?
2. How many unique households were served by UMD between 1999 and 2019?
3. How many new households joined UMD services yearly between 1999 and 2019?
4. How many UMD services did households typically use?
5. For households that used more than one UMD service, how long were the intervals between two services?
6. Among households receiving more than one service, how long did it take them to stand on their own feet, moved out of the community (including death), or in general, stopped using UMD services? 


## Part B. Trends
1. Is there any particular season or month where UMD saw more households coming?
2. Is there any particular season or month where UMD saw more new households coming?

# Data source
1. [UMD_Services_Provided_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_20190719.tsv)

1. [UMD_Services_Provided_metadata_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_metadata_20190719.tsv)

1. [Local Area Umemployment Statistics](https://data.bls.gov/timeseries/LAUMT372050000000004?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true)  (Series Id: LAUMT372050000000004)


# Variables to be included in the analysis:
  Date
  Client File Number
    

## Proposed analysis approach
A.1 Count the number of (observations), total and by year. Numbers of visits by year will be displayed with a bar plot.
A.2 Counting the number of unique `<Client File Number>`.
A.3 Obtain the date of first visit for each household, count the number of new households each year and present with a bar plot
A.4 Count the number of visits for each `<Client File Number>` and draw a histogram on it.
A5. Count the intervals between two visits of a household, and plot its distribution.
A.6 Obtain a list of clients who visited more than one time, and compute the duration between their first and last visits.

B.1 Count the number of visits by month, across different years. Display with a bar plot.
B.2 Include only the earliest observation for each `<Client File Number>`, and conduct analysis as in B.1.