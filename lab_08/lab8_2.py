
# moduli import
import matplotlib.pyplot as plt
import numpy as np
import random

# random list generation
random_numbers = [random.randint(10, 20) for _ in range(10000)]

# drawing the graph
plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=11, color='skyblue', edgecolor='black')
plt.title('Гістограма розподілу випадкових чисел (10-20)')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


