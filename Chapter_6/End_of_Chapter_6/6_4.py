# Done by Carlos Amaral (2020/10/11)

import pandas as pd

gss_df = pd.read_csv('GSS1993_9Fields.csv')

# Create a Panda Series Object from HAPPY column
happiness_flag = gss_df.HAPPY

# New DataFrame
happiness_flag.loc[(happiness_flag.HAPPY < 3)] = 1
happiness_flag.loc[(happiness_flag.HAPPY >= 3)] = 0

print(happiness_flag.HAPPY.value_counts(sort=False))

