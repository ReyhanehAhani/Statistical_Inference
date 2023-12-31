import numpy as np

def estimate(n):
    points = np.sum(np.random.uniform(0, 1, n)**2 + np.random.uniform(0, 1, n)**2 < 1)
    return 4 * points / n


n = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for i in n:
    result = estimate(i)
    print(result, 'Estimator result for N =', i)

