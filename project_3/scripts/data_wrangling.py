## This python script imports raw datasets, wrangles, and writes analysis datasets for further analysis in R.

## Input: ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv
##		  ACS_17_5YR_B21001_with_ann.csv
##        ACS_17_5YR_S1810_with_ann.csv
##        CLIENT_191102.tsv.txt
##        DISABILITY_ENTRY_191102.tsv.txt  

## Output: client.csv
##         summary_sex.csv
##		   summary_age.csv
##		   summary_race.csv
##		   summary_ethnicity.csv
##		   summary_veteran.csv
##		   durham_disability.csv
##         disability_entry_subject.csv
##         disability_entry_summary.csv


import pandas as pd
import numpy as np

## Read in raw demographic datasets from US Census Bureau
durham_raw_sar = pd.read_csv('data/raw/ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv')

durham_raw_v = pd.read_csv('data/raw/ACS_17_5YR_B21001_with_ann.csv')

durham_raw_d = pd.read_csv('data/raw/ACS_17_5YR_S1810_with_ann.csv')

# 1. Process the table containing sex, age and race (SAR) information
## Only keep population estimates and percent estimates (discard margins of error)
mask1 = durham_raw_sar.iloc[0].str.contains('Estimate').values

durham_sar = durham_raw_sar.iloc[0:2, mask1]

## Reshape SAR table 
durham_sar_long = pd.DataFrame(durham_sar.iloc[0]).rename(columns = {0 : 'name'})    # Transpose the table from wide to long

durham_sar_expand = durham_sar_long['name'].str.split('!!', 1, expand = True)  

durham_sar_expand['value'] = durham_sar.iloc[1]

durham_sar_expand['var'] = durham_sar.columns

durham_sar_expand = durham_sar_expand.rename(columns = {0 : 'stat', 1: 'label'})

durham_sar_expand['index'] = durham_sar_expand['var'].str[0:9]

durham_sar_est = durham_sar_expand.pivot(index = 'index', columns = 'stat', values = 'value').rename_axis(None, axis=1).reset_index()

durham_sar_label = durham_sar_expand[['index','label']].drop_duplicates()

durham_sar_level = durham_sar_label['label'].str.split('!!', expand = True)

durham_sar_level['index'] = durham_sar_label['index']

durham_sar_merge = durham_sar_level.merge(durham_sar_est, on = 'index', how = 'left')

durham_sar_merge.columns = ['lev1','lev2','lev3','lev4','lev5',durham_sar_merge.columns[5],durham_sar_merge.columns[6],'Percent Estimate']

durham_sar_merge.head()

## Process sex and age data 
durham_sex_age_ = durham_sar_merge[durham_sar_merge['lev1'] == 'SEX AND AGE']

durham_age = durham_sex_age_.iloc[4:17,[2,5,6,7]]

durham_sex = durham_sex_age_.iloc[1:3,[2,5,6,7]]


## Process race data 
durham_race_ = durham_sar_merge[durham_sar_merge['lev1'] == 'RACE']

durham_race_ = durham_race_.iloc[:,[3,5,6,7]]

durham_race_ = durham_race_[durham_race_['index'].str.contains('37|38|39|44|52|57|58')]

race_other = pd.Series(['Other', ' ', sum(pd.to_numeric(durham_race_['Estimate'][-2:].iloc[-2:])),
                        sum(pd.to_numeric(durham_race_['Percent Estimate'][-2:].iloc[-2:]))],
                      index = durham_race_.columns)

durham_race = durham_race_.append(race_other,ignore_index=True).drop([5,6])

## Process ethnicity data
durham_ethnicity_ = durham_sar_merge[durham_sar_merge['lev1'] == 'HISPANIC OR LATINO AND RACE']

durham_ethnicity_ = durham_ethnicity_[durham_ethnicity_['index'].str.contains('71|76')]

durham_ethnicity = durham_ethnicity_.iloc[:,[2,5,6,7]]

# 2. Process and reshape the veteran table
mask2 = durham_raw_v.iloc[0].str.contains('Estimate').values

durham_v = durham_raw_v.iloc[0:2, mask2]

durham_v_long = pd.DataFrame(durham_v.iloc[0]).rename(columns = {0 : 'name'})    # Transpose the table from wide to long

durham_v_sub = durham_v_long.iloc[1:3]       # Only keep a subset of data relevant to this analysis

durham_veteran = durham_v_sub['name'].str.split('- ', 1, expand = True)

durham_veteran = durham_veteran.rename(columns = {1 : 'level'})

durham_veteran['index'] = durham_v.columns[1:3]

durham_veteran['Estimate'] = durham_v.iloc[1,1:3]

durham_veteran = durham_veteran.iloc[:,1:4]

durham_veteran['Percent Estimate'] = pd.to_numeric(durham_veteran['Estimate'])*100 / float(durham_v.iloc[1,0])

# 3. Process, reshape, and output disability data
mask3 = durham_raw_d.iloc[0].str.contains('Estimate').values

durham_d = durham_raw_d.iloc[0:2, mask3]  

durham_disability = pd.DataFrame({'level': ['With a disability', 'Without a disability'],
                                  'index' : [durham_d.columns[0],''],
                                  'Estimate' : [float(durham_d.iloc[1,1]), float(durham_d.iloc[1,0]) - float(durham_d.iloc[1,1])], 
                                  'Percent Estimate' : [float(durham_d.iloc[1,2]), 100 - float(durham_d.iloc[1,2])]})

durham_disability = durham_disability[['level', 'index', 'Estimate', 'Percent Estimate']]

durham_disability = durham_disability.to_csv('data/analysis/durham_disability.csv',index=False)

# 4. Client data
## Read in raw client data from UMD
client_raw = pd.read_csv('data/raw/CLIENT_191102.tsv.txt', sep='\t')

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

veteran_dic = {'Yes': 'Veteran', 'No': 'Nonveteran'}

for i, row in client.iterrows():
    if client['Client Age at Entry'].iloc[i] >= 18:
        client['veteran_cat'] = client['Client Veteran Status'].str.strip()
        client['veteran_cat'].replace(veteran_dic, inplace = True)

## Output the client dataset
client.to_csv('data/analysis/client.csv',index=False)

# 5. Merge summary data from UMD and ACS. Output to CSV file for further analysis in R.

## Construct a function to merge summary data (counts and percents) from UMD and from ACS 
def merge_summary(durham_in,            # input dataset (eg. durham_sex)
                  level_in_durham,      # level variable in the input dataset (eg. 'lev3')
                  var_in_client,        # corresponding variable name in the client dataset (eg. 'Client Gender')
                  out):                  # output dataset (eg. 'sex' - > sex_summary.csv)

    ### Create client summary data on the variable specified
    client_summary = pd.DataFrame(client.groupby(var_in_client, as_index = False).size().reset_index(name='count'))

    client_summary.rename(columns = {var_in_client: 'level'}, inplace = True)

    client_summary['percent'] = client_summary['count']/client_summary['count'].sum()*100

    client_summary['source'] = 'UMD'

    ### Reshape Durham summary data on the variable specified
    acs = durham_in[[level_in_durham, 'Estimate', 'Percent Estimate']]

    acs.columns = ['level','count','percent']

    acs['source'] = 'Duhram'

    ### Merge the client summary dataset and Durham summary dataset vertically
    summary = pd.concat([client_summary, acs], ignore_index=True)

    ### Output csv file
    summary.to_csv('data/analysis/summary_'+ out + '.csv',index=False)
	
## Output sex summary data
merge_summary(durham_in = durham_sex, level_in_durham = 'lev3', var_in_client = 'Client Gender', out = 'sex')

## Output age summary data
merge_summary(durham_in = durham_age, level_in_durham = 'lev3', var_in_client = 'age_cat', out = 'age')

## Output race summary data
merge_summary(durham_in = durham_race, level_in_durham = 'lev4', var_in_client = 'race_cat', out = 'race')

## Output ethnicity summary data
merge_summary(durham_in = durham_ethnicity, level_in_durham = 'lev3', var_in_client = 'ethnicity_cat', out = 'ethnicity')

## Output veteran summary data
merge_summary(durham_in = durham_veteran, level_in_durham = 'level', var_in_client = 'veteran_cat', out = 'veteran')

# 6. Disability data
## Read in raw disability at entry dataset
disability_entry_raw = pd.read_csv('data/raw/DISABILITY_ENTRY_191102.tsv.txt', sep='\t')

## Keep only variables relevant to analysis
disability_entry = disability_entry_raw.iloc[:,2:8]

## Remove the string '(HUD)' from variables
for i in [2,3]:
    disability_entry.iloc[:,i] = disability_entry.iloc[:,i].str.rstrip(' (HUD)')
    
## Output subject-level disability entry dataset
disability_entry.to_csv('data/analysis/disability_entry_subject.csv',index=False)

## Create an indicator for disability        
for i in range(0, len(disability_entry)):
    disability_entry['disability_ind'] = (disability_entry['Disability Determination (Entry)'] == 'Yes')
    
## For each subject, obtain their disability status ('With a disability' if at least one record of disability during the duration of the dataset)
disability_ind2 = disability_entry.groupby(['Client Unique ID']).agg('sum') 
disability_ind2['disability_total'] = pd.cut(disability_ind2.iloc[:,1], [-1,0,150], labels = ['Without a disability','With a disability'])

### If intersted in the first or last entry rather than all, the following code yields the disability status at each date of entry
### disability_entry['entry_date'] = pd.to_datetime(disability_entry['Disability Start Date (Entry)'])
### disability_entry.groupby(['Client Unique ID','entry_date']).agg('sum')

disability_ind2['Client Unique ID'] = disability_ind2.index
disability_ind2 = disability_ind2.iloc[:,1:4]
disability_ind2.to_csv('data/analysis/disability_entry_summary.csv',index=False)



