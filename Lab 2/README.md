# Lab 2: Data Structures in Python

This lab focuses on using **Python data structures** such as lists, tuples, sets, and dictionaries to solve real-world–inspired problems. The exercises emphasize data manipulation, aggregation, and logical validation.

Each question is implemented as a separate Python program.

---

## Questions and Code Links

### Question 1: Movie Ratings Analyzer
File: [q1.py](q1.py)

Ask the user to input a list of movies with ratings, for example:
`[("Titanic", 8), ("Inception", 9)]`

The program:
- Computes the average rating  
- Finds the highest-rated movie  
- Lists all movies with ratings above the average  

---

### Question 2: Unique Words Collector
File: [q2.py](q2.py)

Take a paragraph as input from the user and:
- Split it into words  
- Remove duplicate words  
- Sort them alphabetically  
- Count the total number of unique words  

---

### Question 3: Student Marks Manager
File: [q3.py](q3.py)

Store student names as keys and a list of marks as values in a dictionary.

The program:
- Computes each student’s average marks  
- Assigns grades (A / B / C / D)  
- Prints the top 2 students based on average marks  

---

### Question 4: Inventory Tracker
File: [q4.py](q4.py)

Simulate a small store inventory, for example:
`{"apple": 10, "banana": 5, "milk": 2}`

The program allows:
- Adding new items  
- Selling items (reducing quantity)  
- Printing items that are low in stock (quantity < 3)  

---

### Question 5: Word Reverser Game
File: [q5.py](q5.py)

Ask the user for a list of words.

The program:
- Reverses a word only if its length is even  
- Prints the new list after processing  

---

### Question 6: Simple Path Validator
File: [q6.py](q6.py)

Represent a map using a dictionary, for example:
`{"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}`

The program:
- Takes a path input from the user (e.g., `["A", "C", "D"]`)  
- Checks whether each consecutive step is connected  
- Prints **"Valid path"** or **"Invalid path"**  


