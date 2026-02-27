import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2]
y = [1, 1/2, 4/3]

plt.figure(figsize=(8, 5))

plt.plot(x, y, 'o', label='Data Points', color = "pink")
plt.plot(x, y, '-', label='Linear Spline')

for i in range(len(x) - 1):
    x0, x1 = x[i], x[i+1]
    y0, y1 = y[i], y[i+1]

coefficient = np.polyfit(x, y, 2)
poly = np.poly1d(coefficient)

x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = poly(x_smooth)
plt.plot(x_smooth, y_smooth, '-', label='Quadratic Fit (Parabola)')

# ===============================
# AGGIUNTA: spline quadratica
# ===============================

# Sistema con 2 tratti: [0,1] e [1,2]
# Ogni tratto: a*x^2 + b*x + c → 6 incognite

A = np.array([
    [0**2, 0, 1, 0, 0, 0],     # S0(0) = 1
    [1**2, 1, 1, 0, 0, 0],     # S0(1) = 1/2
    [0, 0, 0, 1**2, 1, 1],     # S1(1) = 1/2
    [0, 0, 0, 2**2, 2, 1],     # S1(2) = 4/3
    [2*1, 1, 0, -2*1, -1, 0],  # S0'(1) = S1'(1)
    [2, 0, 0, 0, 0, 0]         # S0''(1) = 0 → a0 = 0
])
b = np.array([1, 1/2, 1/2, 4/3, 0, 0])

coeffs = np.linalg.solve(A, b)
b0, a0, c0, a1, b1, c1 = coeffs

def S0(x): return a0*x**2 + b0*x + c0
def S1(x): return a1*x**2 + b1*x + c1

x0_vals = np.linspace(0, 1, 100)
x1_vals = np.linspace(1, 2, 100)

plt.plot(x0_vals, S0(x0_vals), label='Quadratic Spline [0,1]', color = "Purple")
plt.plot(x1_vals, S1(x1_vals), label='Quadratic Spline [1,2]', color = "Purple")

plt.title("Linear Spline and Parabola Through Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
