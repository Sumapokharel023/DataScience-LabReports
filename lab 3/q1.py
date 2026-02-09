try:
    file = open("sample.txt", "w")
    file.write("Hello World\n")
    file.write("This is Lab 3\n")
    file.write("File Handling in Python\n")
    file.close()

    file = open("sample.txt", "r")
    content = file.read()
    print("File Contents:")
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:", e)
