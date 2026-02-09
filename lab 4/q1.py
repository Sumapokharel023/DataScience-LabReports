marks = list(map(int, input("Enter student marks separated by space: ").split()))

marks.sort(reverse=True)
print("Marks in descending order:", marks)
