import math

# Function to find zero of
def f(x):
  return(x*x - 4.0)

numberOfBisections = 50
xLeft = 1.0  # starting number to the left of zero
dx = 1.0     # Jump size
xMax = 100.0 # Stopping value

# Finding an xRight that brackets a zero of the function starting at x0.
xRight = xLeft + dx
while(0.0 < f(xLeft)*f(xRight) and xRight < xMax):
  xRight = xRight + dx

if(xMax <= xRight):
  print("A bracket could not be found with the start value and stop value of", xLeft, xMax)
else:
  i = 0
  while i < numberOfBisections:
    xNew = xLeft  + (xRight - xLeft)/ 2.0  # midpoint calculation
                                          # computes midpoint of interval [xLeft, xRight]
    fLeft = f(xLeft)
    fNew = f(xNew)

    # sign check
    if fLeft * fNew < 0:
      xRight = xNew
    else:
      xLeft = xNew

    i = i + 1

  xNew = xLeft + (xRight - xLeft)/2.0
  maxError = (xRight - xLeft)/2.0
  print("Aprroximate x value of a zero is",xNew)
  print("The function value if you use this value is",f(xNew))
  print("An error bound from the given value to the true value is",maxError)




