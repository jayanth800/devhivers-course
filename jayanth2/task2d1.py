#LIST Examples (fruits)
fruits = ["apple","banana","mango","grapes"]

print("List of fruits:",fruits)


 # List are mutable (can change)
fruits.append("orange")
print("After adding fruit:",fruits)

#TUOPLES Example (numbers)
numbers = (10, 20, 30, 40)


print("Tuples of numbers:", numbers)

# Access element
print("First number:", numbers[0])


#SET Example
fruit_set = {"apple","banan","mango","grapes"}

print("Set of fruits:", fruit_set)


# Add element
fruit_set.add("orange")
print("After adding:", fruit_set)


# Dictionary Example
student = {
    "name": "Ravi",
    "grade": "A",
    "age": 17
}

print("Student Info:", student)


students = {
    "Rahul": 85,
    "Anita": 90,
    "Kiran": 78
}

print("Student Grades:")

for name, grade in students.items():
    print(name, ":", grade)


fruits = ["apple", "banana", "apple", "mango"]

fruit_set = set(fruits)

print("List:", fruits)
print("Converted to Set:", fruit_set)


numbers = (10, 20, 30)

num_list = list(numbers)

print("Tuple:", numbers)
print("Converted to List:", num_list)