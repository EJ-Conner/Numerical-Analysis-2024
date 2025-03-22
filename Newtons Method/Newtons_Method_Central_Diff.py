import math

# Function to find zero of
def f(x):
  return(x*x - 4.0)

# Central difference calc
def df(x, h=1e-6):
  return (f(x + h) - f(x - h)) / (2 * h)

xStart = 0.1    # inital
tol = 0.0000001 # tolerance
maxIter = 20

iter = 0
dx = tol + 1
xOld = xStart
print(iter, xOld)

while(tol <= dx and iter < maxIter):
    # varibale to store central difference approx
    dfx = df(xOld)
    xNew = xOld - f(xOld) / dfx
    dx = abs(xNew - xOld)
    xOld = xNew
    iter += 1
    print(f"Interation: {iter},    Old x: {xOld}")

# Check for convergence
if(maxIter <= iter):
  print("A zero was never found with the tolerance and max iterations of", tol, maxIter)
else:
  print("Aprroximate x value of a zero is",xOld)
  print("The number of iterations used was",iter)
  print("The function value if you use this value is",f(xOld))



