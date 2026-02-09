paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
unique_words = set(words)

sorted_words = sorted(unique_words)

print("Unique words:")
for word in sorted_words:
    print(word)

print("Total unique words:", len(unique_words))
