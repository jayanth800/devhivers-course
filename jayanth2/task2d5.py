import numpy as np

print("---- Create Arrays ----")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Array A:", a)
print("Array B:", b)


#  Element-wise operations
print("\n---- Element-wise Operations ----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)


#  Basic statistics
print("\n---- Basic Statistics ----")
data = np.array([12, 15, 18, 20, 22])

print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Standard Deviation:", np.std(data))


#  Matrix operations
print("\n---- Matrix Example ----")
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Matrix:\n", matrix)

# Row and column aggregates
print("\nRow Sum:", np.sum(matrix, axis=1))
print("Column Sum:", np.sum(matrix, axis=0))


#  Row and column mean
print("\nRow Mean:", np.mean(matrix, axis=1))
print("Column Mean:", np.mean(matrix, axis=0))


#  Statistical analysis on dataset (Exam Scores)
print("\n---- Exam Scores Dataset ----")

scores = np.array([78, 85, 90, 66, 74, 88, 92])

print("Scores:", scores)
print("Average Score:", np.mean(scores))
print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))
print("Standard Deviation:", np.std(scores))