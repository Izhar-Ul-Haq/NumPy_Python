import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)
c = a-b
a = a**2
b = b**3
print(a)
print(b)
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print("The A Matrix:",A)
print("The B Matrix:",B)
C = A*B
print("The C Matrix:", C)