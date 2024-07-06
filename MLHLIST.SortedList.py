#  Created by BrodyDanger
# 7.5.2024
# Global Hack Week Season Launch 2025 
# Sorting list of hackathons Challenge

# Import libraries

import pandas as pd 
#Sort Names
datalist = pd.read_csv('List of Hackathon Names - Sheet1.csv') # Read in csv
datalist['Start Date'] = pd.to_datetime(datalist['Start Date'])
datalist['End Date'] = pd.to_datetime(datalist['End Date'])
namessortedlist = datalist.sort_values(by=['Name','Start Date','End Date']) # Sort by name, start date, end date
namessortedlist.to_csv('MLHNameSorted.csv',index=False) # Write to sorted file
print("complete")
