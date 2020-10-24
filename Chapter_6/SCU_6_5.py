# Done by Carlos Amaral (2020/10/10)

# SCU 6.5 - Replacing multilple values in one step

import pandas as pd

survey_df = pd.read_csv("survey_df_less_columns.csv")

survey_df_cleaned = survey_df.loc[(survey_df["SIBS"] > -1)]
survey_df_cleaned = survey_df.loc[survey_df["SIBS"] < 98]
survey_df_cleaned = survey_df.loc[survey_df["SIBS"] < 99]
survey_df_cleaned = survey_df.loc[survey_df["HRS1"] != -1]

# Write clean data to .csv file:
survey_df_cleaned.to_csv("survey_df_cleaned.csv", index=False)

