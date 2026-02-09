words = input("Enter words separated by space: ").split()

new_words = []
for word in words:
    if len(word) % 2 == 0:
        new_words.append(word[::-1])
    else:
        new_words.append(word)

print("Processed words:")
print(new_words)
