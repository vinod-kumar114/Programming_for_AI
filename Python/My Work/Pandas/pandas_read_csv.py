import pandas as pd

file = pd.read_csv('patients.csv')

#  if we need specific columns
# file = pd.read_csv('patients.csv', usecols=['Age', 'ID'])
# print(file)

# print(file.info())
# file = file.drop("ID", axis=1)
# print(file.drop("ID", axis=1).describe())  # -> sum, std, mean


# changing name of cols
file.columns = ['Col1', 'Col2', 'Col3', 'Col4']
# print(file)

# changing name of specific col
file.rename(columns={"Col1":"ID"}, inplace=True)
# print(file)
file.rename(columns={"Col2":"Age"}, inplace=True)
# print(file)
file.rename(columns={"Col3":"Glucose"}, inplace=True)
# print(file)
file.rename(columns={"Col4":"Diabetes"}, inplace=True)
# print(file)



# ==========================================
# 1. ADDING NEW COLUMNS
# ==========================================


# df.insert(loc, column_name, value, allow_duplicates=False)


# ==========================================
# 1. ADDING NEW ROWS
# ==========================================

# for single row
file.loc[4] = [5,25,178,0]
print(file)

# for multiple rows, make another data frame and use concat method

# concat method
# pd.concat([df1, df2, df3], axis=0, ignore_index=False)




# ========== loc & iloc ==============

# .loc (Label-Based): Custom names/labels use karta hai. Slice ranges mein end index include hota hai.

# .iloc (Integer Position-Based): Zero-based integer positions (0, 1, 2...) use karta hai. Slice ranges mein end index exclude hota hai (Python standard slicing ki tarah).