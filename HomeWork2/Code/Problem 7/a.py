import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Problem 7\Data.xls' 
df = pd.read_excel(file_path)

print("First few rows of the dataframe:")
print(df.head())

plt.hist(df['population'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Population Values for Cancer Mortality')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()
