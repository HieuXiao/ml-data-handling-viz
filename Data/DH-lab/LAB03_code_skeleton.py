import pandas as pd

df = pd.read_csv("LAB03_retail_quality_issues_raw.csv")
print(df.shape)
print(df.head())

missing_count = df.isna().sum()
missing_pct = df.isna().mean() * 100
print(pd.DataFrame({"missing_count": missing_count, "missing_pct": missing_pct.round(2)}))

print("Duplicate rows:", df.duplicated().sum())
print(df["gender"].value_counts(dropna=False))
print(df.describe(include="all"))
