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

