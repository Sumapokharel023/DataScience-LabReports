import random

students = input("Enter 6 student names separated by space: ").split()

volunteers = random.sample(students, 3)

print("Selected Volunteers:")
for v in volunteers:
    print(v)
