import math
import matplotlib.pyplot as plt
import numpy as np


center = np.pi

plt.figure(figsize=(8, 8))
plt.xlim(-center, 3 * center)
plt.ylim(-1.5, 1.5)

# Taylor series of nth taylor polynomial approx of func
def Ty(x, n, a, center): # x is input values where polynomial is calc.
  p = a[n]
  for i in range(n-1, -1, -1):
    p = a[i] + p*(x-center)
  return p

a = [0 for _ in range(12)]

for i in range(0, len(a)//2):
  a[2*i+1] = (-1)**(i+1)/math.factorial(2*i+1)



# x values
x = np.linspace(-center, 3* center, 100)
y = np.sin(x)

y_t0 = Ty(x, 0, a, center)
y_t1 = Ty(x, 1, a, center)
y_t3 = Ty(x, 3, a, center)
y_t5 = Ty(x, 5, a, center)


# Plotting
dx = 0.1
# xs = np.arange(-c, 3*c, dx)
plt.plot(x, y, color = 'blue', label = 'sin(x)')

colors = ['green', 'yellow', 'pink', 'orange', 'red', 'purple']
for i in range(6):
  plt.plot(x, [Ty(xx, 2*i+1, a, center) for xx in x], color = colors[i], label = f'T{i}(x)')


plt.axvline(x = center, color = 'black', linestyle = ':', label = 'x = π')
plt.title('Taylor Series Approximations of sin(x) Centered at π')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
