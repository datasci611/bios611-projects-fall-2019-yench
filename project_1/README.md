##Background
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene, and other services to homeless people and people in emergent needs in Durham. This projects aims to look at services provided by UMD in the past, and provide summary statistics useful for PR and storytelling, as well as discover trends that might help UMD respond better to changing needs in the future.    

## Questions to be addressed
### Part A. Summary statistics
1. How many households (family or individuals) used UMD services, total and by year?
1. How many portions of food, clothes, diapers, school kits, and hygiene kits were provided, total and by year?
1. Approximately how many unique individuals were served by UMD? 
1. How many times do clients come for services until they stood on their own, moved out of the community, or loss to follow-up? 
1. (Cont.) Among clients receiving more than one service, how long did it take them to stand on their own, move out of the community, or loss to follow-up? 

### Part B. Trends
1. Is there any particular season or month where UMD saw more clients coming?
1. Is there any particular season or month where UMD saw more new clients coming?
1. Is there any trend in the numbers of food portions, clothes, diapers, school kits and hygiene provided?

##Data source
UMD provided the two datasets used in this analysis:
1. [UMD_Services_Provided_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_20190719.tsv)
This data set contains the record of services provided by UMD from 1/1/2002 to 7/19/2019.

1. [UMD_Services_Provided_metadata_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_metadata_20190719.tsv)
This dataset explains the columns in the first dataset.

## Variables to be included in the analysis
    Date
    Client File Number
    Food Provided for
    Clothings
    Diapers
    School kits
    Hygiene kits

## Proposed analysis approch
A.1 Count the number of visits (observations), total and by year. Numbers of visits by year will be displayed with a line plot.
A.2 The number of food, clothes, diapers, school kits, and hygiene kits will be summed over all observations, across all years or by year. Numbers by year will be displayed with a one line plot or a panel of line plots.
A.3 For each `<Client File Number>`, take the maximum value among Food Provided for, School kits, Hygiene kits, and 1, as a crude estimate of number of unique people served under this `<Client File Number>`. Sum this crude estimate across all `<Client File Numbers>` to obtain an estimate of the number of unique people served by UMD.
A.4 Count the number of visits for each `<Client File Number>` and draw a histogram on it, excluding clients who started using UMD services after 1/1/2019.
A.5 Obtain a list of clients who visited more than one time, and compute the duration between their first and last visits.

B.1 Count the number of visits by month, across different clients and years. Display with a line plot.
B.2 Include only the earliest observation for each `<Client File Number>`, and conduct analysis as in B.1.
B.3 Sum the numbers of food portions, clothes, diapers, school kits and hygiene provided in each month respectively, across different clients and years. Display the result with a panel of line plots.
    