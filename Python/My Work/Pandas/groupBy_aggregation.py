import pandas as pd, numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}

df = pd.DataFrame(data)

# print(df)

# # Groupby category and calculate the sum of sales
# # there are two categories, so 2 answers will be there. 1 for A, and 1 for B
# print(df.groupby('Category')['Sales'].sum())


# groupby store and calculate the sum of sales
# print(df.groupby('Store')['Sales'].sum())



# # groupby by category and sales
# print(df.groupby(['Store','Category'])['Sales'].sum()) # -> pehly store ko categorize krega, then S1 and S2 ke liye A and B alag alag krega
# print(df.groupby(['Category','Store'])['Sales'].sum()) # -> pehly Category ko categorize krega, then A nd B ke liye S1 and S2 alag alag krega









# ================= Aggregation =============
# multiple cheezo ko aik sath combine krky answer nikalna chahty ho
# mean, median, mode, std, 

# function -> .agg

print(df["Sales"].agg(['mean', 'max', 'min', 'count','std','median']))