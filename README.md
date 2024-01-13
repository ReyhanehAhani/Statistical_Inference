# Homework 1 - Python Code ReadMe

## Question 3: Birthday Paradox Simulations

### three_shared_BD Function
This function aims to simulate the Birthday Paradox problem, where the goal is to find the minimum number of people needed in a group such that there is a 50% chance that at least three people share the same birthday.

#### Usage
```python
import random
from collections import Counter

def three_shared_BD(n, num_trials):
    # ... (function code)
    return success_count / num_trials
```

#### Description
- **n**: Number of people in the group.
- **num_trials**: Number of simulation trials.

#### Example
```python
num_trials = 10000
target_probability = 0.5
num_simulations = 20

for i in range(num_simulations):
    n = 1
    while True:
        probability = three_shared_BD(n, num_trials)
        if probability >= target_probability:
            print(f"Simulation {i+1}: Minimum n for P(A) > {target_probability} is {n}")
            break
        n += 1
```

### two_shared_BD Function
This function simulates a variant of the Birthday Paradox, looking for the minimum number of people needed in a group such that there is a 90% chance that at least two people share the same birthday.

#### Usage
```python
import random

def two_shared_BD(n, num_trials):
    # ... (function code)
    return success_count / num_trials
```

#### Description
- **n**: Number of people in the group.
- **num_trials**: Number of simulation trials.

#### Example
```python
num_trials = 30
target_probability = 0.9
num_simulations = 10

for i in range(num_simulations):
    n = 1
    while True:
        probability = two_shared_BD(n, num_trials)
        if probability >= target_probability:
            print(f"Simulation {i+1}: Minimum n for P(A) > {target_probability} is {n}")
            break
        n += 1
```

## Question 10: Random Data Distributions

This code generates random data from various distributions and plots them.

### Usage
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ... (code for plot_distribution function)

# 1) Generate random data from a Uniform distribution
uniform_data = np.random.uniform(0, 1, 10000)
plot_distribution(uniform_data, "Uniform Distribution")

# ... (similar code for other distributions)

# Generate means of each distribution over multiple iterations
# ... (code for the iteration loop and plotting means)
```

## Question 12: Monte Carlo Estimation of Pi

This code estimates the value of pi using the Monte Carlo method.

### Usage
```python
import numpy as np
import matplotlib.pyplot as plt
import math

# ... (code for estimate_pi function)

# Various number of N for different iterations
N_values = [100, 500, 1000, 5000, 10000]

# ... (code for pi estimation and plotting)
```

## Question 13: Gambler's Ruin Simulation

This code simulates a gambler's experience, tracking the stake over rounds.

### Usage
```python
import numpy as np
import matplotlib.pyplot as plt

# ... (code for gamble and simulate_gambling functions)

# Example simulation
simulate_gambling(initial_stake=100, bet_amount=10, win_probability=0.5, target_amount=200, num_rounds=1000, num_simulations=5)

# ... (code for multiple iterations and statistics plotting)
```

## Question 7: Expected Gains Simulation

This code simulates a scenario where two players roll dice, and player X gains points based on the outcomes.

### Usage
```python
import numpy as np

# ... (code for expected_gains_list simulation)

# Example simulation
simulation_number = 10000
for _ in range(simulation_number):
    # ... (code for X, Y, and G calculations)

print(sum(expected_gains_list) / simulation_number)
```

### Description
This code calculates the expected gains in a game where two players roll dice. The simulation is repeated a specified number of times, and the average expected gain is then printed.


# Homework 2 - Python Code ReadMe

## Part a_7: Data Loading and Initial Exploration

This part loads the data from an Excel file and prints the first few rows of the dataframe. Additionally, it generates a histogram for the 'population' column.

### Usage
```python
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
```

## Part b_7: Basic Descriptive Statistics

This part calculates and prints total cancer mortality, population mean, population variance, and population standard deviation.

### Usage
```python
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
```

## Part c_7: Sampling Distribution of the Mean

This part generates a sampling distribution of the mean with a sample size of 25 and 10,000 samples.

### Usage
```python
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

plt.figure(figsize=(8, 6))
plt.hist(distribution_means, bins=100, color='skyblue', edgecolor='black')
plt.title('Sampling Distribution of the Mean (Sample Size = 25)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()
```

## Part d_7: Confidence Intervals

This part calculates and prints 95% confidence intervals for the mean of the population.

### Usage
```python
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

# Confidence intervals calculations
# ... (code for confidence intervals calculation)
```

## Part e_7: Ratio Estimate for Population Mean and Total Cancer Mortality

This part calculates and prints ratio estimates for the population mean and total cancer mortality.

### Usage
```python
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
```

## Part m_7: Stratified Sampling - Fractional Allocation

This part performs stratified sampling with four strata, calculates the sampling fractions using proportional and optimal allocation, and computes the variances for simple random sampling, proportional allocation, and optimal allocation.

### Usage
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

file_path = 'Problem 7\Data.xls'
df = pd.read_excel(file_path)

num_strata = 4

# ... (code for stratified sampling and variance calculations)
```

# Homework 3 - Python Code ReadMe

This repository contains Python scripts for data analysis and statistical tests. Below is a summary of the scripts and their functionality.

## Contents

### Question 3_1 - Age Distribution Visualization

File: `question_3_1.py`

This script uses Matplotlib to create a histogram showing the age distribution of male and female fans. It uses data arrays `men_ages` and `women_ages` to generate the plot.

### Question 3_2 - Normality Test and Q-Q Plot

File: `question_3_2.py`

This script performs a Kolmogorov-Smirnov test on the ages of men using SciPy's `kstest`. Additionally, it creates a Q-Q plot using the `probplot` function from SciPy.

### Question 4_2 - Random Number Classification

File: `question_4_2.py`

Here, a probability matrix is flattened, and pseudo-random numbers are generated to classify observations based on the specified conditions. The counts in each cell and an example of the first few observations are displayed.

### Question 4_4 - Chi-Squared Goodness-of-Fit Test

File: `question_4_4.py`

This script uses the generated data from Question 4_2 to perform a chi-squared goodness-of-fit test. It calculates observed and expected counts, then checks the hypothesis at a significance level of 0.05.

### Question 8_1 - Kolmogorov-Smirnov Test for Uniform Distribution

File: `question_8_1.py`

The script performs a Kolmogorov-Smirnov test on given data to determine if it follows a uniform distribution.

### Question 8_2 - Maximum Difference Calculation

File: `question_8_2.py`

This script calculates the maximum difference between corresponding elements of two data arrays, `data1` and `data2`.

### Question 3_6 - Mann-Whitney U Test

File: `question_3_6.py`

The Mann-Whitney U test is performed on the ages of men and women to compare the distributions.

## Instructions

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Run the scripts using a Python interpreter:

   ```bash
   python question_3_1.py
   python question_3_2.py
   python question_4_2.py
   python question_4_4.py
   python question_8_1.py
   python question_8_2.py
   python question_3_6.py
   ```
