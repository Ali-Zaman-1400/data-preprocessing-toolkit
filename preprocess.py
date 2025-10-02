import pandas as pd
import numpy as np
import chardet

# Auto-detect encoding
with open("input.csv", "rb") as f:
    result = chardet.detect(f.read())
encoding = result["encoding"]

# Read dataset
df = pd.read_csv("input.csv", encoding=encoding)

# Handle missing values (fill with mean for numeric columns)
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mean())

# Detect and fix outliers using IQR
for col in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    df[col] = np.where(df[col] > upper, df[col].median(), df[col])
    df[col] = np.where(df[col] < lower, df[col].median(), df[col])

# Save output
df.to_csv("output_clean.csv", index=False, encoding="utf-8")

print(" Preprocessing completed! Saved to output_clean.csv")
