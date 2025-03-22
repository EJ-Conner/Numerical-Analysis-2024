import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

f = 3*x**2 - 3*x + 4
f_prime = sp.diff(f, x)
print(f)
print(f_prime)

zeros = sp.solve(f_prime, x)
print(zeros)


function = sp.lambdify(x, f)
function_prime = sp.lambdify(x, f_prime)
x_points = np.arange(-2,2.6, .1)
y_points = function(x_points)
y_prime_points = function_prime(x_points)

plt.plot(x_points, y_points, label='f(x)', color='b')
plt.plot(x_points, y_prime_points, label="f'(x)", color='orange')
plt.plot(zeros, 0, 'ro', label="f'(x) zero")
plt.title('Function with Derivative and its zero')
plt.xlabel=('x axis')
plt.ylabel=('y axis')
plt.ylim(-15, 25)
plt.legend()
plt.grid()
plt.show()