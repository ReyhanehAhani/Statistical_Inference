import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# ------------------------------- First Part ------------------------------- #

# Ploting Function
def plot_distribution(data, title):
    
    plt.figure(figsize=(8, 6))
    sns.histplot(data, kde=True)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# 1) Generate random data from a Uniform distribution
uniform_data = np.random.uniform(0, 1, 10000)
plot_distribution(uniform_data, "Uniform Distribution")

# 2) Generate random data from a Normal distribution
normal_data = np.random.normal(0, 1, 10000)
plot_distribution(normal_data, "Normal Distribution")

# 3) Generate random data from a Gamma distribution
gamma_data = np.random.gamma(2, 2, 10000)
plot_distribution(gamma_data, "Gamma Distribution")

# 4) Generate random data from an Exponential distribution
exponential_data = np.random.exponential(1, 10000)
plot_distribution(exponential_data, "Exponential Distribution")

# 5) Generate random data from a Binomial distribution
binomial_data = np.random.binomial(10, 0.5, 10000)
plot_distribution(binomial_data, "Binomial Distribution")


# ------------------------------- Second Part ------------------------------- #

# Generate means of each distribution over multiple iterations
num_iterations = 1000
sample_size = 10000
means = []

for _ in range(num_iterations):
    data = np.random.normal(0, 1, sample_size)
    mean = np.mean(data)
    means.append(mean)

plot_distribution(means, "Distribution of Sample Mean")
