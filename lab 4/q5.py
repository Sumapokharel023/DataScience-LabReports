import re

paragraph = input("Enter a paragraph: ")

words = re.findall(r'\b[A-Z][a-zA-Z]*\b', paragraph)

print("Words starting with uppercase letter:")
print(words)
