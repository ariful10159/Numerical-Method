import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return x**3 - 4*x - 9

# Bisection Method (easy version)
def bisection(f, a, b, tol=1e-5):
    while abs(b - a) > tol:
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return mid

# Find root
root = bisection(f, 2, 3)
print(f"Root ≈ {root:.5f}")

# Plot
x = np.linspace(0, 4, 100)
plt.plot(x, f(x), label='f(x) = x³ - 4x - 9')
plt.axhline(0, color='red', linestyle='--')
plt.axvline(root, color='green', linestyle='--', label=f'Root = {root:.5f}')
plt.scatter(root, f(root), color='blue')
plt.title("Bisection Method (Easy Version)")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

