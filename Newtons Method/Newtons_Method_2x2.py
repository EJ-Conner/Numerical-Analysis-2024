import math
import numpy as NP

# Size of matrix
N = 2

# Define system of nonlinear equations
def f1(x):
  return(x[0]*x[0] + x[1]*x[1] - 1.0)

def f2(x):
  return(x[0] - x[1]*x[1])

# Define Jacobian matrix
def df11(x):
  return(2.0*x[0])

def df12(x):
  return(2.0*x[1])

def df21(x):
  return(1.0)

def df22(x):
  return(-2.0 * x[1])

# Pivoting function.
def pivit(i, A, B, N):
  max = A[i][i]
  index = i
  for k in range(i+1, N):
    if(max < abs(A[k][i])):
      index = k
      max = abs(A[k][i])
  if(index != i):
    for j in range(0, N):
      temp = A[i][j]
      A[i][j] = A[index][j]
      A[index][j] = temp

    temp = B[i]
    B[i] = B[index]
    B[index] = temp

# store derivative functions in matrix
Derivatives = [[df11, df12],
               [df21, df22]]

# Function to calc Newton step (dx)
def gradShot(x, N):
  dx = [100.0, 100.0]
  A = [[Derivatives[i][j](x) for j in range(N)] for i in range(N)]
  B = [-f1(x), -f2(x)]

  # Gaussian Elim w/ pivoting to solve Ax=B
  for i in range(0, N):
    pivit(i, A, B, N)
    temp = A[i][i]
    for j in range(i, N):
      A[i][j] = A[i][j]/temp
    B[i] = B[i]/temp

    for k in range(i+1, N):
      temp = -A[k][i]
      for j in range(i, N):
        A[k][j] = A[i][j]*temp + A[k][j]
      B[k] = B[i]*temp + B[k]

  # Back sub to find dx
  for i in range(N-1, -1, -1):
    sum = B[i]
    for j in range(N-1, i, -1):
      sum = sum - A[i][j]*dx[j]
    dx[i] = sum/A[i][i]
  return(dx)

def VecMag(v, N):
  mag = 0.0
  for i in range(0, N):
    mag += v[i]*v[i]
  return(NP.sqrt(mag))

def VecAdd(v1, v2, N):
  mag = 0.0
  for i in range(0, N):
    v1[i] = v1[i]+v2[i]
  return(v1)

# Initial conditions
x = [2.0, 5.0]
tol = 0.000001
maxIter = 20

iter = 0
change = tol + 1.0
print("iter, change, x",iter, change, x)
while(tol <= change and iter < maxIter):
  dx = gradShot(x, N)
  x = VecAdd(x, dx, N)
  change = VecMag(dx, N)
  iter = iter + 1
  print("iter, change, x",iter, change, x)

if(maxIter <= iter):
  print("A zero was never found with the tolerance and max iterations of", tol, maxIter)
else:
  print("Aprroximate x value of a zero is",x)
  print("The number of iterations used was",iter)
  print("The function value if you use this value is",f1(x), f2(x))

