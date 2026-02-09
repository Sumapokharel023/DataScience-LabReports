def number_generator():
    for i in range(1, 6):
        yield i

print("Generated numbers:")
for num in number_generator():
    print(num)
