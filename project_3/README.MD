# BIOS611 Project 3 

## Background and objective
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This projects focuses on the shelter aspect of UMD, and aims to compare the composition of shelter clients with that of local population. Specifically, who use UMD's shelter? Are their composition different from that of local population, in terms of sex, age, race, ethnicity, and veteran status? 

## Audience
UMD and stakeholders are the target audience of this project. 

## Data source
 
1. UMD
UMD provided a total of 16 datasets containing information of clients upon their entry to and exit from their shelter. 2 of the datasets are used in this project, as listed below.    
[CLIENT_191102.tsv.txt](https://github.com/datasci611/bios611-projects-fall-2019-yench/blob/master/project_3/data/raw/CLIENT_191102.tsv.txt)
[DISABILITY_ENTRY_191102.tsv.txt](https://github.com/datasci611/bios611-projects-fall-2019-yench/blob/master/project_3/data/raw/DISABILITY_ENTRY_191102.tsv.txt)

2. United Census Bureau American Community Survey
The demographic data of Durham county is obtained from the American Community Survey tables DP05 (sex, race, ethnicity), ACS_17_5YR_B21001 (veteran), and S1810 (disability) produced by US Census Bureau.  
[American Community Survey Table DP05 2017: ACS 5-Year Estimates Data Profiles](https://data.census.gov/cedsci/table?hidePreview=true&g=0600000US3706390932&q=Durham%20township,%20Durham%20County,%20North%20Carolina&table=DP05&tid=ACSDP5Y2017.DP05&lastDisplayedRow=93&y=)

[American Community Survey B21001 SEX BY AGE BY VETERAN STATUS FOR THE CIVILIAN POPULATION 18 YEARS AND OVER]
(https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=CF)

[American Community Survey S1810 DISABILITY CHARACTERISTICS]
(https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_17_5YR_S1810&prodType=table)


## Analysis approach
Python: for preparing analysis datasets to be analyzed with R  

R: for analysis of three questions. An R Markdown file and an report are produced.  

Makefile: for managing the project flow.

Dockerfile: builds a docker container based on rocker/tidyverse, and installs the latest version of tidyr package to access pivot_wider and pivot_longer functions. The building step will take a while.
