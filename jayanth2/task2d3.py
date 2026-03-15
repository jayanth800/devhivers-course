import numpy as np

#different between list and array

numbers_list = [1, 2, 3, 4, 5]
print("Python List:", numbers_list)
print(type(numbers_list))

numbers_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", numbers_array)
print(type(numbers_array))


#creating simple arrays

import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([5, 10, 15, 20, 25])

print("Array 1:", arr1)
print("Array 2:", arr2)

#atributes of arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)

print("Shape:", arr.shape)   # rows and columns
print("Size:", arr.size)     # total elements
print("Data Type:", arr.dtype)


#performance comparison of list and array

import numpy as np
import time

# Python list
list_data = list(range(1000000))
start = time.time()
list_result = [x*2 for x in list_data]
end = time.time()
print("List time:", end-start)

# NumPy array
array_data = np.array(list_data)
start = time.time()
array_result = array_data * 2
end = time.time()
print("Array time:", end-start)