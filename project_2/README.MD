# BIOS611 Project 2 

[Project URL]: (https://yench.shinyapps.io/project_2/)

## Background
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This project intends to create a shiny dashboard which alllows stakeholders of UMD to visualize the different services provided by UMD.   

## Plots to be included
**Plot A1.** A histogram of counts of services UMD provided, by type of services.  
**Plot A2.** A pie chart showing the percentage of visits seeking the selected service among all visits. 
A user can choose the years and the type of service they want to look at.

**Plot B.** Family size and services
This section creates a scatterplot for a selected type of service with family size as the x-axis.
  
For the y-axis, a user can choose one of the three:  
i) count of visits attributable to the selected service, and  
ii) proportion of visits attributable to the selected service, and  
iii) average number of portions provided in each visit for the selected service


## Data source
This data set is provided by UMD. It contains records of services UMD provided from the 1990s to 2019. 
[UMD_Services_Provided_20190719.tsv](https://github.com/datasci611/bios611-projects-fall-2019-yench/blob/master/project_2/data/UMD_Services_Provided_20190719.tsv.txt)


## Variables included in the analysis:
Date, Client File Number, Bus Tickets, Food Provided for, Food Pounds, Clothing Items, Diapers, School Kits, and Hygiene Kits.