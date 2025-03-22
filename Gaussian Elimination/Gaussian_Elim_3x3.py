import math
import numpy as NP

# Size of matrix
N = 3

print("Number of rows and columns =", N)

# Loading the matrix
A = [[2.0, 2.0, -4.0],
     [-2.0, 3.0, 5.0],
     [7.0, 3.0, -1.0]]

# Loading the vector it is equal to.
B = [1.0, 2.0, 7.0]

# Zeroing out the solution vector.
x = [0.0, 0.0, 0.0]

# Setting the check vector to a non-zero value
y = [-10.0, -10.0, -10.0]

print("\nInputs")
print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])

print("\nWorking on first colmn")
temp = A[0][0]
for j in range(0, N):
  A[0][j] = A[0][j]/temp
B[0] = B[0]/temp

print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])

temp = -A[1][0]
for j in range(0, N):
  A[1][j] = A[0][j]*temp + A[1][j]
B[1] = B[0]*temp + B[1]

print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])


temp = -A[2][0]
for j in range(0, N):
  A[2][j] = A[0][j]*temp + A[2][j]
B[2] = B[0]*temp + B[2]


print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])

print("\nWorking on second colmn")



temp = A[1][1]
for j in range(1, N):
  A[1][j] = A[1][j]/temp
B[1] = B[1]/temp

print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])

temp = -A[2][1]
for j in range(1, N):
  A[2][j] = A[1][j]*temp + A[2][j]
B[2] = B[1]*temp + B[2]

print("A B", A[0], B[0])
print("   ", A[1], B[1])
print("   ", A[2], B[2])

print("\nDoing back substitution")
######################################    13.8(x2) = 5.9 -> x2 = 5.9 / 13.8
x[2] = B[2]/A[2][2]
######################################    x1(1.0) + x2(0.2) = 0.6 -> x1 = (0.6 - x2(0.2)) / 1.0
x[1] = (B[1] - A[1][2]*x[2])/A[1][1]
######################################    x0(1.0) + x1(1.0) + x2(-2.0) = 0.5 -> x0 = (0.5 - (x2(-2.0)) - x1(1.0)) / 1.0
x[0] = (B[0] - A[0][1]*x[1] - A[0][2]*x[2])/A[0][0]
######################################
print("\nThe solution to your problem is")
print("x = ", x)

print("\nDoing a check")
# Reloading the inputs
A = [[2.0, 2.0, -4.0],
     [-2.0, 3.0, 5.0],
     [7.0, 3.0, -1.0]]
B = [1.0, 2.0, 7.0]

y[0] = A[0][0]*x[0] + A[0][1]*x[1] + A[0][2]*x[2]
y[1] = A[1][0]*x[0] + A[1][1]*x[1] + A[1][2]*x[2]
y[2] = A[2][0]*x[0] + A[2][1]*x[1] + A[2][2]*x[2]
print("Ax =", y)
print("B =", B)
error = NP.subtract(B,y)
print("\nAx - B or your error = ", error)