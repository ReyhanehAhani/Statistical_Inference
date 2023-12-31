import pandas as pd

file_path = 'Problem 7\Data.xls'  
df = pd.read_excel(file_path)

population_mean = df['population'].mean()
total_mortality = df['mortalities'].sum()

population_variance = df['population'].var()
population_std_dev = df['population'].std()

print("Total Cancer Mortality:", total_mortality)
print("Population Mean:", population_mean)
print("Population Variance:", population_variance)
print("Population Standard Deviation:", population_std_dev)
