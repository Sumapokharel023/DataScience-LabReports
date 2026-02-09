import csv
try:
    file = open("students.csv", "r")
    reader = csv.reader(file)

    print("Student Records:")
    for row in reader:
        try:
            roll = int(row[0])
            name = row[1]
            marks = float(row[2])
            print(roll, name, marks)
        except (ValueError, IndexError):
            print("Invalid data found")

    file.close()

except FileNotFoundError:
    print("CSV file not found")
except Exception as e:
    print("Error:", e)
