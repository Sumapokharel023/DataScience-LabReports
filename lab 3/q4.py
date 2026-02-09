import json

student = {
    "id": 1,
    "name": "Suma",
    "marks": 85
}

try:
    file = open("student.json", "w")
    json.dump(student, file)
    file.close()

    file = open("student.json", "r")
    data = json.load(file)
    file.close()

    print("Student Information:")
    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Marks:", data["marks"])

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Error decoding JSON file")
