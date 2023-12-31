import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

sample_size = 25
num_samples = 10000
distribution_means = []

for _ in range(num_samples):
    sample = np.random.choice(df['mortalities'], size=sample_size, replace=True)
    sample_mean = np.mean(sample)
    distribution_means.append(sample_mean)

# # For testing
# distribution_mean = np.mean(distribution_means)
# distribution_std_dev = np.std(distribution_means)

# print("Mean of the Sampling Distribution:", distribution_mean)
# print("Standard Deviation of the Sampling Distribution:", distribution_std_dev)

plt.figure(figsize=(8, 6))
plt.hist(distribution_means, bins=100, color='skyblue', edgecolor='black')
plt.title('Sampling Distribution of the Mean (Sample Size = 25)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()
