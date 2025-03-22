import math
import numpy as NP
from matplotlib import pyplot as plt
import sys

# Loading inputs
x = [-2.0, -1.0, 1.0, 3.0, 4.0, 5.0, 8.0, 9.0]
# new x's for testing
#x = [-4.0, -2.0, 1.0, 2.0, 6.0, 7.0, 9.0, 10.0]
# Loading outputs
y = [2.0, 2.0, -3, -4.0, 5.0, 2.0, -1.0, 5.0]

# Finding the number of points
N = len(x)
M = len(y)
if(N!= M):
  print("The number of inputs does not match the number of outputs")
  sys.exit("Peace OUT!")
else:
  print("Number points =", N)

# Sets figure size
plt.figure(figsize=(8,8))

# Creats an x y plane
left = -10
right = 10
bottom = -10
top = 10
plt.axis([left, right, bottom, top])
plt.ylabel('f', fontsize=20)
plt.xlabel('x', fontsize=20)
plt.title('divided differnce graph', fontsize=20)

# Plotting x and y axis
lines = plt.plot([left , right], [0.0, 0.0], color='k', linewidth=1.0)
lines = plt.plot([0.0 , 0.0], [bottom, top], color='k', linewidth=1.0)

# Ploting points
plt.plot(x, y, 'o', color ='r')

# Setting the coefficients
a = [0.0 for i in range(N)]

div_diff = [[0.0 for k in range(N)] for k in range(N)]
for i in range(N):
    div_diff[i][0] = y[i]  # First column is just the y values

for j in range(1, N):  # Loop over columns
    for i in range(N - j):  # Loop over rows
        div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x[i + j] - x[i])

for i in range(N):
    a[i] = div_diff[0][i]  # Coefficients are the top row of the divided difference table


# Final function to be plotted.
def f(xx):
  b = [0.0 for i in range(N)]
  b[0] = a[0]  # Start with the first coefficient
  sum = b[0]
  for i in range(1, N):  # Build the Newton polynomial incrementally
      b[i] = a[i]
      for j in range(i - 1, -1, -1):
          b[i] = b[i] * (xx - x[j])
  for i in range(1, N):
      sum += b[i]
  return(sum)

# Draw function
dx = 0.1
xx = left

while xx < right:
  # printing values of actual x points listed above.
  if any(abs(xx - xi) < 1e-9 for xi in x):
    print(f"f({xx}) = {f(xx)}")
  lines = plt.plot([xx , xx+dx], [f(xx),f(xx+dx)], color='b', linewidth=1.0)
  xx += dx

plt.show()

