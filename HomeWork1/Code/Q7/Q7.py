import numpy as np

expected_gains_list = []
simulation_number = 10000

for _ in range (simulation_number):

    n = 60

    X = np.random.randint(1, 5, size=n)
    Y = np.random.randint(1, 7, size=n)  

    G = np.where(X > Y, 2 * X, -1)
    expected_gain_loss = np.mean(G)

    expected_gains_list.append(expected_gain_loss)

print(sum(expected_gains_list)/simulation_number)