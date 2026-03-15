import numpy as np

print("---- Matrix Creation ----")

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)


#  Matrix Addition
print("\n---- Matrix Addition ----")
print(A + B)


#  Matrix Subtraction
print("\n---- Matrix Subtraction ----")
print(A - B)


#  Matrix Multiplication
print("\n---- Matrix Multiplication ----")
print(np.dot(A, B))


#  Generate Random Numbers
print("\n---- Random Numbers ----")
rand_numbers = np.random.rand(5)
print(rand_numbers)


#  Generate Random Matrix
print("\n---- Random Matrix ----")
rand_matrix = np.random.randint(1, 10, (3,3))
print(rand_matrix)


#  Dice Roll Simulation
print("\n---- Dice Roll Simulation ----")
dice_roll = np.random.randint(1,7,10)
print("10 Dice Rolls:", dice_roll)


#  Random Sampling (Example: Selecting Students)
print("\n---- Random Sampling ----")
students = np.array(["Amit","Rahul","Sneha","Riya","Arjun"])
sample = np.random.choice(students,3)
print("Selected Students:", sample)