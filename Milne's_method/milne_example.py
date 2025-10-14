# Milne's Method example
# Problem: y' = y - x^2 + 1, with exact solution y(x) = (x+1)^2 - 0.5 e^x
# We'll use RK4 to bootstrap first 3/4 points and then Milne predictor-corrector.

import math

# ODE
def f(x, y):
    return y - x*x + 1

# exact solution for comparison
def y_exact(x):
    return (x + 1)**2 - 0.5 * math.exp(x)

# RK4 single step
def rk4_step(x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h*k1/2)
    k3 = f(x + h/2, y + h*k2/2)
    k4 = f(x + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

# Milne predictor (one common form) and corrector
# Using: y_p(n+1) = y(n-3) + 4h/3 * (2f(n) - f(n-1) + 2f(n-2))
#         y(n+1) = y(n-1) + h/3 * (f(n+1,p) + 4f(n) + f(n-1))


def milne_method(x0, y0, h, n_steps, tol=1e-6, max_iter=10):
    # We'll compute points x0, x1, ... using step h
    xs = [x0 + i*h for i in range(n_steps+1)]
    ys = [0.0]*(n_steps+1)
    ys[0] = y0

    # bootstrap first 3 values using RK4 (we need up to y3 to start Milne)
    for i in range(1, min(4, n_steps+1)):
        ys[i] = rk4_step(xs[i-1], ys[i-1], h)

    # function values
    fs = [f(xs[i], ys[i]) for i in range(min(4, n_steps+1))]

    for n in range(3, n_steps):
        # indices: we have ys up to index n; compute ys[n+1]
        # ensure fs list has entries for 0..n
        if len(fs) <= n:
            fs.append(f(xs[n], ys[n]))

        # predictor
        yp = ys[n-3] + (4*h/3.0) * (2*fs[n] - fs[n-1] + 2*fs[n-2])

        # predicted f at n+1
        fp = f(xs[n+1], yp)

        # corrector iterations
        y_new = ys[n-1] + (h/3.0) * (fp + 4*fs[n] + fs[n-1])
        iter_count = 0
        while abs(y_new - yp) > tol and iter_count < max_iter:
            yp = y_new
            fp = f(xs[n+1], yp)
            y_new = ys[n-1] + (h/3.0) * (fp + 4*fs[n] + fs[n-1])
            iter_count += 1

        ys[n+1] = y_new
        # append f(n+1) for future steps
        if len(fs) <= n+1:
            fs.append(f(xs[n+1], ys[n+1]))
        else:
            fs[n+1] = f(xs[n+1], ys[n+1])

    return xs, ys


if __name__ == '__main__':
    x0 = 0.0
    y0 = 0.5  # exact y(0) = (0+1)^2 - 0.5 e^0 = 1 - 0.5 = 0.5
    h = 0.2
    n_steps = 10  # compute up to x = 2.0

    xs, ys = milne_method(x0, y0, h, n_steps)

    print(f"x\tMilne_y\tExact_y\tAbsError")
    for xi, yi in zip(xs, ys):
        print(f"{xi:.4f}\t{yi:.6f}\t{y_exact(xi):.6f}\t{abs(yi - y_exact(xi)):.2e}")
