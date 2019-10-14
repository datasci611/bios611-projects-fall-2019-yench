## Background
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This project intends to create a shiny dashboard which alllows user to visualize the different services provided by UMD.   

## Plots to be included
1. A histogram of counts of services UMD provided, by tpyes of services.
   User can choose the years and the types of service they want to look at.

2. A scatter plot of two selected variables that are not 'Date' and 'Client File number', and an estimate of correlation between the two variables.

3. For each household, count the number of each type of services it used, divide by the number of all visits, and plot against the number of people in that household (estimated by the maximum of 'Food provided for' of that household throughout time).


## Data source
1. [UMD_Services_Provided_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_20190719.tsv)

1. [UMD_Services_Provided_metadata_20190719.tsv](https://raw.githubusercontent.com/biodatascience/datasci611/gh-pages/data/project1_2019/UMD_Services_Provided_metadata_20190719.tsv)


## Variables to be included in the analysis:
  Date
  Client File Number
  Bus Tickets
  Food Provided for
  Food Pounds
  Clothing Items
  Diapers
  School Kits
  Hygiene Kits