# %% 
import sys
import pandas as pd
sys.path.insert(1, '../')
import eval_functions as ef
import numpy as np
# %%
# Name: Laura Condon 
# Description: Assigning bonus points to the people with the largest differences in their week 1 forecast from observations 
weeknum = 10

all_names = ef.getFirstNames()
print('Everyone:', all_names)
print()

#make a list of all the people who got points this week
points_list = ['Tong', 'Nathan', 'Dave', 'Jessica']
print('People getting points already:', points_list)
print()

# Make a list of the names of people not getting points
# Example with a list comprehension
nopoints_list = [name for name in all_names if name not in points_list]

#Read in the forecast results for this week
fcst_results = pd.read_csv('../../weekly_results/forecast_week10_results.csv', index_col='name')

#Grab out just the people who are not receiving points already 
nopoint_results = fcst_results.loc[nopoints_list]

#
difference = np.abs(nopoint_results["1week_forecast"]-nopoint_results["2week_forecast"])

#Sort by the differences largest to smallest, grab out the first three index values
sorted_differences = difference.sort_values(ascending=False)

#Choose the top 3 differences to get  points
bonus_names = sorted_differences.iloc[0:3,].index

print("People Getting bonus points:", bonus_names)
print()

#Write out the bonus points
#ef.write_bonus(bonus_names, all_names, weeknum)            #UNCOMMENT

# %%
