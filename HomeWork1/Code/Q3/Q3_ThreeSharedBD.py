import random
from collections import Counter

def three_shared_BD(n, num_trials):

    success_count = 0

    for _ in range(num_trials):
        
        birthdays = [random.randint(1, 365) for _ in range(n)]
        birthday_counter = Counter(birthdays)

        for _, count in birthday_counter.items():
            if count >= 3:
                success_count += 1
                break
        
    return success_count / num_trials

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