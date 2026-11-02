"""
Intro:
    Pandas is a open source py lib for working with structured data such as tables, spreadsheets, CSV files, and database like records. 

    Two main data structures are:
    1. Series: stores 1D labeled data
    2. DataFrame: stores data in rows and columns

    Provides tools like: load, inspect, clean, filter, transform, summarize, group, and transform datasets.

    Used is Data Science, research, business analytics, and machine learning workflows. 

"""

# To install -> python -m pip install pandas
# for reading and writing Excel (.xlsx) files, install -> python -m pip install openpyxl


import pandas as pd

# print(pd.__version__) # check version



# ============== PANDAS DATA STRUCTURES ============

# ------- Why we use Pandas if we have np.array() ----
# A NumPy array is purely a grid of raw numbers, whereas a pandas Series is data with context (labels + data type).
# In NumPy, array[0] gives you 78. But what does 78 belong to? In pandas, you can assign custom row labels. We can label that element by our own word like we do in dict
# Pandas handles missing values (NaN) properly



# ========================= 1. Series (1D) ======================

# Series with default labels
marks = pd.Series([78, 85, 92, 67])
# print(marks)
# Unlike Numpy, pandas series pairs every element with its index (the label)

# Series with custom labels:
marks = pd.Series([78, 85, 92], index=["Ali", "Sara", "Ahmed"])
# print(marks)

# print(marks["Sara"])

# We are working with lists, if we talk about dict, the keys will become labels and the values will become data. 


# ========== Series Attributes and calculations ==========
scores = pd.Series([70, 80, 90, 100])
# print(scores.index)  # -- print the index
# print(scores.values) # -- will only give values, except the indexes
# print(scores.dtype)  # -- will print its data type
# print(scores.size)   # -- give no of elements in this series
# print(scores.mean()) # -- mean of this series
# print(scores.max())  # -- max value in this series
# print(scores.min())  # -- min value in this series
# print(scores.sum())  # -- sum of the values of this series

# .index --> it returns the labels associated with each element in series or data frame. When we don't explicitly pass custom labels, pandas saves memory by generating a 'RangeIndex' instead of storing every single index number. 
# Output --> RangeIndex(start=0, stop=4, step=1)

# We can convert it into a list:
index_list = list(scores.index)
# print(index_list)

# If we pass custom labels, it will print them
marks = pd.Series([78, 85, 92], index=["Ali", "Sara", "Ahmed"])
# print(marks.index)

# ---------- Date and Time Labels (DatetimeIndex) --------
# When working with time-series data, pandas uses a dedicated timestamp index:
dates = pd.date_range(start='2026-01-01', periods=3)
s = pd.Series([100, 102, 105], index = dates)
# print(s.index)


# ======================== 1. DataFrame (2D) =====================

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', "Noor"],
    'Age':[21, 22, 20, 23],
    'Department':["CS", "IT", 'CS', 'AI'],
    'Marks':[78, 92, 67, 88]
}

# Here we are dealing with a dictionary of 4 keys - Pandas converts each dictionary key into a column Header, and corresponding list of values becomes the data rows under that column
# It is 4x4 matrics, with an extra col of indices

df = pd.DataFrame(data)
# print(df)

# ----- Ways to create DataFrames ---

# 1. Dictionary of lists:
data = {
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Age': [21, 22, 20]
}
df = pd.DataFrame(data)


# 2. List of Dictionaries
students = [
    {'Name':'Ali', 'Marks':78},
    {'Name':'Sara', 'Marks':98},
]
df = pd.DataFrame(students)


# 3. List of Lists
rows = [
    ['Ali', 78], 
    ['Sara', 98]
]
df = pd.DataFrame(rows, columns=['Name', 'Marks'])


# 4. From Pandas Series
names = pd.Series(['Ali', 'Sara', 'Ahmed'])
marks = pd.Series([78, 92, 98])

df = pd.DataFrame({'Name':names, 'Marks':marks})



# ----------- .set_index() -----------
# It replaces the current row index with one or more existing columns
# For example: I want the indexing of students along with their roll no, then set_index() will make the indexing along the roll no. 

students = {
    'Roll No':[101, 102, 103, 104],
    'Name': ['Ali', 'Sara', 'Ahmed', "Noor"],
    'Age':[21, 22, 20, 23],
    'Department':["CS", "IT", 'CS', 'AI'],
    'Marks':[78, 92, 67, 88]
}

# Accessing the columns

df = pd.DataFrame(students)

# print(df["Name"]) # single col
# print(df["Name"][0]) # a single element
# print(df[["Name", "Roll No"]])


# deleting a col or row, if we pass axis=0, it will delete the row, and if we pass axis=1, it wil delwte the col.
df = df.drop("Age", axis=1)
# print(df)

df_roll = df.set_index("Roll No")
# print(df_roll)
# So if i want indexing along an specific col, i will use df.set_index('col name') 

# we can also reset the index to normal by using : .reset_index()


# ========= Inspecting a DataSet ===============

# print(df.head())  # at default will print first 5 rows - we can pass custom no of rows
# print(df.tail())  # at default will print last 5 rows - we can pass custom no of rows
# print(df.shape)   # tuple of rows and cols (rows, cols)
# print(df.columns) # gives columns
# print(df.index)   # gives indexes along a single row
# print(df.dtypes)
# df.info()
# print(df.describe())
# print(df.describe(include='all')) # -- it will cover every aspect


# ==== df.info() ====
# Ye pury DataFrame ki short summary/overview deta hy
# You get to know that how many rows, cols, missing values are there, and which datatypes are there -- also tells us about memory usage

# ====df.describe() ====
# df.describe() pandas ka statistical summary tool hai. Yeh aapke DataFrame ke numeric columns ka numerical inspection (mean, median, min, max, etc.) automatically calculate karke ek hi table me dikha deta hai.







# =========== Loading and Saving Data ========

df_csv = pd.read_csv("customers-100.csv")
# print(df_csv.head())

# Common parameters:
# df = pd.read_csv(
#     filepath_or_buffer='students.csv',
#     sep=',', --- values ko separate krny wla character
#     header=0,
#     index_col='Student_ID',
#     usecols=['Student_ID', 'Name', 'Marks'],
#     nrows=100,
#     na_values=['N/A', 'Missing']
# )


df_excel = pd.read_excel('SampleData.xlsx')
# If you do not pass sheet_name, pandas will simply load the very first sheet (index 0) of the Excel workbook by default.

# Commonly used parameters:
# df = pd.read_excel(
#     io='students.xlsx',
#     sheet_name='Sheet1', -- knosi sheet read krni hy?
#     header=0,
#     skiprows=2, -- start ki kitni rows ko skip krna hy
#     usecols='A:C' -- kitny cols tak kaam krna hy
# )

#  We can read selected cols and rows using: usecols - cols in csv, and nrows - rows in csv



# ======= Exporting Data back to csv or excel =========

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Noor'],
    'Age': [21, 22, 20, 23],
    'Department': ['CS', 'IT', 'CS', 'AI'],
    'Marks': [78, 92, 67, 88]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('students_output.csv', index=False) 
# By default, pandas writes indexes as well, so to get rid of them we use index = False

# Save to Excel
df.to_excel('students_output.xlsx', sheet_name='Students_Data', index=False)


# If you want to save multiple DataFrames into different sheets of the same Excel file:
cs_df = df[df['Department'] == 'CS']
it_df = df[df['Department'] == 'IT']

with pd.ExcelWriter('department_report.xlsx') as writer:
    cs_df.to_excel(writer, sheet_name='CS_Students', index=False)
    it_df.to_excel(writer, sheet_name='IT_Students', index=False)



# ===== loc and iloc =====

# used to select specific rows and cols from a dataframe
# .loc -- label-based (uses index names and col names)
# .iloc -- integer position-based (0-based index positions)

# df.loc[row_selection, column_selection]
# df.iloc[row_selection, column_selection]

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4'])

# print(df.loc['S3', 'Name']) # if we don't select col, it will give complete data of the S3 index
# print(df.loc[['S2', 'S4'], ['Name', 'Department']]) # it will give their names and relative departments

# ======= Slicing with .loc
# print(df.loc['S1':'S3', 'Name':'Department']) # select s1 till s3, and from name to department col

# print(df.iloc[1]) # data of student at index 1

# Rows at positions 0 and 2, columns at positions 0 and 3
# print(df.iloc[[0, 2], [0, 3]])

# From row position 0 to 3 (position 3 is NOT included -> gets 0, 1, 2) ---- Slicing
# print(df.iloc[0:3, 0:3])



# ======== Filtering Rows ====
# Boolean filtering keeps rows that meet a condition.

high_marks = df[df["Marks"] > 80] # it will select the students whose marks are greater than 80 and label them true

# AND (&) : Both conditions must be true:
cs_high = df[(df['Department'] == 'CS') & (df['Marks'] >= 75)]

# OR (|) : either condition maybe true
selected = df[(df['Department'] == 'CS') | (df['Marks'] >= 75)]

# NOT (~) : reverse a condition
not_cs = df[~(df['Department'] == "CS")]

# Match any listed value: -- will give the students who are in any of the departments
chosen = df[df['Department'].isin(['CS','AI'])] 
# print(chosen)

# Inclusive Range
mid_scores = df[df['Marks'].between(70,90)]

# Missing and known values:
missing_marks = df[df['Marks'].isna()]  #-- it will check whether the dataframe contains missing values
# print(missing_marks)

known_marks = df[df['Marks'].notna()] # -- will print data of students whose marks are available 
# print(known_marks)



data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Noor'],
    'Age': [21, 22, 20, 23],
    'Department': ['CS', 'IT', 'CS', 'AI'],
    'Marks': [78, 92, 67, 88]
}

df = pd.DataFrame(data)

# selecting cols
# print(df["Name"]) # single col
# print(df[["Name", "Age"]]) # multiple cols

# selecting rows
# we mke use of loc and iloc
# print(df.loc[0])

# selecting a portion
# print(df.iloc[2:,0:2])  # same as numpy

# print(df[(df["Age"]>20) & (df["Marks"]>80)])


import numpy as np

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