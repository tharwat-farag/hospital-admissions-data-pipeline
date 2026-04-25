import os
import pandas as pd

input_file = "D:\Docker\ADMISSIONS.csv"
output_file = "D:\Docker\ADMISSIONS_CLEAN.csv"
os.makedirs(output_file, exist_ok=True)
df = pd.read_csv(input_file)
# Remove rows with missing values
df_clean = df.dropna()
df.to_parquet(f"{output_file}/ADMISSIONS_CLEAN.parquet", index=False)
print("Data cleaning completed. Cleaned data saved to ADMISSIONS_CLEAN.parquet")


