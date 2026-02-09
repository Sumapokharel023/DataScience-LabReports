# Lab 5: Pandas Basics and Data Handling

This lab introduces the fundamentals of **data analysis using the Pandas library**. The exercises focus on creating and manipulating DataFrames, handling missing and duplicate data, detecting outliers, transforming columns, and saving cleaned datasets.

Each question is implemented as a separate Python program using Pandas.


---

## Questions and Code Links

### Question 1: DataFrame Creation
File: [q1.py](q1.py)

Import Pandas and create a DataFrame with the following columns:
- Name  
- Age  
- Marks  

The program:
- Displays the first five rows of the DataFrame  
- Displays the shape of the dataset  

---

### Question 2: Loading a CSV File
File: [q2.py](q2.py)

Load a CSV file into a Pandas DataFrame and:
- Display column names  
- Display data types of each column  
- Display basic statistical information  

---

### Question 3: Filtering Data
File: [q3.py](q3.py)

Select and display:
- Rows where `Marks > 60`  
- Only the `Name` and `Marks` columns from the filtered data  

---

### Question 4: Handling Missing Values
File: [q4.py](q4.py)

The program:
- Checks for missing values in the dataset  
- Fills missing numerical values using the mean of the respective columns  

---

### Question 5: Duplicate Data Handling
File: [q5.py](q5.py)

The program:
- Detects duplicate rows in the dataset  
- Removes duplicate rows  
- Verifies the dataset after removal  

---

### Question 6: Outlier Detection Using IQR
File: [q6.py](q6.py)

Identify outliers in the `Marks` column using the **Interquartile Range (IQR) method** and:
- Remove the detected outliers  
- Display the cleaned dataset  

---

### Question 7: Data Transformation and Export
File: [q7.py](q7.py)

The program:
- Creates a new column by transforming `Marks` (e.g., `Marks / 10`)  
- Renames columns where necessary  
- Saves the cleaned dataset to a new CSV file  


