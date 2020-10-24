# Done by Carlos Amaral (2020/10/04)

# SCU 6.3 - Modify Structure of DataFrame Changing Columns

import pandas as pd 
results_df = pd.read_json("Trips from area 8.json")

print("Original set of columns: ", results_df.columns)

results_df = results_df[['trip_miles', 'trip_seconds']]



print("After reduciong columns: ", results_df.columns)