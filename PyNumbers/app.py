import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.shape)

array = np.zeros((3, 4), dtype=int)
print(array)
array = np.ones((3, 4), dtype=int)
print(array)
array = np.full((3, 4), 5, dtype=int)
print(array)
array = np.random.random((3, 4))
print(array)
print(array[0, 0])
print(array > 0.5)
print(array[array > 0.2]) # returns a new array with only values greater than 0.2
print(np.sum(array))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
