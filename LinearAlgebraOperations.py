#LINEAR ALGEBRA OPERATIONS WITH NUMPY
from cProfile import label
from re import X
import matplotlib
import numpy as np
from numpy.random import randint as ri

#Dot/Inner/Outer products
A = ri(1, 10, 9).reshape(3, 3)
print("Matrix A:\n", A)
print("Matrix A Transpose:\n", np.transpose(A))

B = ri(1, 10, 6).reshape(3, 2)
print("\nMatrix B:\n", B)
print("Matrix B Transpose:\n", np.transpose(B))

#Dot product
print("\nMatrix A and B Dot product:\n", np.dot(A, B))

#Trace of a Matrix
print("\nTrace of matrix A:\n", np.trace(A))
print("\nTrace of 2nd offset matrix A:\n", np.trace(A, offset=2))

#Singular Value Decomposition
A = np.random.randint(1, 10, 9).reshape(3, 3)
print("\nOriginal Matrix A:\n", A)
u, s, v = np.linalg.svd(A, compute_uv=1, full_matrices=True)
print("\nU:\n",u)
print("\nSingular values, S:", s)
print("\nV:\n", v)

#QR decomposition/factorization
A = np.random.randint(1, 10, 9).reshape(3, 3)
print("\nThe original matrix:\n", A)
q, r = np.linalg.qr(A)
print("\nQ:", q)
print("\nR:", r)

#Eigenvalues and eigenvectors
A = np.random.randint(1, 10, 9).reshape(3, 3)
print("\nThe original matrix:\n", A)
w, v= np.linalg.eig(A)
print("\nEigenvalues:\n", w)
print("\nEigenvectors:\n", v)

#LINEAR EQUATION SOLVING, MATRIX INVERSE, LINEAR LEAST SQUARE
A = np.array([[2,5,1],[3,-2,-1],[1,-3,1]])
B = np.array([14,-1,4])
x = np.linalg.solve(A,B)

#Linear Equation Solving
print("\nThe equation solution is:\n", x)

#Matrix Inverse
A = 0.1 * np.random.randint(1, 20, 16).reshape(4, 4)
print("\nMatrix A:\n", A)
print("\nInverse of A:\n", np.linalg.inv(A))

#Least Square
x = np.arange(1, 11, 1)
y = 2 * x + np.random.randn(10) - 1
print("\n", x)
print("\n", y)
A = np.vstack([x, np.ones(len(x))]).T
print("\n",A)
m, c = np.linalg.lstsq(A, y)[0]
print("\nCoefficient:" + str(m) + "\n" + "intercept:" + str(c))

import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m * x + c, 'r', label='Fitted line')
plt.legend()
plt.show()