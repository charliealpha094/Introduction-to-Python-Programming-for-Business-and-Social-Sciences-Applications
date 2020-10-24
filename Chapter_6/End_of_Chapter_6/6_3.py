# Done by Carlos Amaral (2020/10/10)


import pandas as pd

# Build a DataFrame from a json file
trips = pd.read_json('Trips by pickup area.json')

# Remove Pick_up Areas with value of NaN or count_trip < 1000
trips = trips[trips.count_trip_seconds < 1000]
print("After removing: ", trips['count_trip_seconds'].count())

print(trips)

