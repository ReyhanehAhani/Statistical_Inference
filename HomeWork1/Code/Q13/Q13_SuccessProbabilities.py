import numpy as np
import matplotlib.pyplot as plt

def gamble(initial_stake, bet_amount, win_probability, target_amount, num_rounds):
    stake = initial_stake
    results = []

    for _ in range(num_rounds):

        if np.random.rand() < win_probability:
            stake += bet_amount
        else:
            stake -= bet_amount

        results.append(stake)
        if stake >= target_amount or stake <= 0:
            break

    return results

def simulate_gambling(initial_stake, bet_amount, win_probability, target_amount, num_rounds, num_simulations):
    probabilities = []

    for i in range(num_simulations):

        results = gamble(initial_stake, bet_amount, win_probability, target_amount, num_rounds)

        if results[-1] >= target_amount:
            probabilities.append(1)
        else:
            probabilities.append(0)

    probability_of_success = sum(probabilities) / num_simulations
    return probability_of_success

iterations = 50
success_probabilities = []

for iteration in range(iterations):
    probability_of_success = simulate_gambling(initial_stake=100, bet_amount=10, win_probability=0.5, target_amount=200, num_rounds=1000, num_simulations=5)
    success_probabilities.append(probability_of_success)


# Calculate and display statistics
mean_value = np.mean(success_probabilities)
print(f"Mean value over {iterations} iterations: {mean_value}")

# Plot the probabilities over all iterations
plt.figure(figsize=(8, 6))
plt.plot(range(1, iterations + 1), success_probabilities, marker='o', linestyle='-', color='g')
plt.xlabel('Iteration')
plt.ylabel('Probability of Success')
plt.title('Probability of Success Over 50 Iterations')
plt.grid(True)
plt.show()
