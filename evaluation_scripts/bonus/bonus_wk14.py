


# %%
from datetime import datetime
from matplotlib.pyplot import xticks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import eval_functions as ef
import dataretrieval.nwis as nwis


# %%
station_id = "09506000"
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)
print('all students:', firstnames)

# Listing everyone who already attained points this week
points = ['Tong', 'Jessica', 'Jessi', 'Dave', 'Nathan'] 
evaluators = ['Claire', 'Lauren', 'Nathan']
print('already receieved points this week:', points)
print('evaluators:',evaluators)


#%%
# Read in everyone's forecast entries
forecasts1 = np.zeros(nstudent)  # 1 wk forecasts for this week
forecasts2 = np.zeros(nstudent)  # 2 wk forecasts for this week
filepath1 = os.path.join('..','weekly_results','forecast_week3_results.csv')

#%%
def predct_obsrvd_difference(start_week):
    forecasts_end1 = np.zeros(nstudent)  # 1 wk forecasts for this week
    output = []
    
    for i in range(nstudent):
        filename = names[i] + '.csv'
        filepath = os.path.join('..', 'forecast_entries', filename)
        temp = pd.read_csv(filepath, index_col='Forecast #')
        forecasts_end1[i] = temp.loc[(start_week), '1week']
        output.append(forecasts_end1[i])

    frcst_filepath = os.path.join('..','weekly_results',f'forecast_week{start_week}_results.csv')
    obsrvd = pd.read_csv(frcst_filepath).iloc[1,3]
    diff = np.abs(output - obsrvd) 
    diff_df = pd.DataFrame({'Difference': diff})
    return(diff_df)

wk3_df = predct_obsrvd_difference(3)
wk14_df = predct_obsrvd_difference(14)

improve = (wk3_df - wk14_df)
improve[np.isnan(improve)] = 0
#%%
names = pd.read_csv(filepath1)
diff_df = pd.DataFrame({'name': names['name'], 'Difference': improve['Difference']})
diff_df = diff_df.sort_values(by='Difference', ascending=False)
print(diff_df)

#%%
# Initialize an array to store the selected names
bonus = []

# Loop through the sorted DataFrame to select names
for index, row in diff_df.iterrows():
    name = row['name']
    
    # Check if the name is not in 'points' and 'evaluators' arrays
    if name not in points and name not in evaluators:
        bonus.append(name)
    
    # Break the loop when 3 names are selected
    if len(bonus) == 3:
        break

print('Bonus points:', bonus)

# %%
