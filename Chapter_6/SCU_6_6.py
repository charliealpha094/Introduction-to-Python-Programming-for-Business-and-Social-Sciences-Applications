# Done by Carlos Amaral (2020/10/10)

# SCU 6.6 - Creating Dummy Variables

import pandas as pd

survey_df = pd.read_csv("survey_df_cleaned.csv")

# Dummy is nineties have a value of True when YEAR is in the 1990's (and False otherwise)
survey_df["dummy_is_nineties"] = (survey_df["YEAR"] >= 1990) & (survey_df["YEAR"] <= 1999)


# Converts our True/False flag to integer (1 or 0)
survey_df["dummy_is_nineties"] = survey_df["dummy_is_nineties"].astype(int)

# Write to a new csv file
survey_df.to_csv("survey_df_cleaned_with_dummy_variable.csv", index=False)

