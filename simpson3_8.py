import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ফাংশন f(x) = 0.2 + 25x - 200x² + 675x³ - 900x⁴ + 400x⁵
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Simpson’s 3/8 rule ফাংশন
def simpsons_3_8(f, a, b):
    h = (b - a) / 3
    result = (3*h/8) * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))
    return result

# Integration সীমা
a, b = 0, 0.8

# ফলাফল প্রিন্ট
print("Simpson’s 3/8 Rule Result =", simpsons_3_8(f, a, b))

# Plot করার জন্য data তৈরি
x = np.linspace(-0.01, 0.82, 100)
y = f(x)

# Simpson’s 3/8 এর জন্য 4টা পয়েন্ট
x_points = [a, (b-a)/3, 2*(b-a)/3, b]
y_points = [f(xi) for xi in x_points]

# Cubic spline দিয়ে interpolation curve তৈরি
spline = CubicSpline(x_points, y_points)
y_spline = spline(x)

# Plot
plt.plot(x, y, label="Actual f(x)")
plt.plot(x, y_spline, '--', label="Cubic Spline (Simpson 3/8)")
plt.scatter(x_points, y_points, color='green')
plt.fill_between(x, y_spline, alpha=0.3)

plt.legend()
plt.title("Simpson’s 3/8 Rule Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()