import math

# Function to find zero of
def f(x):
  return(x*x - 4.0)

# Derivative
def df(x):
  return(2.0*x)

xStart = 0.1    # initial guess
tol = 0.0000001 # tolerance
maxIter = 20    # max iterations

iter = 0
dx = tol + 1
xOld = xStart
print(iter, xOld)
while(tol <= dx and iter < maxIter):
  xNew = xOld - f(xOld)/df(xOld)
  dx = abs(xNew - xOld)
  xOld = xNew
  iter += 1
  print("Iteration: ", iter, " Old x: ", xOld)

# Check for convergence
if(maxIter <= iter):
  print("A zero was never found with the tolerance and max iterations of ", tol, maxIter)
else:
  print("Aprroximate x value of a zero is",xOld)
  print("The number of iterations used was",iter)
  print("The function value if you use this value is",f(xOld))



