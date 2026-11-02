import pandas as pd
# print(pd.__version__)

# series = A Pandas 1D labled array that can hold any data type, think of it like a singl column in a spread sheet (1D)

data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])  # the right side indexing
# print(series)

# if we want to find a single element, we use location 
# print(series.loc["b"]) # will return a value that is at the label

# updating data
series.loc["c"] = 103
# print(series)

# index locating is also eligible
# print(series.iloc[0]) # starts with 0th index



# with dictionary
calories = {"day 1": 1750, "day 2": 1500, "day 3": 1700} # here days become the index and calories become the data

series = pd.Series(calories)
# print(series)

# print(series[series>1600])



# DataFrame = A tabular data structure with rows and cols (2D)

data = {
    "name": ["Ali", "Dua", 'Aisha'], 
    "age": [16, 19, 18]
}

df = pd.DataFrame(data, index = ["e1", "e2", "e3"])

# print(df.loc["e2"])  # searching one element
# print(df.iloc[2])

# Adding a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Adding a new row
# easy way, create a new data frame and concatenate them
new_row = pd.DataFrame([{"name":"Ayan", "age":20, "Job":"helper"}], index=["e4"])
df = pd.concat([df,new_row])

# Adding a new rows
new_rows = pd.DataFrame([{"name":"shayn", "age":17, "Job":"worker"}, {"name":"Hussain", "age":21, "Job":"Head"}], index=["e5", "e6"])
df = pd.concat([df,new_rows])
# print(df)


# importing csv and json files in pand as
df_csv = pd.read_csv("customers-100.csv")  # reading from acsv file

# print(df_csv.to_string())
# print(df_csv)


df_json = pd.read_json("students.json")
print(df_json) 