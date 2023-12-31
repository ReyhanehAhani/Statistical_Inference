import random

def two_shared_BD(n, num_trials):
    success_count = 0

    for _ in range(num_trials):
        birthdays = set()
        for _ in range(n):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                success_count += 1
                break
            birthdays.add(birthday)

    return success_count / num_trials

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