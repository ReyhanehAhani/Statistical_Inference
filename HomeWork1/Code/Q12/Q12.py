import numpy as np
import matplotlib.pyplot as plt
import math

def estimate_pi(N):
    points_inside_circle = 0

    for _ in range(N):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    estimated_pi = 4 * (points_inside_circle / N)
    return estimated_pi

actual_pi = math.pi

differences = []
estimated_pi_values = []

# Various number of N for diferent iteration
N_values = [100, 500, 1000, 5000, 10000]

for N in N_values:
    estimated_pi_value = estimate_pi(N)
    
    difference = abs(estimated_pi_value - actual_pi)
    differences.append(difference)
    estimated_pi_values.append(estimated_pi_value)
    print(f"N = {N}: Estimated Pi = {estimated_pi_value}, Difference = {difference}")

fig, ax1 = plt.subplots(figsize=(10, 6))

# Use a logarithmic scale for better visualization
ax1.plot(N_values, differences, marker='o', linestyle='-', label='Difference', color='blue')
ax1.set_xscale('log')  
ax1.set_xlabel('Number of Random Points (N)')
ax1.set_ylabel('Difference from Actual Pi', color='blue')
ax1.tick_params('y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(N_values, estimated_pi_values, marker='s', linestyle='--', label='Estimated Pi', color='green')
ax2.set_ylabel('Estimated Pi', color='green')
ax2.tick_params('y', colors='green')

plt.title('Monte Carlo Estimation of Pi')
fig.tight_layout()
plt.show()
