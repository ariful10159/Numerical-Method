

import numpy as np

# সমীকরণগুলো:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

# coefficient (A) এবং constant (B)
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])
B = np.array([8, -11, -3])

# মূল determinant
D = np.linalg.det(A)

# প্রতিটি ভেরিয়েবল এর জন্য determinant
Dx = np.linalg.det(np.column_stack((B, A[:, 1], A[:, 2])))
Dy = np.linalg.det(np.column_stack((A[:, 0], B, A[:, 2])))
Dz = np.linalg.det(np.column_stack((A[:, 0], A[:, 1], B)))

# সমাধান (Cramer's Rule)
x = Dx / D
y = Dy / D
z = Dz / D

print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

