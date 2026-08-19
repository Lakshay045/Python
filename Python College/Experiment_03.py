# ==========================================================
# EXPERIMENT:
# Load, Clean, and Preprocess a Real-World Dataset using Pandas
# ==========================================================

# Step 1: Import Libraries
import pandas as pd
import numpy as np

print("=" * 60)
print("DATA PREPROCESSING USING PANDAS")
print("=" * 60)

# ----------------------------------------------------------
# Step 2: Load Dataset
# ----------------------------------------------------------
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print("\nDataset Loaded Successfully!")

# ----------------------------------------------------------
# Step 3: Display Dataset
# ----------------------------------------------------------
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

# ----------------------------------------------------------
# Step 4: Check Missing Values
# ----------------------------------------------------------
print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# ----------------------------------------------------------
# Step 5: Handle Missing Values
# ----------------------------------------------------------

# Fill Age with Median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked with Mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because it has many missing values
df.drop(columns=["Cabin"], inplace=True)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# ----------------------------------------------------------
# Step 6: Remove Duplicate Rows
# ----------------------------------------------------------
print("\nDuplicate Rows Before Removal:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate Rows After Removal:", df.duplicated().sum())

# ----------------------------------------------------------
# Step 7: Detect and Remove Outliers using IQR
# ----------------------------------------------------------

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

Lower_Limit = Q1 - 1.5 * IQR
Upper_Limit = Q3 + 1.5 * IQR

df = df[
    (df["Age"] >= Lower_Limit) &
    (df["Age"] <= Upper_Limit)
]

print("\nDataset Shape After Removing Outliers")
print(df.shape)

# ----------------------------------------------------------
# Step 8: Data Transformation
# ----------------------------------------------------------

# Convert Gender into Numeric Values
df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

# Convert Embarked into Numeric Values
df["Embarked"] = df["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2
})

# Create Family Size Feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Create Age Groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 18, 35, 60, 100],
    labels=["Child", "Young Adult", "Adult", "Senior"]
)

# ----------------------------------------------------------
# Step 9: Display Cleaned Dataset
# ----------------------------------------------------------
print("\nCleaned Dataset")
print(df.head())

print("\nFinal Dataset Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

# ----------------------------------------------------------
# Step 10: Save Cleaned Dataset
# ----------------------------------------------------------
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_titanic.csv'")