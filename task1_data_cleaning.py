
import pandas as pd

# Load original dataset
df = pd.read_excel("ApexPlanet_Task1_Original.xlsx")

print("Original dataset shape:", df.shape)

# 1. Handle missing Age using median
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# 2. Handle missing City
df["City"] = df["City"].fillna("Unknown")

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Standardize Order_Date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 5. Identify Total_Sales outliers using IQR
Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["Sales_Outlier"] = df["Total_Sales"].apply(
    lambda x: "Yes" if x < lower_bound or x > upper_bound else "No"
)

# Final checks
print("\nFinal dataset shape:", df.shape)
print("\nMissing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("\nSales outliers:")
print(df["Sales_Outlier"].value_counts())
