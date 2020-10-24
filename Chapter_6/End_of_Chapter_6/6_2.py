# Done by Carlos Amaral (2020/10/10)

import pandas as pd

ages = [26,33]
names = ['Carlos', 'Patricia']


df = pd.DataFrame({'names': names, 'ages': ages})

print(df)

print("\n", df.describe())



