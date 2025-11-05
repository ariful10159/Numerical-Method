# First let's import necessary libs
import matplotlib.pyplot as plt
import numpy as np
import math

def f2(x):
    return x**3 - 2*x + 2

def g3(x):
    return (x**3 + 1) / 4


def iteration_method(g, x, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError(
        "Iteration did not converge within the maximum number of iterations."
    )



root = iteration_method(g3, 1)


# Let's plot the result
#  x = np.arange(-10, 10, 0.1)

# easy one
# plt.plot(x,f2(x),label='f(x)=x^3-2x+2')
# plt.scatter(root,f(root),color='red',label='Root')

# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title(f'Iteration Method Root: {root:.5f}')
# plt.grid()
# plt.legend()

# Let's plot the result
x = np.arange(-10, 10, 0.1)

plt.plot(x, f2(x), label='f2(x) = x^3 - 2x + 2')
plt.scatter(root, f2(root), color='blue')  


# Mark the root on the plot
plt.axvline(root, color='purple', linestyle='--', label=f'x = root ({root:.5f})')

plt.axvline(0, color='green', linestyle='--')
plt.axhline(0, color='red', linestyle='--')

plt.xlabel('x')
plt.ylabel('f2(x)')
plt.title(f"Iteration Method Root: {root:.5f}")
plt.grid()
plt.legend()  
plt.show()