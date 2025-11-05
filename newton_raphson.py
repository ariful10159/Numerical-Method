import numpy as np
import matplotlib.pyplot as plt

# ফাংশন f(x) = x² - 2
def f(x):
    return x**2 - 2

# f'(x) = 2x
def df(x):
    return 2*x

# Newton-Raphson Method
def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)   # সূত্র: xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)
        if abs(x_new - x) < tol:   # পার্থক্য ছোট হলে থামবে
            return x_new
        x = x_new
    return None   # যদি না মেলে

# প্রাথমিক অনুমান থেকে মূল বের করা
root = newton_raphson(f, df, 1)
print("Root =", root)

# প্লট করার জন্য ডেটা তৈরি
# np.linspace(0, 3, 100) = 0 থেকে 3 পর্যন্ত মোট 100টি সমান দূরত্বে থাকা সংখ্যার 1‑D array 
# (start ও stop দুটোই অন্তর্ভুক্ত)।
# spacing = (3 - 0) / (100 - 1) = 3/99 ≈ 0.030303...
x = np.linspace(0, 3, 100)
y = f(x)

# গ্রাফ আঁকা
plt.plot(x, y, label='f(x) = x² - 2', color='blue')
plt.axhline(0, color='black')                 # x-axis
plt.axvline(root, color='red', linestyle='--', label=f'Root ≈ {root:.5f}')
plt.scatter(root, f(root), color='green', s=60)
plt.title("Newton-Raphson Method for f(x) = x² - 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()