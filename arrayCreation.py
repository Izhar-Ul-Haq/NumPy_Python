import numpy as np
a = np.array([1,2,3,4,5])
# Show array
print(a)
# Show the type of array
print(type(a))
# Show how many elements are there in the array 
print(a.size)
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
# We are gonna create an array and convert the type into complex
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
# Zeros matrix
print(np.zeros((3, 4)))
# Ones Matrix
print(np.ones((3, 4)))
# Create array sequence. For it we use arange function in numpy
print(np.arange(10, 30, 5))
# Arrange function can also be used with float numbers
print(np.arange(0, 2, 0.3))
print(np.arange(10000))