# Gauss Elimination Method (সহজ ভার্সন)
def gauss_elimination(A, B):
    n = len(B)

    # Step 1: Augmented matrix তৈরি (A | B)
    for i in range(n):
        A[i].append(B[i])

    # Step 2: Forward Elimination → Upper Triangular বানানো
    for i in range(n):
        # Pivot element check
        if A[i][i] == 0:
            raise ZeroDivisionError("Pivot element 0 পাওয়া গেছে!")

        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n + 1):
                A[j][k] -= ratio * A[i][k]

    # Step 3: Back Substitution → উপরের দিক থেকে সমাধান বের করা
    x = [0] * n
    # এই লাইনটা দিয়ে আমরা একটা list বানাচ্ছি, যেখানে n সংখ্যক শূন্য (0) থাকবে।
    
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


# উদাহরণ
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
B = [8, -11, -3]

ans = gauss_elimination(A, B)
print("Solution:")
print(f"x = {ans[0]:.2f}, y = {ans[1]:.2f}, z = {ans[2]:.2f}")