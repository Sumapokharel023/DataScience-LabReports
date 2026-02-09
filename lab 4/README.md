# Lab 4: Advanced Techniques in Python

This lab introduces **advanced Python programming techniques** such as sorting methods, list comprehensions, generators, random sampling, regular expressions, and functional programming concepts. These exercises help improve code efficiency, readability, and real-world applicability.

Each question is implemented as a separate Python program.
 
---

## Questions and Code Links

### Question 1: Sorting Student Marks
File: [q1.py](q1.py)

Write a Python script that takes a list of student marks and sorts them in descending order (highest to lowest) using either the `sorted()` function or the `.sort()` method.

---

### Question 2: Even Numbers Using List Comprehension
File: [q2.py](q2.py)

Use a list comprehension to create a new list containing only the even numbers between 1 and 20, demonstrating a concise and readable alternative to traditional loops.

---

### Question 3: Generator Function with yield
File: [q3.py](q3.py)

Create a generator function using the `yield` keyword that produces numbers from 1 to 5 one by one to illustrate how lazy evaluation can save memory when dealing with large datasets.

---

### Question 4: Random Volunteer Selection
File: [q4.py](q4.py)

Write a Python script that takes a list of six student names and uses the `random.sample()` function to randomly select exactly three volunteers for a presentation, ensuring that no student is selected more than once.

---

### Question 5: Extracting Capitalized Words Using Regular Expressions
File: [q5.py](q5.py)

Use the `re` module to write a script that searches through a paragraph and extracts all words that start with an uppercase letter, such as proper nouns or sentence starters.

---

### Question 6: Pairing Names and Scores Using zip() and reduce()
File: [q6.py](q6.py)

Given a list of student names and a list of their corresponding scores:
- Use the `zip()` function to pair names with scores  
- Apply the `reduce()` function from the `functools` module to calculate the total sum of all scores  



