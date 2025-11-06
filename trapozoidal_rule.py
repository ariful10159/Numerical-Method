import numpy as np
import matplotlib.pyplot as plt

def fun(x):
  return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def trapezoidal_rule(fun, a, b):
  return (b - a) * (fun(a) + fun(b)) / 2
# np.arange(start, stop, step) diye একটা 1‑D array তৈরি করা হয় — start থেকে step করে বাড়বে, 
# আর stop এর চেয়ে ছোট পর্যন্ত থাকবে (stop নিজে included নয়)।

# array = np.arange(-0.01, 0.82, 0.01) মানে:

# শুরু: -0.01
# শেষ (exclusive): 0.82 (0.82 নিজে থাকবে না)
# ধাপ: 0.01

array = np.arange(-0.01, 0.82, 0.01)

print(trapezoidal_rule(fun, 0, 0.8))
plt.plot(array, fun(array))
plt.plot([0, 0.8], [fun(0), fun(0.8)], color='red')
plt.show()