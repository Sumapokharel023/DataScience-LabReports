age = int(input("Enter your age: "))
current_year = 2025

birth_year = current_year - age
print("Birth Year:", birth_year)

if (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0):
    print("Birth year was a Leap Year")
else:
    print("Birth year was not a Leap Year")
