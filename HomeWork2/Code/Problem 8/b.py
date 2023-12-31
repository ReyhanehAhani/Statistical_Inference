import numpy as np
import matplotlib.pyplot as plt

def ellipse_area(a, b, n):
    
    x = np.random.uniform(-a, a, n)
    y = np.random.uniform(-b, b, n)
    inside_ellipse = (x**2 / a**2 + y**2 / b**2) < 1

    area_ratio = np.sum(inside_ellipse) / n
    total_area = 4 * a * b  
    estimated_area = area_ratio * total_area

    # Plotting for better visualization of the estimator 
    plt.scatter(x, y, c=inside_ellipse, cmap='viridis', alpha=0.5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Monte Carlo Simulation for Ellipse Area Estimation')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return estimated_area

major_axis = 3
minor_axis = 2

n = [100, 1000, 10000, 100000]

for i in n:
    estimated_area = ellipse_area(major_axis, minor_axis, i)
    print(f"Estimated Area of Ellipse: {estimated_area} for N = {i}")
