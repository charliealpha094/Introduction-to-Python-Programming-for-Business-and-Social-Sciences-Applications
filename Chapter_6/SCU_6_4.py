# Done by Carlos Amaral (2020/10/05)

# SCU 6.4 - Reporting Information about Data in a Pandas DataFrame

import pandas as pd

results_df = pd.read_json("Taxi_Trips.json")


print("The description is: ", results_df.describe())

print("\nThe median is: ", results_df.median())