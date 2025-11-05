# Gauss-Jordan Elimination in Python

def gauss_jordan(a, b):
    n = len(b)

    # Make augmented matrix
    for i in range(n):
        a[i].append(b[i])

    # Forward elimination + make diagonal 1
    for i in range(n):
        # Pivot should not be zero
        if a[i][i] == 0.0:
            raise ZeroDivisionError("Divide by zero detected!")

        # Make pivot = 1
        pivot = a[i][i]
        for j in range(i, n+1):
            a[i][j]  /= pivot

        # Make other rows' same column = 0
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(i, n+1):
                    a[k][j] -= factor * a[i][j]

    # Extract solution
    x = [a[i][n] for i in range(n)]
    return x


# Example usage
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]

b = [8, -11, -3]

solution = gauss_jordan(A, b)
print("Solution:", solution)