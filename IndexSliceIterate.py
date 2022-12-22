import numpy as np
a = np.arange(10)**3
print(a)
print(a[2:5]) # Should print 8, 27, 64
a[:6:2] = 1000 # [1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729]
print(a)
print(a[::-1])  # reversed a