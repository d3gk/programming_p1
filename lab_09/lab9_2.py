
import numpy as nmp

# generating matrix
mtrx = nmp.random.randint(1, 4, size = [3, 3])

# function, which calculates determinant
def manual_det(x):
    return (x[0, 0] * x[1, 1] * x[2, 2] +      x[0, 1] * x[1, 2] * x[2, 0] +
      x[0, 2] * x[1, 0] * x[2, 1] -      x[0, 2] * x[1, 1] * x[2, 0] -
      x[0, 1] * x[1, 0] * x[2, 2] -      x[0, 0] * x[1, 2] * x[2, 1])

# reference
dt = nmp.linalg.det(mtrx)

# log
print(mtrx)
print(dt)
print(manual_det(mtrx))

