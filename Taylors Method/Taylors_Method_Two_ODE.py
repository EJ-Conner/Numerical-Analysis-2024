import math
import numpy as np
from matplotlib import pyplot as plt

# Number of steps
numberOfSteps = 300

# Set the figure size for plotting
plt.figure(figsize=(15, 15))

# Set the limits for the plot axes
tLeft = -1
tRight = 10
fBottom = -1
fTop = 10
plt.axis([tLeft, tRight, fBottom, fTop])

# Set labels and ttie for plot
plt.ylabel('f', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.title('Taylors\'s Method over Direction Fields', fontsize=20)


def differentialEquation(f,t):
    """
    Represents the differential equation:
        df/dt = -f * t * cos(t^2 / 2) + t * cos(t^2 / 2)
    Arguments:
        f : float : The current value of the function f(t)
        t : float : The current value of the independent variable t
    Returns:
        float : The rate of change of f(t) at the point (f,t)
    """
    return(-f*t*math.cos(t*t/2.0) + t*math.cos(t*t/2.0))

def exactSolutionFunction(t):
    """
    Represents the exact solution to the differential equation:
        f(t) = (exp(sin(t^2 / 2)) + 1) / exp(sin(t^2 / 2))
    Arguments:
        t : float : The current value of the independent variable t
    Returns:
        float : The exact value of f(t) at the point t
    """
    return((math.exp(math.sin(t*t/2.0)) +1.0)/math.exp(math.sin(t*t/2.0)))

# Plotting the direction field
gridt = 0.3    # Grid spacing for t
gridf = 0.3    # Grid spacing for f
scaling = 0.6  # Scaling factor for vector length
lengthAdjustment = scaling*gridt   # Adjustment factor for vector length
t= tLeft  # Start value for t

# Loop to draw direction field vectors
while t <= tRight:
    f = fBottom  # Start value for f
    while f <= fTop:
        plt.plot([t], [f], 'ko', ms = 2.0)
        df = differentialEquation(f,t)*gridt # Finds df from the slope.
        length = math.sqrt(df*df + gridt*gridt) # Computes the length of the vector.
        plt.arrow(t, f, (gridt/length)*lengthAdjustment, (df/length)*lengthAdjustment, head_width=0.04, head_length=0.08, fc='b', ec='r')
        f += gridf  # Increment f
    t += gridt      # Increment t

# Initial conditions and stop time
t0 = 0.0
f0 = 2.0
tFinal = 9.0

# Setting the step size and number of steps for the numeric schemes.
h = (tFinal - t0)/numberOfSteps
h1 = h
h2 = h*h/2.0
# Print number of steps and step size
print("Number of Steps = %d  Step size = %5.10f" %(numberOfSteps,h))

# Drawing the exact solution.
t = t0
count = 0
while count < numberOfSteps:
  lines = plt.plot([t, t + h], [exactSolutionFunction(t), exactSolutionFunction(t + h)], color='k', linewidth=1.0)
  count += 1
  t = t0 + h*count
print("The black graph is the exact value at the same time steps")

# Euler's Method (First Order Approximation)
f = f0
t = t0
count = 0
while count < numberOfSteps:
  # Euler's method for approximation (first-order)
  fNew = f + h1 * differentialEquation(f, t)
  lines = plt.plot([t, t+h], [f,fNew], color='b', linewidth=1.0)
  count += 1
  t = t0 + h*count
  f = fNew
print("N = 1: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Blue" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Second Order Method (Improved Euler's Method)
f = f0
t = t0
count = 0
while count < numberOfSteps:
  # Second-order approximation
  fNew = f + h1 * differentialEquation(f, t) + h2 * differentialEquation(differentialEquation(f, t), t)
  lines = plt.plot([t, t+h], [f,fNew], color='c', linewidth=1.0)
  count += 1
  t = t0 + h*count
  f = fNew
print("N = 2: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Cyan" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

plt.show()







