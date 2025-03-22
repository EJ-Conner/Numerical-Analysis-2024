import math
import numpy as NP
from matplotlib import pyplot as plt
import sys

# Loading inputs
x = [-2.0, -1.0, 1.0, 3.0, 4.0, 5.0, 8.0, 9.0]
#x = [-2.0, -1.0, 1.0, 3.0, 4.0, 5.0, 8.0, 9.0]
# Loading outputs
y = [2.0, 2.0, -3, -4.0, 5.0, 2.0, -1.0, 5.0]
#y = [2.0, 1.0, 3, 4.0, 7.0, 8.0, 6.0, 9.0]

# added extra inputs up there to test how linear it is

# Find the number of points and check that the lengths are the same.
N = len(x)
M = len(y)
if(N!= M):
  print("The number of inputs does not match the number of outputs")
  sys.exit("Peace OUT!")
else:
  print("Number points =", N)

# Create figure size
plt.figure(figsize=(8,8))
left = -20
right = 20
bottom = -20
top = 20
plt.axis([left, right, bottom, top])
plt.ylabel('f', fontsize=20)
plt.xlabel('x', fontsize=20)
plt.title('divided differnce graph', fontsize=20)
lines = plt.plot([left , right], [0.0, 0.0], color='k', linewidth=1.0)
lines = plt.plot([0.0 , 0.0], [bottom, top], color='k', linewidth=1.0)
plt.grid()
plt.scatter(x, y, color='blue', label='Data points')

S = 0
S1 = 0
S2 = 0
S3 = 0

# sum up to et correct S's
for xi, yi in zip(x, y):
  S += xi
  S1 += xi**2
  S2 += yi
  S3 += xi*yi

# Create matrix to solve
matrix = NP.array([[S1, S], [S, N]])
matrixEqual = NP.array([S3, S2])

# use NP to solve
solution = NP.linalg.solve(matrix, matrixEqual)
m, b = solution

# print m and b
print("m = ", m)
print("b = ", b)


# Find R^2
TSS = 0
RSS = 0
for xi, yi in zip(x, y):
  TSS += (yi - NP.mean(y))**2
  RSS += (yi - (m*xi + b))**2

print("TSS = ", TSS)
print("RSS = ", RSS)

R2 = 1 - (RSS/TSS)

# Print R^2
print("R^2 = ", R2)

LinReg_line_x = NP.linspace(left, right, 100)  # Generate x values
LinReg_line_y = m * LinReg_line_x + b  # Calculate corresponding y values

plt.plot(LinReg_line_x, LinReg_line_y, color='red', label='Least squares line')
plt.legend()

plt.show()
