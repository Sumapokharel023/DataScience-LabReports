while True:
    print("\n1. Write to file")
    print("2. Read file")
    print("3. Append to file")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            text = input("Enter text to write: ")
            file = open("menu.txt", "w")
            file.write(text + "\n")
            file.close()

        elif choice == 2:
            file = open("menu.txt", "r")
            print("File content:")
            print(file.read())
            file.close()

        elif choice == 3:
            text = input("Enter text to append: ")
            file = open("menu.txt", "a")
            file.write(text + "\n")
            file.close()

        elif choice == 4:
            print("Exiting program")
            break

        else:
            print("Invalid choice")

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Please enter a valid number")
