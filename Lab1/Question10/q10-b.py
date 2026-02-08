print("Enter height format:")
print("1. Centimeters")
print("2. Feet and Inches")
h_choice = int(input("Choice: "))

if h_choice == 1:
    height_cm = float(input("Enter height in cm: "))
    height_m = height_cm / 100
else:
    feet = int(input("Enter feet: "))
    inches = int(input("Enter inches: "))
    height_m = (feet * 0.3048) + (inches * 0.0254)

print("Enter weight format:")
print("1. Kilograms")
print("2. Pounds")
w_choice = int(input("Choice: "))

if w_choice == 1:
    weight = float(input("Enter weight in kg: "))
else:
    weight = float(input("Enter weight in pounds: ")) * 0.453592

bmi = weight / (height_m ** 2)
print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
