

import math
import numpy as NP

# Function to print matrix and vector side-by-side
def printCheck(M, V, N):
  for k in range(0, N):
    if(k == 0):
      print("A B = ", M[k], V[k])
    else:
      print("      ", M[k], V[k])

# Pivoting function.
def pivit(i, AA, BB, N):
  max = AA[i][i]
  index = i
  for k in range(i+1, N):
    if(max < abs(AA[k][i])):
      max = AA[k][i]
      index = k
  if(index != i):
    for j in range(0, N):
      temp = AA[i][j]
      AA[i][j] = AA[index][j]
      AA[index][j] = temp
    temp = BB[i]
    BB[i] = BB[index]
    BB[index] = temp

# Size of matrix
N = 4
print("Number of rows and columns =", N)

# Input matrix A and copy AA for modification.
A = [[3.0, 2.0, 2.0, -4.0],
     [2.0, -2.0, 3.0, 5.0],
     [8.0, -2.0, 1.0, 4.0],
     [1.0, 7.0, 3.0, -1.0]]

AA = [[3.0, 2.0, 2.0, -4.0],
     [2.0, -2.0, 3.0, 5.0],
     [8.0, -2.0, 1.0, 4.0],
     [1.0, 7.0, 3.0, -1.0]]

# Loading the vector it is going to be equal to.
# I will work on BB and check against vector B.
B = [2.0, 1.0, 2.0, 7.0]

BB = [2.0, 1.0, 2.0, 7.0]

# Initializing solution vectors
x = [0.0, 0.0, 0.0, 0.0]
y = [0.0, 0.0, 0.0, 0.0]
error = [-100.0, -100.0, -100.0, -100.0]

print("\nInput matrix and the vector it is equal to")
printCheck(AA, BB, N)

# Doing Gausse elemenation.
for i in range(0, N):
  pivit(i, AA, BB, N)
  print("\nAfter Pivit i", i)
  printCheck(AA, BB, N)

  temp = AA[i][i]
  for j in range(i, N):
    AA[i][j] /= temp
  BB[i] = BB[i]/temp

  for k in range(i+1, N):
    temp = -AA[k][i]
    for j in range(i, N):
      AA[k][j] += temp * AA[i][j] # eliminates elements below diagonal
    BB[k] = BB[i]*temp + BB[k]

# Doing back substitution to find solution vector x
for i in range(N-1, -1, -1):
  sum = BB[i]
  for j in range(N-1, i, -1):
    sum = sum - AA[i][j]*x[j]
  x[i] = sum / AA[i][i]

print("\nThe solution to the problem Ax = B is:")
print("x = ", x)

# Check the solution by calculating Ax and comparing to B.
print("\nDoing a check")
for i in range(0, N):
  y[i] = 0
  for j in range(0, N):
    y[i] = y[i] + A[i][j]*x[j]
print("Ax = ", y)
print("B  = ", B)

# Calculate and print the error vector.
for i in range(0, N):
  error[i] = B[i] - y[i]
print("Error = ", error)