import numpy as np

print("---- Create Matrix ----")
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr)

#  Indexing
print("\n---- Indexing ----")
print("Element at row 2 column 3:", arr[1,2])

#  Extract Row
print("\n---- Extract Row ----")
print("First Row:", arr[0,:])

#  Extract Column
print("\n---- Extract Column ----")
print("Second Column:", arr[:,1])

# Sub Array (Slicing)
print("\n---- Sub Array ----")
print(arr[0:2,1:3])

#  Reshape Array
print("\n---- Reshape ----")
a = np.array([1,2,3,4,5,6])
print("1D Array:", a)

b = a.reshape(2,3)
print("2D Array:\n", b)

c = a.reshape(1,2,3)
print("3D Array:\n", c)

#  Stacking
print("\n---- Stacking ----")
x = np.array([1,2,3])
y = np.array([4,5,6])

print("Vertical Stack:\n", np.vstack((x,y)))
print("Horizontal Stack:", np.hstack((x,y)))

#  Concatenation
print("\n---- Concatenation ----")
print(np.concatenate((x,y)))