from random import randint, random
import matplotlib
import numpy as np

#Operation with array
my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

#Operation with matrix
my_math = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = np.array(my_math)
print("\nHere is the matrix\n", mat)
print("Dimension of the matrix: ", mat.ndim)
print("Size of the matrix: ", mat.size)

#Generate a rage of values
print("\nA series of numbers: ", np.arange(5, 16))

#Vector of 0s
print("\n", np.zeros(5))
#Vector of ones
print("\n", np.ones(5))

#Matrix of 0s
print("\n", np.zeros((3, 4)))
#Matrix of ones
print("\n", np.ones((3,5)))
#Matrix of Ns, N = 5
print("\n", 5*np.ones((3,6)))
#Empty Matrix
print("\n", np.empty((3,5)))
#Identity Matrix
print("\n", np.eye(4))

#Random number generation (Rangin from 0 to 1)
print("\n", np.random.rand(2,3))
#Random integer vector
print("\n", np.random.randint(1, 101, 10))
#Random integer matrix
print("\n", np.random.randint(1, 101, (4,4)))

#Reshaping, min, max, sort
from numpy.random import randint as ri
a = ri(1, 100, 30)
#Reshaping
b = a.reshape(2,3,5)
c = a.reshape(6,5)
print("\nShape of a:", a.shape)
print(a)
print("\nShape of b:", b.shape)
print(b)
print("\nShape of c:", c.shape)
print(c)
#Sorting Vectors
A = ri(1, 100, 10)
print("\nOriginal vector:\n",A)
print("\nSorted vector:\n", np.sort(A, kind="mergesort"))
#Sorting Matrix
M = ri(1, 100, 25).reshape(5, 5)
print("\nOriginal Matrix:\n", M)
print("\nSorted Matrix:\n", np.sort(M, kind="heapsort"))
#Max
print("\nMax of a:", a.max())
print("Max of a location:", a.argmax())

#Indexing and slicing
arr = np.arange(1, 11)
print("\nArray:", arr)
print("Element at 7th index is:", arr[7])
print("Elements from 3rd to 5th index are:", arr[3:6])
print("Elements up to 4th index are", arr[:4])
print("Elements from last backguards are:", arr[-1::-1])
print("3 Elements from last backguards are:", arr[-1: -6: -2])

#Conditional Subsetting
mat = np.array(ri(10, 100, 15)).reshape(3, 5)
print("\nMatrix:\n", mat)
print("Elements grater than 50\n",mat[mat>50])

#Array-Matrix Operations
mat1 = np.array(ri(1, 10, 9)).reshape(3, 3)
mat2 = np.array(ri(1, 10, 9)).reshape(3, 3)
print("\nMatrix 1:\n", mat1)
print("\nMatrix 2:\n", mat2)
#Addition
print("\nAddition:\n", mat1 + mat2)
#Multiplication
print("\nMultiplication:\n", mat1 * mat2)
#Division
print("\nDivision:\n", mat1 / mat2)
#Linear Combination
print("\nLinear Combination (3*A - 2*B):\n", 3 * mat1 - 2 * mat2)
#Addition of an scalar
print("\nAddition of an scalar (100+A):\n", 100 + mat1)
#Exponentiation
print("\nExponentiation:\n", mat1**3)
#Exponential power
print("\nExponential power:\n", np.exp(mat1))
#10th-base logarithm
print("\n10th-base logarithm:\n", np.log10(mat1))
#Module reminder
print("\nModule reminder:\n", np.fmod(mat1, mat2))

#NumPy basic statistics

#Sum of all number of a matrix
print("\nSum of all number of a matrix:\n", np.sum(mat1))
#Sum of all number of a column in a matrix
print("\nSum of all number in a column in a matrix:", np.sum(mat1, axis=0))
#Sum of all number of a row in a matrix
print("\nSum of all number in a row in a matrix:", np.sum(mat1, axis=1))
#Product of all number of a column in a matrix
print("\nProduct of all number in a column in a matrix:", np.prod(mat1, axis=0))
#Product of all number of a row in a matrix
print("\nProduct of all number in a row in a matrix:", np.prod(mat1, axis=1))
#Mean of all number in a matrix
print("\nMean of all number in a matrix:", np.mean(mat1))
#Standard deviation of all number in a matrix
print("\nMean of all number in a matrix:", np.std(mat1))
#Variance of all number in a matrix
print("\nVariance of all number in a matrix:", np.var(mat1))
#Median of all number in a matrix
print("\nMedian of all number in a matrix:", np.median(mat1))

#Correlation and Covariance
import matplotlib.pyplot as plt
A = ri(1, 5, 20)
B = 2 * A + 5 * np.random.randn(20)
plt.scatter(A, B)
plt.title("Scatter plot of A vs B, expect a small positive correlation")
plt.show()
print(np.corrcoef(A, B))
