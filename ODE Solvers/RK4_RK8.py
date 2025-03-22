import math
import numpy as np
from matplotlib import pyplot as plt

# Sets the size of the window to draw in
plt.figure(figsize=(15,15))

# Define axis, time range, and function value range
tLeft = -1
tRight = 10
fBottom = -3
fTop = 5
plt.axis([tLeft, tRight, fBottom, fTop])
plt.ylabel('f', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.title('Runge-Kutta Methods over Direction Fields', fontsize=20)

def differentialEquation(t,f):
    "This is the differential equation."
    a = 0.01  # Damping coefficient
    b = 1.5   # Forcing amplitude
    c = 2.0   # Frequency of oscillation
    d = 0.3   # Nonlinear feedback term
    return -a * f + b * math.sin(c * t) + d * math.cos(f * b) + math.exp(1) * math.sin(t * f)

# Draws the direction fields
gridt = 0.1
gridf = 0.1
scaling = 0.6 # Scaling factor for vector length.
lengthAdjustment = scaling*gridt
t= tLeft
while t <= tRight:
    f = fBottom
    while f <= fTop:
        plt.plot([t], [f], 'ro', ms = 2.0)
        df = differentialEquation(t,f)*gridt # Finds df from the slope.
        length = math.sqrt(df*df + gridt*gridt) # Finds the length of the vector.
        plt.arrow(t, f, (gridt/length)*lengthAdjustment, (df/length)*lengthAdjustment, head_width=0.04, head_length=0.08, fc='cyan', ec='darkviolet')
        f += gridf
    t += gridt

# Intial conditions for the exact IVP
t0 = 0.0
f0 = 2.0
tFinal = 9.0

# Setting up step size
h = 0.01
numberOfSteps = (tFinal - t0)/h
print("Number of Steps = %d  Step size = %5.10f" %(numberOfSteps,h))

# RK4
for sign in [1, -1]:  # Solve both positive and negative initial conditions
    f = sign * f0
    t = t0
    count = 0
    while count < numberOfSteps:
        K1 = h * differentialEquation(t, f)
        K2 = h * differentialEquation(t + 0.5*h, f + 0.5*K1)
        K3 = h * differentialEquation(t + 0.5*h, f + 0.5*K2)
        K4 = h * differentialEquation(t + h, f + K3)
        fNew = f + (K1 + 2.0*K2 + 2.0*K3 + K4) / 6.0
        plt.plot([t, t+h], [f, fNew], color='forestgreen', linewidth=5.0)
        count += 1
        t = t0 + h * count
        f = fNew
    print(f"RK4: time = {t:.10f}  approx = {fNew:.10f} forest green")



# RK8
for sign in [1, -1]:  # Solve both positive and negative initial conditions
    f = sign * f0
    t = t0
    count = 0
    while count < numberOfSteps:
        # Compute RK8 coefficients
        K0 = differentialEquation(t, f)
        K1 = differentialEquation(t + h/9.0, f + (h/9.0)*K0)
        K2 = differentialEquation(t + h/6.0, f + (h/24.0)*(K0 + 3.0*K1))
        K3 = differentialEquation(t + h/4.0, f + (h/16.0)*(K0 + 3.0*K2))
        K4 = differentialEquation(t + h/10.0, f + (h/500.0)*(29.0*K0 + 33.0*K2 - 12.0*K3))
        K5 = differentialEquation(t + h/6.0, f + (h/972.0)*(33.0*K0 + 4.0*K3 + 125.0*K4))
        K6 = differentialEquation(t + h/2.0, f + (h/36.0)*(-21.0*K0 + 76.0*K3 + 125.0*K4 - 162.0*K5))
        K7 = differentialEquation(t + 2.0*h/3.0, f + (h/243.0)*(-30.0*K0 - 32.0*K3 + 125.0*K4 + 99.0*K6))
        K8 = differentialEquation(t + h/3.0, f + (h/324.0)*(1175.0*K0 - 3456.0*K3 - 6250.0*K4 + 8424.0*K5 + 242.0*K6 - 27.0*K7))
        K9 = differentialEquation(t + 5.0*h/6.0, f + (h/324.0)*(293.0*K0 - 852.0*K3 - 1375.0*K4 + 1836.0*K5 - 118.0*K6 + 162.0*K7 + 324.0*K8))
        K10 = differentialEquation(t + 5.0*h/6.0, f + (h/1620.0)*(1303.0*K0 - 4260.0*K3 - 6875.0*K4 + 9990.0*K5 + 1030.0*K6 + 162.0*K9))
        K11 = differentialEquation(t + h, f + (h/4428.0)*(-8595.0*K0 + 30720.0*K3 + 48750.0*K4 - 66096.0*K5 + 378.0*K6 - 729.0*K7 - 1944.0*K8 - 1296.0*K9 + 3240.0*K10))

        # Compute next step
        fNew = f + h*((41.0/480.0)*K0 + (9.0/35.0)*K5 + (34.0/105.0)*K6 + (9.0/280.0)*(K7 + K8) + (3.0/70.0)*K9 + (3.0/14.0)*K10 + (41.0/840.0)*K11)
        plt.plot([t, t+h], [f, fNew], color='magenta', linewidth=3.0)
        count += 1
        t = t0 + h * count
        f = fNew
    print(f"RK8: time = {t:.10f}  approx = {fNew:.10f} magenta")



plt.show()


