import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

num_strata = 4

df['stratum'] = pd.qcut(df['population'], q=num_strata, labels=False)

total_population_stratum = df.groupby('stratum')['population'].sum()

sampling_fraction_proportional = total_population_stratum / total_population_stratum.sum()

stratum_variances = df.groupby('stratum')['population'].var()
sampling_fraction_optimal = 1 / stratum_variances

print("Sampling Fraction (Proportional Allocation):")
print(sampling_fraction_proportional)
print("\nSampling Fraction (Optimal Allocation):")
print(sampling_fraction_optimal)

# Simple random sampling variance
srs_variance = df['population'].var()

# Proportional allocation variance
proportional_allocation_variance = (sampling_fraction_proportional**2 * stratum_variances).sum()

# Optimal allocation variance
optimal_allocation_variance = (sampling_fraction_optimal**2 * stratum_variances).sum()

print("\nVariances:")
print("Simple Random Sampling Variance:", srs_variance)
print("Proportional Allocation Variance:", proportional_allocation_variance)
print("Optimal Allocation Variance:", optimal_allocation_variance)
