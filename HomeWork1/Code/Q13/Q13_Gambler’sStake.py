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

    plt.figure(figsize=(10, 6))

    for i in range(num_simulations):
        
        results = gamble(initial_stake, bet_amount, win_probability, target_amount, num_rounds)

        if results[-1] >= target_amount:
            probabilities.append(1)
        else:
            probabilities.append(0)

        plt.plot(results, label=f'Simulation {i+1}')


    probability_of_success = sum(probabilities) / num_simulations
    print(f"Probability of reaching the target before going broke: {probability_of_success}")

    plt.axhline(target_amount, color='r', linestyle='--', label='Target Amount')
    plt.axhline(0, color='b', linestyle='--', label='Broke')
    plt.xlabel('Number of Rounds')
    plt.ylabel('Gambler\'s Stake')
    plt.title('Gambler\'s Ruin Simulation')
    plt.legend()
    plt.show()

simulate_gambling(initial_stake=100, bet_amount=10, win_probability=0.5, target_amount=200, num_rounds=1000, num_simulations=5)
