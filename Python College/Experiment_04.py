# Write a Python program to perform attribute transformation, sampling, normalization, standardization, and feature scaling on a dataset using Pandas and Scikit-learn.

import pandas as pd
import numpy as np
from sklearn.preprocessing import (
    LabelEncoder,
    MinMaxScaler,
    StandardScaler
)

# Create dataset
data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Salary': [20000, 25000, 30000, 35000, 40000,
               45000, 50000, 55000, 60000, 65000],
    'Department': [
        'IT', 'HR', 'IT', 'Finance', 'HR',
        'IT', 'Finance', 'IT', 'HR', 'Finance'
    ]
}

df = pd.DataFrame(data)

print("ORIGINAL DATASET")
print(df)

# ------------------------------------------------
# 1. ATTRIBUTE TRANSFORMATION
# ------------------------------------------------

encoder = LabelEncoder()

df['Department_Encoded'] = encoder.fit_transform(df['Department'])
print("\nATTRIBUTE TRANSFORMATION")
print(df[['Department', 'Department_Encoded']])

# ------------------------------------------------
# 2. SAMPLING
# ------------------------------------------------

sample = df.sample( n=5, random_state=42)
print("\nSAMPLING")
print(sample)

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

normalizer = MinMaxScaler()

df[['Age_Normalized', 'Salary_Normalized']] = \
    normalizer.fit_transform(
        df[['Age', 'Salary']]
    )

print("\nNORMALIZATION")
print(df[['Age', 'Salary',
          'Age_Normalized',
          'Salary_Normalized']])

# ------------------------------------------------
# 4. STANDARDIZATION
# ------------------------------------------------

standardizer = StandardScaler()

df[['Age_Standardized', 'Salary_Standardized']] = \
    standardizer.fit_transform(
        df[['Age', 'Salary']]
    )

print("\nSTANDARDIZATION")
print(df[['Age', 'Salary',
          'Age_Standardized',
          'Salary_Standardized']])

# ------------------------------------------------
# 5. FEATURE SCALING
# ------------------------------------------------

scaler = MinMaxScaler()

df[['Age_Scaled', 'Salary_Scaled']] = \
    scaler.fit_transform(
        df[['Age', 'Salary']]
    )

print("\nFEATURE SCALING")
print(df[['Age', 'Salary',
          'Age_Scaled',
          'Salary_Scaled']])
