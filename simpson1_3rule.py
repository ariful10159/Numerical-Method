import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ফাংশনটি সংজ্ঞায়িত করা হয়েছে
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Simpson’s 1/3 Rule Function
def simpsons_1_3(f, a, b):
    mid = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4*f(mid) + f(b))

# সীমা নির্ধারণ
a, b = 0, 0.8

# ফলাফল প্রিন্ট
print("Simpson’s 1/3 Rule Result =", simpsons_1_3(f, a, b))

# x এর জন্য array তৈরি
x = np.linspace(-0.01, 0.82, 100)
y = f(x)

# তিনটি পয়েন্ট (a, mid, b)
x_points = [a, (a+b)/2, b]
y_points = [f(xi) for xi in x_points]

# Cubic spline curve তৈরি
spline = CubicSpline(x_points, y_points)
y_spline = spline(x)

# আসল ফাংশন প্লট
plt.plot(x, y, label="Actual f(x)", color='blue')
# Simpson 1/3 Approximation
plt.plot(x, y_spline, '--', color='red', label="Simpson’s 1/3 Approximation")
# পয়েন্টগুলো দেখানো
plt.scatter(x_points, y_points, color='green')
# এরিয়া ভরাট করা
plt.fill_between(x, y_spline, alpha=0.3, color='red')

# গ্রাফের লেবেল ও শিরোনাম
plt.title("Simpson’s 1/3 Rule Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()