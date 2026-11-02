import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("A shape:", A.shape, "B shape:", B.shape)
add_res = A + B

print("A shape:", A.shape, "B shape:", B.shape)
sub_res = A - B

print("A shape:", A.shape, "B shape:", B.shape)
elem_mult = A * B

C = np.array([[1, 2], [3, 4], [5, 6]])
print("A shape:", A.shape, "C shape:", C.shape)
matmul_res = A @ C

print("A shape:", A.shape)
transpose_res = A.T

D = np.array([[4, 7], [2, 6]])
print("D shape:", D.shape)
det_res = np.linalg.det(D)
inv_res = np.linalg.inv(D)

print("Addition:\n", add_res)
print("Subtraction:\n", sub_res)
print("Element-wise Multiplication:\n", elem_mult)
print("Matrix Multiplication (@):\n", matmul_res)
print("Transpose:\n", transpose_res)
print("Determinant:", det_res)
print("Inverse:\n", inv_res)