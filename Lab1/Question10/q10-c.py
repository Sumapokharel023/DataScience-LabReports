age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))

if age >= 18 and age <= 40 and bmi >= 18.5 and bmi <= 29.9:
    print("Eligible for Army Entrance")
else:
    print("Not Eligible for Army Entrance")
