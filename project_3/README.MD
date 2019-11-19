# BIOS611 Project 3 

## Background and objective
Urban Ministries of Durham (UMD) is a non-profit organization providing shelter, food, clothing, hygiene kits, and other services to people who are homeless or in emergent needs in Durham. This projects focuses on the shelter aspect of UMD, and aims to understand how the shelter is utilized, what the shelter has achieved, and potentially provides ideas for future services. 

## Audience
UMD and stakeholders are the target audience of this project. 

## Questions
Specifically, there are 3 sets of questions I would like to address in this project:
1. Who uses UMD's shelter? Are their composition different from that of local population, in terms of race, gender, age, veteran status, and history of domestic violence, adjusted by year? 

(I'm very sorry that there is not much to for you to provide feedback yet. It took me forever to get the python code to work. I'll update the as much as I can during the week. You don't have to come back at a later time though, sorry again.)
(If time allows...)

2. How do clients utilize UMD's shelter, in terms of seasonality, duration, interval between shelter stay, and number of usage? 

3. What do clients walk away with after their stay in the shelter? Are we able to predict their return by what they recieve or achieve in the shelter?


## Data source
 
1. UMD
UMD provided a total of 16 datasets containing information of clients upon their entry to and exit from their shelter. X of the datasets are used in this project, as listed below.    
[to be updated](link for data)

2. United Census Bureau
The demographic data of Durham county is obtained from the American Community Survey DP05 (sex, race, ethnicity) and DP02 (veteran and disability status) tables produced by US Census Bureau.  
[American Community Survey Table DP05 2017: ACS 5-Year Estimates Data Profiles](https://data.census.gov/cedsci/table?hidePreview=true&g=0600000US3706390932&q=Durham%20township,%20Durham%20County,%20North%20Carolina&table=DP05&tid=ACSDP5Y2017.DP05&lastDisplayedRow=93&y=)

[American Community Survey Table DP02 2017: ACS 5-Year Estimates Data Profiles]
(https://data.census.gov/cedsci/table?q=Durham%20County,%20North%20Carolina&hidePreview=true&table=DP02&tid=ACSDP5Y2017.DP02&lastDisplayedRow=0&mode=&g=)


## Analysis approach
Python: for preparing analysis datasets to be analyzed with R  

R: The analyses of three questions will come with summary statistics and plots, and for question 1 and 3 there will be statistical tests. Output will be an html report.  

Makefile: for downloading data and running a python script and R markdown, and production of dependency plot.

Docker: for creating an environment in which this project is run.
