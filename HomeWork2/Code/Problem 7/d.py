import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

sample_size = 100
sample = df.sample(sample_size)

sample_mean = sample['mortalities'].mean()
sample_total_mortality = sample['mortalities'].sum()

actual_mortalities_mean = df['mortalities'].mean()
actual_mortalities_total = df['mortalities'].sum()

estimated_mortalities_mean = sample['mortalities'].mean()
estimated_mortalities_total = sample_total_mortality * (len(df) / sample_size)

print(f"Sample mean: {sample_mean}")
print(f"Sample total mortality: {sample_total_mortality}")

print('-------------------------------------')

print(f"Actual mortalities mean: {actual_mortalities_mean}")
print(f"Actual total mortality: {actual_mortalities_total}")

print('-------------------------------------')

print(f"Estimated mortalities mean: {estimated_mortalities_mean}")
print(f"Estimated total mortality: {estimated_mortalities_total}")
