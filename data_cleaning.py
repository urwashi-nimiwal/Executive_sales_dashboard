import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tracker_data.csv",encoding="latin1")
print(df.head(5))

# Check the basic information before cleaning
print(df.shape)
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())


# Convert Order Date and Ship Date into datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# Remove $ and commas from Sales and convert it to numbers
df["Sales"] = df["Sales"].str.replace("$", "", regex=False)
df["Sales"] = df["Sales"].str.replace(",", "", regex=False)
df["Sales"] = pd.to_numeric(df["Sales"])

# Clean the Profit column
# Values inside brackets represent negative numbers
df["Profit"] = df["Profit"].str.replace("$", "", regex=False)
df["Profit"] = df["Profit"].str.replace(",", "", regex=False)
df["Profit"] = df["Profit"].str.replace("(", "-", regex=False)
df["Profit"] = df["Profit"].str.replace(")", "", regex=False)
df["Profit"] = pd.to_numeric(df["Profit"])

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# Check the data after cleaning
print("\nData types after cleaning:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# See the cleaned data
print(df.head())
# after cleaning the data save it to a new csv file
df.to_csv("tracker_data_cleaned.csv", index=False)