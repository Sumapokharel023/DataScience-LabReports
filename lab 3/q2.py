numbers = []

try:
    file = open("numbers.txt", "r")
    for line in file:
        try:
            num = float(line.strip())
            numbers.append(num)
        except ValueError:
            pass   # Ignore invalid entries
    file.close()

    if len(numbers) > 0:
        total = sum(numbers)
        average = total / len(numbers)
        print("Sum:", total)
        print("Average:", average)
    else:
        print("No valid numbers found")

except FileNotFoundError:
    print("numbers.txt file not found")
