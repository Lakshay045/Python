import numpy as np
import pandas as pd
from scipy import stats

# -------------------------------
# Sample Dataset
# -------------------------------
data = {
    'Math': [85, 78, 90, 88, 76, 95, 89, 84, 91, 73],
    'Science': [82, 74, 91, 87, 79, 94, 90, 81, 92, 75],
    'English': [80, 72, 88, 86, 77, 93, 87, 79, 90, 74]
}

df = pd.DataFrame(data)

print("========== DATASET ==========")
print(df)

# -------------------------------
# Mean
# -------------------------------
print("\n========== MEAN ==========")
print(df.mean())

# -------------------------------
# Median
# -------------------------------
print("\n========== MEDIAN ==========")
print(df.median())

# -------------------------------
# Mode
# -------------------------------
print("\n========== MODE ==========")
mode_result = stats.mode(df, keepdims=True)
print(pd.DataFrame(mode_result.mode, columns=df.columns))

# -------------------------------
# Variance
# -------------------------------
print("\n========== VARIANCE ==========")
print(df.var())

# -------------------------------
# Standard Deviation
# -------------------------------
print("\n========== STANDARD DEVIATION ==========")
print(df.std())

# -------------------------------
# Quartiles
# -------------------------------
print("\n========== QUARTILES ==========")
print("Q1 (25%):")
print(df.quantile(0.25))

print("\nQ2 (50% - Median):")
print(df.quantile(0.50))

print("\nQ3 (75%):")
print(df.quantile(0.75))

# -------------------------------
# Correlation
# -------------------------------
print("\n========== CORRELATION MATRIX ==========")
print(df.corr())

# -------------------------------
# Complete Statistical Summary
# -------------------------------
print("\n========== DESCRIPTIVE SUMMARY ==========")
print(df.describe())
