text = input("Enter a paragraph: ")

# Count words
words = text.split()
word_count = len(words)

# Count characters (excluding spaces)
char_count = len(text.replace(" ", ""))

# Count sentences
sentence_count = text.count('.') + text.count('!') + text.count('?')

print("Word count:", word_count)
print("Character count:", char_count)
print("Sentence count:", sentence_count)