from functools import reduce

names = input("Enter student names separated by space: ").split()
scores = list(map(int, input("Enter corresponding scores: ").split()))

paired = list(zip(names, scores))
print("Student Score Pairs:", paired)

total_score = reduce(lambda x, y: x + y, scores)

print("Total Score:", total_score)
