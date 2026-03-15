#string slicing

sentence = "Python programming is very interesting"

words = sentence.split()

first_word = words[0]
last_word = words[-1]
middle_words = words[1:-1]

print("Sentence:", sentence)
print("First word:", first_word)
print("Last word:", last_word)
print("Middle words:", middle_words)


#string formating
name = "jayanth"
age = 17
course = "Python"

message = f"My name is {name}, I am {age} years old and I am learning {course}."

print(message)


#uppercase and lowercase
text = "Python Is Fun To Learn"

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


#replace words
sentence = "I like Java programming"

new_sentence = sentence.replace("Java", "Python")

print("Original:", sentence)
print("After Replace:", new_sentence)


#split and join
sentence = "apple banana mango orange"

# Split string into list
fruits = sentence.split()

print("Split result:", fruits)

# Join list into string
new_sentence = "-".join(fruits)

print("Joined string:", new_sentence)