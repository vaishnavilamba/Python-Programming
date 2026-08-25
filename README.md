# 🐍 Python & Data Analysis Learning Journey

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-Learning-orange?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Learning-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-success?style=for-the-badge" />
</p>

<p align="center">
  <b>A structured journey from Python fundamentals to Data Analysis with Python.</b>
  <br>
  Learning concepts • Writing code • Solving problems • Working with data
</p>

---

## 📌 About This Repository

This repository contains my **Python learning journey**, starting from the fundamentals and gradually moving toward **advanced Python concepts and Data Analysis**.

I am building this repository topic by topic rather than simply learning syntax. Each section contains examples, practice programs, exercises, and implementations that help me understand how Python works in real programming scenarios.

The main objective is to build a strong foundation in Python before moving deeper into **Data Science, Machine Learning, and AI-related technologies**.

---

# 🗺️ Learning Roadmap

```text
                    PYTHON
                       │
                       ▼
              ┌─────────────────┐
              │ Python Basics   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Control Flow    │
              └────────┬────────┘
                       │
                       ▼
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Lists          Tuples          Sets
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Dictionaries
                       │
                       ▼
                   Functions
                       │
                       ▼
             Modules & Packages
                       │
                       ▼
                File Handling
                       │
                       ▼
              Exception Handling
                       │
                       ▼
                    OOP
                       │
                       ▼
              Advanced Python
                       │
                       ▼
              Data Analysis
                 ┌─────┴─────┐
                 ▼           ▼
               NumPy       Pandas
                 │           │
                 └─────┬─────┘
                       ▼
                Data Manipulation
```

---

# 📚 Topics Covered

## 1️⃣ Python Basics

The first stage focuses on understanding the fundamental building blocks of Python.

### Topics

* Python introduction
* Python syntax
* Variables
* Constants
* Data types
* Type checking
* Type conversion
* Input and output
* Operators
* Arithmetic operators
* Comparison operators
* Logical operators
* Assignment operators
* Membership operators
* Identity operators
* Strings
* String indexing
* String slicing
* String methods
* Basic Python programs

### Example

```python
name = "Vaishnavi"
age = 21

print("Name:", name)
print("Age:", age)
```

---

# 2️⃣ Control Flow

Control flow allows a program to make decisions and execute different blocks of code depending on conditions.

### Topics

* `if`
* `if-else`
* `if-elif-else`
* Nested conditions
* `for` loop
* `while` loop
* `break`
* `continue`
* `pass`
* Nested loops
* Practical problems using loops and conditions

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
else:
    print("Needs Improvement")
```

---

# 3️⃣ Lists

Lists are one of the most commonly used Python data structures.

### Topics

* Creating lists
* Indexing
* Negative indexing
* Slicing
* Updating elements
* Adding elements
* Removing elements
* `append()`
* `insert()`
* `extend()`
* `remove()`
* `pop()`
* `sort()`
* `reverse()`
* List traversal
* Nested lists
* List comprehension

### Example

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 4️⃣ Tuples

Tuples are ordered and immutable collections in Python.

### Topics

* Creating tuples
* Tuple indexing
* Tuple slicing
* Tuple packing
* Tuple unpacking
* Tuple methods
* Difference between List and Tuple
* Immutability

### Example

```python
student = ("Vaishnavi", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)
```

---

# 5️⃣ Sets

Sets are unordered collections of **unique elements**.

### Topics

* Creating sets
* Adding elements
* Removing elements
* Set operations
* Union
* Intersection
* Difference
* Symmetric difference
* Membership testing
* Removing duplicate values

### Example

```python
numbers = {1, 2, 2, 3, 4, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

---

# 6️⃣ Dictionaries

Dictionaries store data in **key-value pairs**.

### Topics

* Creating dictionaries
* Accessing values
* Adding key-value pairs
* Updating values
* Removing elements
* `keys()`
* `values()`
* `items()`
* `get()`
* Dictionary traversal
* Nested dictionaries
* Dictionary comprehension

### Example

```python
student = {
    "name": "Vaishnavi",
    "age": 21,
    "branch": "CSE"
}

print(student["name"])
```

Output:

```text
Vaishnavi
```

---

# 7️⃣ Functions

Functions allow code to be organized into reusable blocks.

### Topics

* Defining functions
* Calling functions
* Function parameters
* Arguments
* Return values
* Default arguments
* Keyword arguments
* Positional arguments
* Variable-length arguments
* `*args`
* `**kwargs`
* Scope of variables
* Local variables
* Global variables
* Lambda functions
* Recursive functions
* Higher-order functions
* Function practice problems

### Example

```python
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)

print(result)
```

Output:

```text
30
```

---

# 8️⃣ Modules & Packages

This section focuses on organizing Python code into reusable modules and packages.

### Topics

* What are modules?
* Creating custom modules
* Importing modules
* `import`
* `from ... import`
* Aliases
* Built-in modules
* Packages
* Installing packages using `pip`
* `requirements.txt`
* Working with external libraries

### Example

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# 9️⃣ File Handling in Python

File handling allows Python programs to store and retrieve information from files.

### Topics

* Opening files
* Reading files
* Writing files
* Appending data
* File modes
* `open()`
* `read()`
* `readline()`
* `readlines()`
* `write()`
* `writelines()`
* `with` statement
* Working with text files
* File paths
* Basic file-processing programs

### Example

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

Using `with` is preferred because Python automatically handles closing the file.

---

# 🔟 Exception Handling

Exception handling allows programs to deal with unexpected situations without crashing unnecessarily.

### Topics

* Errors vs Exceptions
* `try`
* `except`
* `else`
* `finally`
* Multiple exceptions
* Custom exceptions
* `raise`
* Handling user input errors
* Practical exception-handling programs

### Example

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 1️⃣1️⃣ Object-Oriented Programming — OOP

Object-Oriented Programming is used to structure programs around **classes and objects**.

### Topics

* Classes
* Objects
* Constructors
* `__init__()`
* Instance variables
* Methods
* Public variables
* Protected variables
* Private variables
* Encapsulation
* Getters
* Setters
* Inheritance
* Method overriding
* Polymorphism
* Abstraction
* Abstract classes
* Abstract methods
* `ABC`
* `abstractmethod`
* Operator overloading
* Magic/Dunder methods

### Example

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


person = Person("Vaishnavi", 21)

person.display()
```

---

# 1️⃣2️⃣ Advanced Python

This section moves beyond basic Python programming into more powerful language features.

### Topics

* Iterators
* Iterables
* Generators
* `yield`
* Generator expressions
* Advanced functions
* Decorators
* Comprehensions
* Advanced function concepts
* Memory-efficient programming
* Pythonic programming techniques

### 🔄 Iterators

An iterator is an object that allows us to traverse through elements one at a time.

### 🔄 Generators

Generators produce values **one at a time** using the `yield` keyword.

```python
def numbers():
    for i in range(5):
        yield i

for number in numbers():
    print(number)
```

### Why are generators useful?

Generators are especially useful when working with:

* Large datasets
* Data processing
* File processing
* Data pipelines
* Memory-intensive operations

---

# 1️⃣3️⃣ Data Analysis with Python

This is the current stage of the learning journey.

The focus is on learning how Python can be used to **load, manipulate, analyze, summarize, and understand data**.

The major libraries being explored are:

* **NumPy**
* **Pandas**

---

## 🔢 NumPy

**NumPy (Numerical Python)** is a library used for numerical computing and working efficiently with arrays.

### Topics

* Installing NumPy
* Importing NumPy
* NumPy arrays
* `ndarray`
* One-dimensional arrays
* Multi-dimensional arrays
* Array indexing
* Array slicing
* Array dimensions
* Array shape
* Array size
* Array data type
* Array reshaping
* Array operations
* Mathematical operations
* Statistical operations
* Built-in array creation functions

### Important NumPy Functions

```python
np.array()
np.arange()
np.zeros()
np.ones()
np.linspace()
np.random
```

### Statistical Concepts

* Mean
* Median
* Variance
* Standard deviation
* Normalization
* Standardization

### Example

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
```

---

# 🐼 Pandas

**Pandas** is a Python library mainly used for **data manipulation and data analysis**.

It provides two important data structures:

### Series

A one-dimensional labeled data structure.

```python
import pandas as pd

marks = pd.Series([80, 90, 75, 88])

print(marks)
```

### DataFrame

A two-dimensional tabular data structure consisting of rows and columns.

```python
data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)
```

---

## 📊 Pandas Topics

### DataFrame Operations

* Creating DataFrames
* Reading data
* Inspecting data
* Selecting columns
* Selecting rows
* Indexing
* Slicing
* Adding columns
* Updating columns
* Removing columns
* Sorting data
* Filtering data

### `loc` and `iloc`

Learning different ways to access DataFrame data.

```python
df.loc[0, "Name"]
```

uses **labels**, while:

```python
df.iloc[0, 0]
```

uses **integer positions**.

---

## 📈 Data Aggregation

Data aggregation means **combining multiple data values to produce a meaningful summary**.

Common aggregation operations include:

```python
df["Marks"].sum()
df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].count()
```

### Group-Based Aggregation

A major Pandas concept is:

```python
groupby()
```

It allows data to be divided into groups and analyzed separately.

For example:

```text
Department
     │
     ├── CSE
     ├── ECE
     └── ME
```

We can calculate the average salary, total sales, or number of employees for each department.

---

# 🧮 Data Preprocessing Concepts

As part of the Data Analysis journey, I am also learning important concepts used before Machine Learning.

### Statistical Concepts

* Mean
* Median
* Variance
* Standard Deviation
* Normalization
* Standardization

### Standardization

Standardization transforms data so that it generally has:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

The commonly used formula is:

```text
z = (x - μ) / σ
```

where:

* `x` = original value
* `μ` = mean
* `σ` = standard deviation
* `z` = standardized value

---

# 📁 Repository Structure

The repository is organized topic-wise so that each concept has its own section.

```text
Python/
│
├── 1-python-Basics/
│
├── 2-Control_Flow/
│
├── 3-Lists/
│
├── 4-Tuple/
│
├── 5-Sets/
│
├── 6-Dictionaries/
│
├── 7-Functions/
│
├── 8-ModulesAndPackages/
│
├── 9-FileHandlingInPython/
│
├── 10-ExceptionHandling/
│
├── 11-OOPS/
│
├── 12-AdvancePython/
│
├── 13-Data-Analysis-With-Python/
│
├── .gitignore
│
├── README.md
│
└── requirements.txt
```

---

# 🛠️ Tools & Technologies

| Tool / Technology      | Purpose                          |
| ---------------------- | -------------------------------- |
| 🐍 Python              | Core programming language        |
| 🔢 NumPy               | Numerical computing              |
| 🐼 Pandas              | Data manipulation & analysis     |
| 💻 VS Code             | Development environment          |
| 🌱 Virtual Environment | Dependency isolation             |
| 📦 pip                 | Python package management        |
| 🔧 Git                 | Version control                  |
| 🐙 GitHub              | Repository & project management  |
| 📊 CSV / Excel         | Working with structured datasets |

---

# 🎯 Learning Objectives

Through this repository, I aim to:

* Build strong Python fundamentals
* Understand Python data structures
* Write clean and reusable Python programs
* Understand Object-Oriented Programming
* Learn advanced Python concepts
* Work with files and exceptions
* Manipulate real-world datasets
* Understand NumPy arrays and numerical operations
* Learn Pandas for data analysis
* Understand statistical concepts used in data preprocessing
* Develop problem-solving skills
* Build a strong foundation for Machine Learning and AI

---

# 🧪 Learning Approach

I am following a **learn → implement → practice → analyze** approach.

```text
        📖 Learn Concept
              ↓
        💻 Write Code
              ↓
        🧪 Practice
              ↓
       📊 Work With Data
              ↓
       🧠 Understand Why
              ↓
        🚀 Build Projects
```

The purpose of this repository is not to collect code blindly. Every topic is practiced through examples and exercises to develop a deeper understanding of Python.

---

# 📈 Progress Tracker

| #  | Topic                     | Status         |
| -- | ------------------------- | -------------- |
| 1  | Python Basics             | ✅ Completed    |
| 2  | Control Flow              | ✅ Completed    |
| 3  | Lists                     | ✅ Completed    |
| 4  | Tuples                    | ✅ Completed    |
| 5  | Sets                      | ✅ Completed    |
| 6  | Dictionaries              | ✅ Completed    |
| 7  | Functions                 | ✅ Completed    |
| 8  | Modules & Packages        | ✅ Completed    |
| 9  | File Handling             | ✅ Completed    |
| 10 | Exception Handling        | ✅ Completed    |
| 11 | OOP                       | ✅ Completed    |
| 12 | Advanced Python           | ✅ Completed    |
| 13 | Data Analysis with Python | 🔄 In Progress |

---

# 🚀 What's Next?

After strengthening Python and Data Analysis fundamentals, the next stage of the journey will focus on:

```text
Data Analysis
      ↓
Data Visualization
      ↓
Data Preprocessing
      ↓
Machine Learning Fundamentals
      ↓
Supervised Learning
      ↓
Unsupervised Learning
      ↓
Deep Learning
      ↓
Real-World Projects
```

Potential technologies and libraries:

* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow / PyTorch
* Jupyter Notebook
* SQL
* Machine Learning algorithms

---

# 💡 Key Learning Philosophy

> **Don't just memorize the syntax. Understand what happens behind the syntax.**

For every concept, the goal is to understand:

```text
What is it?
     ↓
Why do we need it?
     ↓
How does it work?
     ↓
How do we implement it?
     ↓
Where is it used in real life?
```

---

# 📌 Repository Status

**Current Stage:** Data Analysis with Python

**Python Fundamentals:** Completed ✅

**OOP:** Completed ✅

**Advanced Python:** Completed ✅

**NumPy:** Learning / Practicing 🔄

**Pandas:** Learning / Practicing 🔄

**Data Analysis:** In Progress 🔄

---

# 👩‍💻 Author

**Vaishnavi**

B.Tech CSE Student

This repository represents my continuous journey of learning Python, strengthening programming fundamentals, and moving toward data-driven technologies.

---

## ⭐ If you find this repository useful

Feel free to explore the individual topic folders and follow the learning journey from **Python fundamentals to Data Analysis**.

> **Learn consistently. Practice deeply. Build continuously.**
