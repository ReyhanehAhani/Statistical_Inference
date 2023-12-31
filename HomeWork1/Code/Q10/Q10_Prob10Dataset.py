import os
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Create the directory if it doesn't exist
result_directory = "Q10/Result"
os.makedirs(result_directory, exist_ok=True)

# Printing Function
def print_txt(text, filename):
    filepath = os.path.join(result_directory, filename + ".txt")
    with open(filepath, "w") as log_file:
        print(text, file=log_file)

# Opening Dataset
df = pd.read_csv("Q10/prob10.csv")
print_txt("Dataset loaded successfully.", "Log")

# Convert '?' data to numpy NOT A NUMBER
df.replace("?", np.nan, inplace=True)
print_txt("Replaced '?' with NaN in the dataset.", "Log")

# Printing Primary Data Types
print_txt(str(df.dtypes), "Primary_dTypes")

# Changing object type to numerical values
def convert_to_numeric(df):
    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            pass 

convert_to_numeric(df)
print_txt("Converted object types to numerical values.", "Log")

# Data Cleaning
for column in df.columns:
    if df[column].dtype == "object":
        # Replace NaN with the mode for object-type columns
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        # Replace NaN with the mean for numerical-type columns
        df[column].fillna(df[column].mean(), inplace=True)

print_txt("Performed data cleaning (filled NaN values).", "Log")

# Bar Chart for Car Manufacturer Frequencies
plt.figure(figsize=(12, 6))
df['make'].value_counts().plot(kind='bar')
plt.title('Frequency of Each Car Manufacturer')
plt.xlabel('Car Manufacturer')
plt.ylabel('Frequency')
plt.savefig(os.path.join(result_directory, 'Car_Manufacturer_Frequency.png'))
plt.close()

# Displaying DataFrame Information
df_info_text = str(df.info())
print_txt(df_info_text, "DataFrame_Info")

# Dispersion Information, Skewness, and Kurtosis
dispersion_info = df.describe()
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
skewness = df[numerical_columns].apply(skew)
kurt = df[numerical_columns].apply(kurtosis)

print_txt("\nDispersion Information:", "Statistics_Info")
print_txt(str(dispersion_info), "Statistics_Info")
print_txt("\nSkewness:", "Statistics_Info")
print_txt(str(skewness), "Statistics_Info")
print_txt("\nKurtosis:", "Statistics_Info")
print_txt(str(kurt), "Statistics_Info")

# Scatter Plot: Engine Size vs. Price
plt.figure(figsize=(8, 6))
sns.scatterplot(x='engine-size', y='price', data=df)
plt.title('Scatter Plot: Engine Size vs. Price')
plt.savefig(os.path.join(result_directory, 'Scatter_Plot_Engine_Size_vs_Price.png'))
plt.close()

# Pairplot for Selected Variables
sns.pairplot(df[['length', 'wheel-base', 'curb-weight', 'horsepower', 'city-mpg','price']])
plt.suptitle("Pairplot for Selected Variables", y=1.02)
plt.savefig(os.path.join(result_directory, 'Pairplot_Selected_Variables.png'))
plt.close()

# Correlation Heatmap
correlation_matrix = df[numerical_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(result_directory, 'Correlation_Heatmap.png'))
plt.close()

# Boxplots for Categorical Columns
categorical_columns = ['make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style']

for col in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, y='price', data=df)
    plt.title(f'Boxplot for {col} and Price')
    plt.savefig(os.path.join(result_directory, f'Boxplot_{col}_and_Price.png'))
    plt.close()

print_txt("Visualization plots saved as images in Q10/Result directory.", "Log")
