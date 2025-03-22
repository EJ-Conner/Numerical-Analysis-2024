import math
from matplotlib import pyplot as plt

# Set size of figure
plt.figure(figsize=(10, 10))

# Define the axes
fStart = -7.0
fStop = 7.0
gStart = -7.0
gStop = 7.0
plt.axis([fStart, fStop, gStart, gStop])
plt.xlabel('f', fontsize=15)
plt.ylabel('g', fontsize=15)

# Different phase planes
#plt.title("Phase Plane for f' = f, g' = 3g", fontsize=15)
plt.title("Phase Plane for f' = g/2, g' = -2*f", fontsize=15)
#plt.title("Phase Plane for f' = -5*f + 2*g, g' = f - 4*g", fontsize=15)
#plt.title("Phase Plane for f' = 2*f - g, g' = f + 2*g", fontsize=15)
#plt.title("Phase Plane for f' = 5*f - 3*g, g' = 4*f - 3*g", fontsize=15)
#plt.title("Phase Plane for f' = -1*g, g' = f-g", fontsize=15)

# Define the differential equations
def f_prime(f, g):
  # pick f' here
   # return f
    return g/2
   # return -5*f + 2*g
   # return 2*f - g
   # return 5*f - 3*g
   # return -1*g


def g_prime(f, g):
  # pick g' here
   # return 3*g
    return -2*f
   # return f - 4*g
   # return f + 2*g
   # return 4*f - 3*g
   # return f-g

# Grid step size
gridf = 0.5
gridg = 0.5

# Generate the phase plane
f = fStart
while f <= fStop:
    g = gStart
    while g <= gStop:
        plt.plot([f], [g], 'ko', ms=1.5)
        df = f_prime(f, g) * gridf
        dg = g_prime(f, g) * gridg
        length = math.sqrt(df**2 + dg**2)

        # Skip vector scaling to avoid division by zero if crit point is at 0
        if length != 0:
            vectorScaling = 0.3 * (gridf / length)  # Scale vectors for better visualization
            plt.arrow(f, g, df * vectorScaling, dg * vectorScaling, head_width=0.1, head_length=0.1, fc='blue', ec='blue')

        g += gridg
    f += gridf


plt.show()

