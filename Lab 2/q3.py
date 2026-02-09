students = {}

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks

averages = {}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    averages[name] = avg

    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "D"

    print(name, "- Average:", avg, "Grade:", grade)

top_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

print("Top 2 students:")
for i in range(2):
    print(top_students[i][0], "-", top_students[i][1])
