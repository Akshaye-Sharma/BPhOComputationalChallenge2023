import numpy as np
import math
from matplotlib import pyplot as plt

P = 248.348  # Period

def simpsonintegration(theta, ecc):
    a = 0
    n = 81 
    h = (theta - a) / (n - 1)
    x = np.linspace(a, theta, n)
    f = 1 / (1 + ecc * np.cos(x))**2
    I_simp = (h / 3) * (f[0] + 2 * np.sum(f[2:n-2:2]) \
                        + 4 * np.sum(f[1:n-1:2]) + f[-1])
    time = (P * (1 - ecc**2)**(3/2)) * I_simp * (1 / (2 * math.pi))
    return time

thetas = np.arange(0, 19, 0.1)

times0 = [simpsonintegration(theta, 0) for theta in thetas]
times025 = [simpsonintegration(theta, 0.25) for theta in thetas]

plt.plot(times0, thetas, label='Circular orbit (e=0)', color='blue')
plt.plot(times025, thetas, label='Elliptical orbit (e=0.25)', color='green')

# Plotting Info & Misc
plt.xlim(0, 800)
plt.ylim(0, 20)
plt.xlabel('Time')
plt.ylabel('Theta (radians)')
plt.legend()
plt.grid(True)
plt.title('Orbital Time vs Angle Using Simpson Integration')
plt.show()
