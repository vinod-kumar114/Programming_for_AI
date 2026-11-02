import numpy as np

np.random.seed(42)

A = np.random.randint(1,20, size=(3,4))
B = np.random.randint(1,20, size=(3,4))

# print(A)
# print(B)

# print(A+B)
# print(A-B)
# print(A*B)

# for matrix multiplication we must first change the shape of B
# print(A @ B.reshape(4,3))

# print(np.transpose(A))

B = np.random.randint(1,20, size=(4,4))
print(np.round(np.linalg.det(B),3)) # Error, dimensions must be square

print(np.round(np.linalg.inv(B),3))