## This python script imports raw datasets, wrangles, and writes analysis datasets for further analysis in R.

## Input: ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv
##		  ACSDP5Y2017.DP02_data_with_overlays_2019-11-18T123256.csv
##        CLIENT_191102.tsv.txt
##        DISABILITY_ENTRY_191102.tsv.txt  

## Output: durham_sex.csv
##		   durham_age.csv
##		   durham_race.csv
##		   durham_ethnicity.csv
##		   durham_veteran.csv
##		   durham_disability.csv
##         client.csv
##         disability_entry_subject.csv
##         disability_entry_summary.csv


import pandas as pd
import numpy as np


# 1. Local demographic data
## Read in raw demographic datasets from US Census Bureau
durham_raw_sre = pd.read_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/raw/ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv')

durham_raw_vd = pd.read_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/raw/ACSDP5Y2017.DP02_data_with_overlays_2019-11-18T123256.csv')

## Concatenate two tables horizontally (as columns)
durham_raw = pd.concat([durham_raw_sre,durham_raw_vd], axis = 1 )  


## Only keep population estimates and percent estimates (discard margins of error)
durham = durham_raw.iloc[0:2,durham_raw.columns.str.contains('E')]


## Reshaping data structure 
durham_long = pd.DataFrame(durham.iloc[0]).rename(columns = {0 : 'name'})

durham_expand = durham_long['name'].str.split('!!', 1, expand = True)

durham_expand['value'] = durham.iloc[1]

durham_expand['var'] = durham.columns

durham_no_heading = durham_expand.drop(['GEO_ID','NAME'],axis = 0).rename(columns = {0 : 'stat', 1: 'label'})

durham_no_heading['index'] = durham_no_heading['var'].str[0:9]
                  
durham_est = durham_no_heading.pivot(index = 'index', columns = 'stat', values = 'value').rename_axis(None, axis=1).reset_index()

durham_label = durham_no_heading[['index','label']].drop_duplicates()

durham_level = durham_label['label'].str.split('!!', expand = True)

durham_level['index'] = durham_label['index']

durham_merge = durham_level.merge(durham_est, on = 'index', how = 'left')


## Attach column names
durham_merge.columns = ['lev1','lev2','lev3','lev4','lev5',durham_merge.columns[5],durham_merge.columns[6],'Percent Estimate']


## Process and output sex and age data 
durham_sex_age_ = durham_merge[durham_merge['lev1'] == 'SEX AND AGE']

durham_age = durham_sex_age_.iloc[4:18,[2,5,6,7]]

durham_sex = durham_sex_age_.iloc[1:3,[2,5,6,7]]

durham_sex.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_sex.csv',index=False)


durham_age.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_age.csv',index=False)

## Process and output race data 
durham_race_ = durham_merge[durham_merge['lev1'] == 'RACE']

durham_race_ = durham_race_.iloc[:,[3,5,6,7]]

durham_race_ = durham_race_[durham_race_['index'].str.contains('37|38|39|44|52|57|58')]

race_other = pd.Series(['Other', ' ', sum(pd.to_numeric(durham_race_['Estimate'][-2:].iloc[-2:])),
                        sum(pd.to_numeric(durham_race_['Percent Estimate'][-2:].iloc[-2:]))],
                      index = durham_race_.columns)

durham_race = durham_race_.append(race_other,ignore_index=True).drop([5,6])

durham_race.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_race.csv',index=False)


## Process and output ethnicity data
durham_ethnicity_ = durham_merge[durham_merge['lev1'] == 'HISPANIC OR LATINO AND RACE']

durham_ethnicity_ = durham_ethnicity_[durham_ethnicity_['index'].str.contains('71|76')]

durham_ethnicity = durham_ethnicity_.iloc[:,[2,5,6,7]]

durham_ethnicity.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_ethnicity.csv',index=False)


## Process and output veteran data
durham_veteran_ = durham_merge[durham_merge['lev1'] == 'VETERAN STATUS']
durham_veteran_ = durham_veteran_.iloc[:,[2,5,6,7]]
veteran_non = pd.Series(['Non veteran', ' ', 
                         pd.to_numeric(durham_veteran_['Estimate'].iloc[0]) - 
                         pd.to_numeric(durham_veteran_['Estimate'].iloc[1]),
                         100 - pd.to_numeric(durham_veteran_['Percent Estimate'].iloc[1])],
                        index = durham_veteran_.columns)

durham_veteran = durham_veteran_.append(veteran_non,ignore_index=True).drop(0)

durham_veteran.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_veteran.csv',index=False)

 
## Process and output disability data
# durham_disability_ = durham_merge[durham_merge['lev1'].str.contains('DISABILITY')]
# durham_disability_
# durham_disability.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/durham_disability.csv',index=False)
 

 
# 2. Client data
## Read in raw client data from UMD
client_raw = pd.read_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/raw/CLIENT_191102.tsv.txt', sep='\t')

## Select only variables that will be used in the analysis
client = client_raw.iloc[:,2:10]

## Remove the string '(HUD)' from variables
for i in [5,6,7]:
    client.iloc[:,i] = client.iloc[:,i].str.rstrip('(HUD)')

## Categorize age according to the cutoffs of local demographic data
age_cut = [0,4,9,14,19,24,34,44,54,59,64,74,84,100]

age_label = durham_age.iloc[0:13,0]

client['age_cat'] = pd.cut(client['Client Age at Entry'], age_cut, labels = age_label)


## Categorize race according to the levels of of local demographic data
## Note that the 'Other' category in the ACS dataset correspond to other races or belonging to 2 races, 
## but the 'Other' in the UMD data corresponds to 'Client doesn't know'. Clients with race values of 
## 'Client refused', and 'Data not collected' will not be included when comparing UMD and local populations.
race_dic = {'White': 'White', 
            'Black or African American': 'Black or African American', 
            'American Indian or Alaska Native':'American Indian and Alaska Native', 
            'Asian': 'Asian',
            'Native Hawaiian or Other Pacific Islander': 'Native Hawaiian and Other Pacific Islander',
            "Client doesn't know": 'Other'}

client['race_cat'] = client['Client Primary Race'].str.strip()

client['race_cat'].replace(race_dic, inplace = True)


## Categorize ethnicity according to the levels of of local demographic data

ethnicity_dic = {'Non-Hispanic/Non-Latino': 'Not Hispanic or Latino',
                 'Hispanic/Latino': 'Hispanic or Latino (of any race)'}

client['ethnicity_cat'] = client['Client Ethnicity'].str.strip()

client['ethnicity_cat'].replace(ethnicity_dic, inplace = True)

## Categorize veteran status according to the levels of of local demographic data 
## (only look at subjects 18 years old and over at entry)

veteran_dic = {'Yes': 'Civilian veteran', 'No': 'Non veteran'}

for i, row in client.iterrows():
    if client['Client Age at Entry'].iloc[i] >= 18:
        client['veteran_cat'] = client['Client Veteran Status'].str.strip()
        client['veteran_cat'].replace(veteran_dic, inplace = True)

## Output the client dataset
client.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/client.csv',index=False)

# 3. Disability data
## Read in raw disability at entry dataset
disability_entry_raw = pd.read_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/raw/DISABILITY_ENTRY_191102.tsv.txt', sep='\t')

## Keep only variables relevant to analysis
disability_entry = disability_entry_raw.iloc[:,2:8]

## Remove the string '(HUD)' from variables
for i in [2,3]:
    disability_entry.iloc[:,i] = disability_entry.iloc[:,i].str.rstrip(' (HUD)')
    
## Output subject-level disability entry dataset
disability_entry.to_csv('Documents/GitHub/bios611-projects-fall-2019-yench/project_3/data/analysis/disability_entry_subject.csv',index=False)

## Create an indicator for disability        
for i in range(0, len(disability_entry)):
    disability_entry['disability_ind'] = (disability_entry['Disability Determination (Entry)'] == 'Yes')
    
## For each subject, obtain their disability status ('With a disability' if at least one record of disability during the duration of the dataset)
disability_ind2 = disability_entry.groupby(['Client Unique ID']).agg('sum') 
disability_ind2['disability_total'] = pd.cut(disability_ind2.iloc[:,1], [-1,0,150], labels = ['Without a disability','With a disability'])

### If intersted in the first or last entry rather than all, the following code yields the disability status at each date of entry
### disability_entry['entry_date'] = pd.to_datetime(disability_entry['Disability Start Date (Entry)'])
### disability_entry.groupby(['Client Unique ID','entry_date']).agg('sum')
