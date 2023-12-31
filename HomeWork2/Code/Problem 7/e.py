import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

sample_size = 100
sample = df.sample(sample_size)

alpha = (sample_size / (sample_size - 1))

sample_population_var = alpha * sample['population'].var()
sample_population_std_dev = np.sqrt(alpha) * sample['population'].std()

print(f"Estimated Population Variance: {sample_population_var}")
print(f"Estimated Population Standard Deviation: {sample_population_std_dev}")