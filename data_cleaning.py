import pandas as pd
import numpy as np

df = pd.read_csv("raw_data.csv")
print("Original Data:")
print(df)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\nCleaned Column Names:")
print(df.columns)

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'].fillna(df['age'].median(), inplace=True)

df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['salary'].fillna(df['salary'].median(), inplace=True)

#df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
df['join_date'] = pd.to_datetime(
    df['join_date'],
    errors='coerce',
    dayfirst=True
)

df['join_date'].fillna(df['join_date'].mode()[0], inplace=True)
print(df['join_date'])


df.drop_duplicates(inplace=True)

df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned data saved!")

df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned data saved!")

log = [
    "Standardized column names",
    "Handled missing values",
    "Converted incorrect data types",
    "Removed duplicate records"
]

with open("cleaning_log.txt", "w") as file:
    for item in log:
        file.write(item + "\n")

print("Cleaning log created!")