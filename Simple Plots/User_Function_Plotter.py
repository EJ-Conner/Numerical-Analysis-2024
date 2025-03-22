import matplotlib.pyplot as plt
import numpy as np

# user input
min = float(input("Enter a min: "))
max = float(input("Enter a max: "))
step = float(input("Enter a step: "))

x = np.arange(min, max, step)
yinput = input("Enter an expression (such as x**2): ")
y = eval(yinput)

plt.plot(x, y, label='Function', linewidth=2, color='b')
plt.xlim(min - 5, max + 5)
plt.title('Function Output')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()



