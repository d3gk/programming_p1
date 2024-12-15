
# imports
import matplotlib.pyplot as plt
import numpy as np


def gencircpnts(radius, pointscnt=100):
    theta = np.linspace(0, 2 * np.pi, pointscnt)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y

plt.figure(figsize=(8, 8))

# Circle 1 (rad=1)
x1, y1 = gencircpnts(1)
plt.scatter(x1, y1, color='red', s=10, label='Коло радіусом 1')

# Circle 2 (rad=2)
x2, y2 = gencircpnts(2)
plt.scatter(x2, y2, color='green', s=10, label='Коло радіусом 2')

# Circle 3 (rad=3)
x3, y3 = gencircpnts(3)
plt.scatter(x3, y3  , color='blue', s=10, label='Коло радіусом 3')
    
plt.title('Три кола різного діаметра')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


