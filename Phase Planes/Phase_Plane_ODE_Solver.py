import math
import numpy as np
from matplotlib import pyplot as plt

# Sets the size of the window
plt.figure(figsize=(8,8))

# Setting up axes
fMin = -5
fMax = 5
gMin = -5
gMax = 5
plt.axis([fMin, fMax, gMin, gMax])
plt.ylabel('f', fontsize=20)
plt.xlabel('g', fontsize=20)
plt.title('Phase Plane', fontsize=20)

# Put DEs here
def Df(f,g):
    "This is the f differintail equation that will generate the Df"
    return(f + g)

def Dg(g,f):
    "This is the g differintail equation that will generate the Dg"
    return(f*g)

# Grid size
gridf = 0.3
gridg = 0.3

# Drawing the phase plain
f = fMin
while f <= fMax:
    g = gMin
    while g <= gMax:
        plt.plot([f], [g], 'ko', ms = 2.0)
        df = Df(f,g)
        dg = Dg(g,f)
        length = math.sqrt(df*df + dg*dg)
        adjustment = (gridf + gridg)/2.0
        plt.arrow(f, g, (df/length)*adjustment, (dg/length)*adjustment, head_width=0.04, head_length=0.08, fc='b', ec='r')
        g += gridg
    f += gridf

# Setting time values
tStart = 0.0
tStop = 10.0
dt = 0.001

# Initial values of the functions should be evaluated at tStart.
t0 = tStart
f0 = 1.0
g0 = -0.4
plt.plot([f0], [g0], 'go', ms = 5.0) #Plotting starting point

# Calculates and draws Euler's method
f = f0
g = g0
t = t0
while t <= tStop:
    fNew = f + dt*Df(f,g)
    gNew = g + dt*Dg(g,f)
    lines = plt.plot([f, fNew], [g,gNew], color='b', linewidth=1.0)
    t = t + dt
    f = fNew
    g = gNew
print("Final Value",t, f, g)

# Calculates and draws T3
f = f0
g = g0
t = t0
while t <= tStop:
    # Taylor expansion to get new values of f and g
    fNew = f + (dt * Df(f,g)) + ((dt**2/2) * (Df(f,g) + Dg(g,f))) + ((dt**3/6) * (Df(f,g) + Dg(g,f) + (Df(f,g)*g) + (f*Dg(g,f))))
    gNew = g + (dt * Dg(g,f)) + ((dt**2/2) * (Df(f,g)*g + f*Dg(g,f))) + ((dt**3/6) * ((Df(f,g) + Dg(g,f))*g + Df(f,g)*Dg(g,f) + 2*Dg(g,f)*Df(f,g) + (f**3)*g))

    lines = plt.plot([f, fNew], [g,gNew], color='g', linewidth=1.0)
    t = t + dt
    f = fNew
    g = gNew
print("Final Value",t, f, g)

plt.show()