import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

sample_size = 25
sample = df.sample(sample_size)

mean_estimate = (sample['population'] * sample['mortalities']).sum() / sample['population'].sum()
total_mortality_estimate = (sample['population'] * sample['mortalities']).sum()

print("Ratio Estimate for Population Mean:", mean_estimate)
print("Ratio Estimate for Total Cancer Mortality:", total_mortality_estimate)