import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

num_strata = 4

df['stratum'] = pd.qcut(df['population'], q=num_strata, labels=False)

# # For testing
# print(df.head())

mean_estimates = []
mean_population = 0
total_mortality_estimates = []

for stratum in range(num_strata):

    stratum_data = df[df['stratum'] == stratum]
    sample = stratum_data.sample(n=6, random_state=42)  
    
    mean_estimate = sample['population'].mean()
    total_mortality_estimate = sample['mortalities'].sum()
    
    mean_population += mean_estimate
    mean_estimates.append(mean_estimate)
    total_mortality_estimates.append(total_mortality_estimate * (len(df)/ len(stratum_data)))

for i in range(num_strata):
    print(f"Stratum {i + 1}:")
    print(f"  Mean Population: {mean_estimates[i]:.2f}")
    print(f"  Total Mortality: {total_mortality_estimates[i]}")
    print('--------------------------')
    print(f"Total Mean Population: {mean_population/4:.2f}")


