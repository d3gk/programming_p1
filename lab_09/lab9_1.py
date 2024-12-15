
# importing
import numpy as np

# creating 7x7 matrix of zeros
x = np.zeros([7, 7])

# creating 7x5 matrix of 3s
y = 3*np.ones([5, 7])

# combining(?) them together
x [1:6, 0:7] = y

# logging
print(x)


