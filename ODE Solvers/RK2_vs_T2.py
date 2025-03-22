import math
import numpy as np
from matplotlib import pyplot as plt

numberOfSteps = 1000


# Sets the size of the window to draw in
plt.figure(figsize=(15,15))

# Set axes for plot
tLeft = -1
tRight = 10
fBottom = -1
fTop = 10
plt.axis([tLeft, tRight, fBottom, fTop])
plt.ylabel('f', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.title('Taylors\'s Method over Direction Fields', fontsize=20)

def differentialEquation(t,f):
    "This is the differential equation."
    return(-f*t*math.cos(t*t/2.0) + t*math.cos(t*t/2.0))

def exactSolutionFunction(t):
    "This is the solution to the differential equation."
    return((math.exp(math.sin(t*t/2.0)) +1.0)/math.exp(math.sin(t*t/2.0)))

# Draws the direction fields
gridt = 0.2
gridf = 0.2
scaling = 0.6
lengthAdjustment = scaling*gridt
t= tLeft
while t <= tRight:
    f = fBottom
    while f <= fTop:
        plt.plot([t], [f], 'ko', ms = 2.0)
        df = differentialEquation(t,f)*gridt # calculates df from slope.
        length = math.sqrt(df*df + gridt*gridt) # calculates vector length
        plt.arrow(t, f, (gridt/length)*lengthAdjustment, (df/length)*lengthAdjustment, head_width=0.04, head_length=0.08, fc='b', ec='r')
        f += gridf
    t += gridt

# Intial conditions and the stop time.
t0 = 0.0
f0 = 2.0
tFinal = 9.0

# Step size
h = (tFinal - t0)/numberOfSteps
h1 = h
h2 = h*h/2.0
print("Number of Steps = %d  Step size = %5.10f" %(numberOfSteps,h))

# Drawing the exact solution.
t = t0
count = 0
while count < numberOfSteps:
  lines = plt.plot([t, t + h], [exactSolutionFunction(t), exactSolutionFunction(t + h)], color='k', linewidth=3.0)
  count += 1
  t = t0 + h*count
print("The black graph is the exact value at the same time steps")

# Drawing T2 solution.
f = f0
t = t0
count = 0
while count < numberOfSteps:
  fNew = f + differentialEquation(t,f)*h1 + ((1-f)*(math.cos(t*t/2.0) - t*t*math.sin(t*t/2.0)) - t*math.cos(t*t/2.0)*differentialEquation(t,f))*h2
  lines = plt.plot([t, t+h], [f,fNew], color='c', linewidth=2.0)
  count += 1
  t = t0 + h*count
  f = fNew
print("T2: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Cyan" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

# Drawing RK2 solution.
alpha = 1
beta = 1
w1 = 0.5
w2 = 0.5
f = f0
t = t0
count = 0
while count < numberOfSteps:
    k1 = h * differentialEquation(t, f)  # Step 1: Compute k1
    k2 = h * differentialEquation(t + alpha * h, f + beta * k1)  # Step 2: Compute k2
    fNew = f + w1 * k1 + w2 * k2  # Step 3: Update fnew
    lines = plt.plot([t, t + h], [f, fNew], color='b', linewidth=1.0)
    count += 1
    t = t0 + h * count
    f = fNew
print("RK2: time = %5.10f  aprox = %5.10f  exact = %5.10f  error = %5.10f Blue" % (t,fNew, exactSolutionFunction(t), fNew - exactSolutionFunction(t)))

plt.show()


