import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

sample_size = 100
sample = df.sample(sample_size)

mean_sample_population = np.mean(sample['population'])

#  Confidence intervals calculations
population_data = df['population']
mean_population = np.mean(population_data)
std_dev_population = np.std(population_data, ddof=1)

confidence_level = 0.95

standard_error = std_dev_population / np.sqrt(len(df))
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, len(df) - 1) * standard_error

lower_interval = mean_population - margin_of_error
upper_interval = mean_population + margin_of_error

print(f"Mean Population: {mean_population}")
print(f"Mean Sample Population: {mean_sample_population}")
print(f"Standard Error: {standard_error}")
print(f"Margin of Error: {margin_of_error}")
print(f"95% Confidence Intervals: ({lower_interval}, {upper_interval})")
