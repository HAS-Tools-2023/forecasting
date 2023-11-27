#%%
import numpy as np
import pandas as pd
import sys
sys.path.insert(1, '../')
import eval_functions as ef
import numpy as np

#%%
# Name: Jess and Rob's Bonus Points Script
# Description: Assigning bonus points with a random choice function.
weeknum = 12

# Listing everyone's first names
first_names = ef.getFirstNames()
print('Everyone:', first_names)
print()

# Listing everyone who already attained points this week
points = ['Tong', 'Jessica', 'Jessi', 'Lauren', 'Nathan'] 
print('Those who already attained points:', points)
print()

# Listing everyone who did not attain points yet this week
no_points = [name for name in first_names if name not in points]


#%%
# Using the numpy library to randomly select names of those who did not attain points, for the bonus points
random_names = np.random.choice(no_points, 3, replace=False)

print('Forecast Bonus Week 1:', random_names)


#Write out the bonus points
ef.write_bonus(random_names, first_names, 12)


# %%
