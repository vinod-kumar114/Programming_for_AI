import pandas as pd

# DataFrame 1: Patients Info
df_patients = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104],
        "name": ["Ali", "Sara", "Usman", "Zainab"],
        "age": [45, 54, 61, 38],
    }
)

# DataFrame 2: Medical Test Results (heart.csv related)
df_tests = pd.DataFrame(
    {
        "patient_id": [102, 103, 104, 105],
        "chol": [240, 210, 280, 190],
        "target": [1, 0, 1, 0],  # 1 = Heart Disease, 0 = No
    }
)

# merge hamesha kisi basis pr hota hy, jaisy yaha pr patient id hy

merged = pd.merge(df_patients,df_tests)
# print(merged)









# ========= Concat

# DataFrame 1: Pehla batch of patients
df1 = pd.DataFrame(
    {
        "patient_id": [101, 102, 103],
        "name": ["Ali", "Sara", "Usman"],
        "age": [45, 54, 61],
    }
)


# DataFrame 3: Additional test features (Same rows as df1)
df3 = pd.DataFrame(
    {
        "chol": [240, 210, 280],
        "trestbps": [130, 140, 120],
        "target": [1, 0, 1],
    }
)

new_frame = pd.concat([df1,df3], axis=1, ignore_index=False)
print(new_frame)