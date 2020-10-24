# Done by Carlos Amaral (2020/10/11)

import pandas as pd

gss_df = pd.read_csv('GSS1993_HealthAndMaritalRecoded.csv')
print("Before removing a few columns:", gss_df)

# Remove all columns except HEALTH and EDUC
gss_df.drop('SEX', axis=1, inplace=True)
gss_df.drop('TRAUMA1', axis=1, inplace=True)
gss_df.drop('DIVORCED', axis=1, inplace=True)
gss_df.drop('WIDOWED', axis=1, inplace=True)
gss_df.drop('AGE', axis=1, inplace=True)
gss_df.drop('SEPARATED', axis=1, inplace=True)
gss_df.drop('NEVER_MARRIED', axis=1, inplace=True)
gss_df.drop('RACE', axis=1, inplace=True)
gss_df.drop('UNHAPPY', axis=1, inplace=True)
gss_df.drop('RINCOM91', axis=1, inplace=True)






print("After removing:", gss_df)

gss_df.to_csv('GSS1993_NewHealth.csv')

