# This program draws Taylor's Method approximations
# over direction fields for a given diff. eq.

import math
import numpy as np
from matplotlib import pyplot as plt

numberOfSteps = 20  # for Taylor's method

# Sets figure size
plt.figure(figsize=(15,15))

# Define axes limits
tLeft = -5
tRight = 10
fBottom = -5
fTop = 10
plt.axis([tLeft, tRight, fBottom, fTop])
plt.ylabel('f', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.title("Taylor\'s Method over Direction Fields", fontsize=20)

def differentialEquation(f,t):
    "This is the differential equation."
    return(-f + t)

def exactSolutionFunction(t):
    "This is the solution to the differential equation."
    return(t - 1.0 + 9.0*math.exp(-t))

# Draws the direction fields
gridt = 0.3
gridf = 0.3
scaling = 0.6
lengthAdjustment = scaling*gridt
t= tLeft
while t <= tRight:
    f = fBottom
    while f <= fTop:
        plt.plot([t], [f], 'ko', ms = 2.0) # plots point
        df = differentialEquation(f,t)*gridt # Calculates the slope
        length = math.sqrt(df*df + gridt*gridt) # Calculates vector length
        plt.arrow(t, f, (gridt/length)*lengthAdjustment, (df/length)*lengthAdjustment, head_width=0.04, head_length=0.08, fc='b', ec='r')
        f += gridf
    t += gridt

# Intial conditions and the stop time.
t0 = 0.0
f0 = 8.0
tFinal = 9.0

# Calculate step size amd Taylor Coefs.
h = (tFinal - t0)/numberOfSteps
c1 = h
c2 = h*h/2.0
c3 = h*h*h/6.0
c4 = h*h*h*h/24.0
c5 = h*h*h*h*h/120.0
print("Number of Steps = %d  Step size = %5.10f" %(numberOfSteps,h))

def Df1(f,t):
  return (-f + t)

def Df2(f,t):
  return (f - t + 1)

def Df3(f,t):
  return (-f + t - 1)

def Df4(f,t):
  return (f - t + 1)

def Df5(f,t):
  return (-f + t - 1)

# Drawing the exact solution.
t = t0
count = 0
while count < numberOfSteps:
  lines = plt.plot([t, t + h], [exactSolutionFunction(t), exactSolutionFunction(t + h)], color='k', linewidth=1.0)
  count += 1
  t = t0 + h*count
print("The black graph is the exact value at the same time steps")

# Drawing the n = 0 solution to the prblem. Little O of 1
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f
  lines = plt.plot([t, t+h], [f,fNew], color='r', linewidth=1.0)
  count += 1
  t = t0 + h*count
  f = fNew
print("N = 0: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Red" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing the n = 1 solution to the prblem. Little O of 2 (Euler's Method)
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + Df1(f,t)*c1
  lines = plt.plot([t, t+h], [f,fNew], color='b', linewidth=2.0)
  count += 1
  t = t0 + h*count
  f = fNew
print("N = 1: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Blue" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing the n = 2 solution to the prblem. Little O of 3
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + Df1(f,t)*c1 + Df2(f,t)*c2
  lines = plt.plot([t, t+h], [f, fNew], color='c', linewidth=2.0)
  count += 1
  t = t0 + h * count
  f = fNew

print("N = 2: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Cyan" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing the n = 3 solution to the prblem. Little O of 4
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + Df1(f,t)*c1 + Df2(f,t)*c2 + Df3(f,t)*c3
  lines = plt.plot([t, t+h], [f, fNew], color='y', linewidth=2.0)
  count += 1
  t = t0 + h * count
  f = fNew

print("N = 3: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Yellow" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing the n = 4 solution to the prblem. Little O of 5
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + Df1(f,t)*c1 + Df2(f,t)*c2 + Df3(f,t)*c3 + Df4(f,t)*c4
  lines = plt.plot([t, t+h], [f, fNew], color='m', linewidth=2.0)
  count += 1
  t = t0 + h * count
  f = fNew

print("N = 4: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Magenta" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing the n = 5 solution to the prblem. Little O of 6
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + Df1(f,t)*c1 + Df2(f,t)*c2 + Df3(f,t)*c3 + Df4(f,t)*c4 + Df5(f,t)*c5
  lines = plt.plot([t, t+h], [f, fNew], color='g', linewidth=2.0)
  count += 1
  t = t0 + h * count
  f = fNew

print("N = 5: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Green" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

plt.show()


