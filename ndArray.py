#ndArray in Numpy Python
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
# Show shape of the array
print(a.shape)
# Show dimentions of the array 
print(a.ndim)
# Show type of the array
print(a.dtype.name)
# Show item size please
print(a.itemsize)
# Show the size of the array
print(a.size)
# Show the type of the array 
print(type(a))