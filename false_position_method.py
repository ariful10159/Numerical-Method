

import matplotlib.pyplot as plt
import numpy as np

# Simple function
def f(x):
  return x**2 - 2

def false_position_method(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    # c = a - (f(a) * (b - a) / (f(b) - f(a)))
    c = b - (f(b) * (a - b) / (f(a) - f(b)))  # Recalculate c using b

    if abs(f(c)) < tol:
        return c
    elif f(a) * f(c) < 0:
        return false_position_method(f, a, c, tol)
    else:
        return false_position_method(f, c, b, tol)



root = false_position_method(f, 0, 10)

# Let's plot the result
x = np.arange(0, 3, 0.1)

plt.plot(x, f(x), label='f(x) = x^2 - 2')
plt.scatter(root, f(root), color='blue')  # Mark the root on the plot
# plt.axvline(root, color='purple', linestyle='--', label=f'x = root ({root:.5f})')

# plt.axvline(0, color='green', linestyle='--')
# plt.axhline(0, color='red', linestyle='--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"False Position Method Root: {root:.5f}")
plt.grid()
plt.legend()
plt.show()

