


# ===============  duplicate rows ================

# Check total duplicate rows
# print("Duplicate rows count:", df.duplicated().sum())

# Drop duplicates (inplace or reassign)
# df = df.drop_duplicates()




# ================ Missing Values ===============

# 1. 
# Drop rows containing any NaN value
# df_clean = df.dropna()

import numpy as np
import pandas as pd

null_data = {
    'A' : [1,2,np.nan, 3],
    'B' : [np.nan,2,np.nan, 3],
    'C' : [1,2,np.nan, np.nan],
    'D' : [1,2,4,9],
}

# Missing Data

# df.isna() -> it will print the data frame in true false values
# df.isna().sum -> it will add all the no of null values


df = pd.DataFrame(null_data)
# print(df.isna().sum()) 

# if we want to drop the rows that has null values, use dropna()

# print(df.dropna())


# Filling NUll values

# fill with zero
df = df.fillna(df.mean())
# df = df.fillna(0, inplace = True) # -> fill with 0
print(df)