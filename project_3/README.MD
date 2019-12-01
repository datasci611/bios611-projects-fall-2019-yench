# BIOS611 Project 3 

## Background and objective
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This projects focuses on the shelter aspect of UMD, and aims to compare the composition of shelter clients with that of local population. Specifically, who use UMD's shelter? Are their composition different from that of local population, in terms of sex, age, race, ethnicity, and veteran status? 

## Audience
UMD and stakeholders are the target audience of this project. 

## Data source
UMD provides a total of 16 datasets containing information of clients upon their entry to and exit from UMD's shelter. 2 of the datasets used in this project are listed below. Metadata of the the ACS data sets are also provided the data/raw directory.
1. Client dataset: this dataset contains information on age, gender, race, ethnicity, and veteran status of shleter clients. [CLIENT_191102.tsv.txt](https://github.com/datasci611/bios611-projects-fall-2019-yench/blob/master/project_3/data/raw/CLIENT_191102.tsv.txt)    
2. Disability dataset: this dataset contains information on the disability status, start and end date of disability, and type of disability of a subset of shelter clients. One client can have multiple records. [DISABILITY_ENTRY_191102.tsv.txt](https://github.com/datasci611/bios611-projects-fall-2019-yench/blob/master/project_3/data/raw/DISABILITY_ENTRY_191102.tsv.txt)  

#### United Census Bureau  
The demographic data of Durham county is obtained from the American Community Survey (ACS) tables DP05 (sex, race, ethnicity), ACS_17_5YR_B21001 (veteran), and S1810 (disability) produced by US Census Bureau.  

1. ACS Table DP05 2017: contains estimates of Durham population regarding sex, race, and ethnicity. [ACS 5-Year Estimates Data Profiles](https://data.census.gov/cedsci/table?hidePreview=true&g=0600000US3706390932&q=Durham%20township,%20Durham%20County,%20North%20Carolina&table=DP05&tid=ACSDP5Y2017.DP05&lastDisplayedRow=93&y=)  
2. ACS Table B21001: contains estimates of Durham population regarding veteran status. [ACS B21001 SEX BY AGE BY VETERAN STATUS FOR THE CIVILIAN POPULATION 18 YEARS AND OVER](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=CF)  
3. ACS Table S1810: contains estimates of Durham population regarding disability status. [ACS S1810 DISABILITY CHARACTERISTICS](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_17_5YR_S1810&prodType=table)  


## Analysis approach
Python: for preparing analysis datasets to be analyzed with R  

R: for analysis of three questions. An R Markdown file and an report are produced.  

Makefile: for managing the project flow.

Dockerfile: builds a docker container based on rocker/tidyverse, and installs the latest version of tidyr package to access pivot_wider and pivot_longer functions. The building step will take a while.
