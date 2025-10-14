import math

# Milne's predictor-corrector implementation only
# Assumes initial history of 4 points is provided: x0..x3, y0..y3
# Uses Milne predictor and corrector forms shown previously.

def f(x, y):
    """Example ODE function. Replace if desired."""
    return y - x*x + 1

def milne_next(xs, ys, fs, h, tol=1e-10, max_iter=10):
    """
    Compute y_{n+1} using Milne predictor-corrector.

    Inputs:
    - xs: list of x values, length at least 4, with xs[-1] = x_n
    - ys: list of y values, length at least 4, with ys[-1] = y_n
    - fs: list of f(x_i, y_i) values corresponding to xs/ys
    - h: step size
    Returns: y_{n+1}, f_{n+1}
    """
    # indices: using last 4 entries: n-3, n-2, n-1, n
    # predictor: y_p(n+1) = y_{n-3} + 4h/3 * (2 f_n - f_{n-1} + 2 f_{n-2})
    y_n3 = ys[-4]
    f_n2 = fs[-3]
    f_n1 = fs[-2]
    f_n = fs[-1]

    y_p = y_n3 + (4.0*h/3.0) * (2.0*f_n - f_n1 + 2.0*f_n2)

    # predicted f at n+1
    x_np1 = xs[-1] + h
    fp = f(x_np1, y_p)

    # corrector: y(n+1) = y(n-1) + h/3 * (f(n+1,p) + 4 f_n + f_{n-1})
    y_new = ys[-2] + (h/3.0) * (fp + 4.0*f_n + f_n1)

    iter_count = 0
    while abs(y_new - y_p) > tol and iter_count < max_iter:
        y_p = y_new
        fp = f(x_np1, y_p)
        y_new = ys[-2] + (h/3.0) * (fp + 4.0*f_n + f_n1)
        iter_count += 1

    return y_new, fp


if __name__ == '__main__':
    # Self-test: use exact solution to provide initial history for y0..y3
    def y_exact(x):
        return (x + 1)**2 - 0.5 * math.exp(x)

    x0 = 0.0
    h = 0.2
    xs = [x0 + i*h for i in range(4)]
    ys = [y_exact(x) for x in xs]
    fs = [f(x, y) for x, y in zip(xs, ys)]

    # compute next point using Milne only
    y4, f4 = milne_next(xs, ys, fs, h)
    x4 = xs[-1] + h
    print(f"x4 = {x4:.4f}")
    print(f"Milne y4 = {y4:.6f}")
    print(f"Exact y4  = {y_exact(x4):.6f}")
    print(f"Abs error = {abs(y4 - y_exact(x4)):.2e}")
