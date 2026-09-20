# 🐍 Python & Data Analysis Learning Journey


<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />

<img src="https://img.shields.io/badge/NumPy-Learning-orange?style=for-the-badge&logo=numpy&logoColor=white" />

<img src="https://img.shields.io/badge/Pandas-Learning-150458?style=for-the-badge&logo=pandas&logoColor=white" />

<img src="https://img.shields.io/badge/Flask-Learning-black?style=for-the-badge&logo=flask&logoColor=white" />

<img src="https://img.shields.io/badge/Streamlit-Learning-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />

<img src="https://img.shields.io/badge/Scikit--Learn-Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />

<img src="https://img.shields.io/badge/Status-In%20Progress-success?style=for-the-badge" />

</p>

<p align="center">

<b>A structured journey from Python fundamentals to Data Analysis, Web Development and Machine Learning applications.</b>

<br>

Learning concepts • Writing code • Practicing • Working with data • Building applications

</p>

---

# 📌 About This Repository

This repository contains my **Python learning journey**, starting from Python fundamentals and gradually progressing toward advanced Python concepts, data analysis, web development, and machine learning applications.

I am building this repository topic by topic rather than simply learning syntax.

Each section contains examples, practice programs, exercises, notebooks, and implementations that help me understand how Python works in real programming scenarios.

The main goal is to build a strong Python foundation and use it for:

- Programming
- Data Analysis
- Data Visualization
- Web Development
- Machine Learning
- Machine Learning Applications

---

# 🗺️ Learning Roadmap

```text
                         PYTHON
                           │
                           ▼
                  Python Fundamentals
                           │
                           ▼
                     Control Flow
                           │
                           ▼
              Python Data Structures
                           │
          ┌────────┬───────┼────────┐
          ▼        ▼       ▼        ▼
        Lists    Tuples   Sets   Dictionaries
          │        │       │        │
          └────────┴───────┴────────┘
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
                  Memory Management
                           │
                           ▼
                    Data Analysis
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
                NumPy             Pandas
                  │                 │
                  └────────┬────────┘
                           ▼
                  Data Visualization
                           │
                           ▼
                   Flask Framework
                           │
                           ▼
                 Streamlit Framework
                           │
                           ▼
                 Machine Learning
                           │
                           ▼
              Machine Learning Apps
                           │
                           ▼
                    Deep Learning
                           │
                           ▼
                  Real-World Projects
```

---

# 📚 Topics Covered

## 1️⃣ Python Basics

The first stage focuses on understanding the fundamental building blocks of Python.

### Topics

- Python introduction
- Python syntax
- Variables
- Constants
- Data types
- Type checking
- Type conversion
- Input and output
- Operators
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- Membership operators
- Identity operators
- Strings
- String indexing
- String slicing
- String methods
- Basic Python programs

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

- `if`
- `if-else`
- `if-elif-else`
- Nested conditions
- `for` loop
- `while` loop
- `break`
- `continue`
- `pass`
- Nested loops
- Practical problems using loops and conditions

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

- Creating lists
- Indexing
- Negative indexing
- Slicing
- Updating elements
- Adding elements
- Removing elements
- `append()`
- `insert()`
- `extend()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`
- List traversal
- Nested lists
- List comprehension

### Example

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

---

# 4️⃣ Tuples

Tuples are ordered and immutable collections in Python.

### Topics

- Creating tuples
- Tuple indexing
- Tuple slicing
- Tuple packing
- Tuple unpacking
- Tuple methods
- Difference between List and Tuple
- Immutability

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

Sets are unordered collections of unique elements.

### Topics

- Creating sets
- Adding elements
- Removing elements
- Set operations
- Union
- Intersection
- Difference
- Symmetric difference
- Membership testing
- Removing duplicate values

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

Dictionaries store data using key-value pairs.

### Topics

- Creating dictionaries
- Accessing values
- Adding key-value pairs
- Updating values
- Removing elements
- `keys()`
- `values()`
- `items()`
- `get()`
- Dictionary traversal
- Nested dictionaries
- Dictionary comprehension

### Example

```python
student = {
    "name": "Vaishnavi",
    "age": 21,
    "branch": "CSE"
}

print(student["name"])
```

---

# 7️⃣ Functions

Functions allow code to be organized into reusable blocks.

### Topics

- Defining functions
- Calling functions
- Function parameters
- Arguments
- Return values
- Default arguments
- Keyword arguments
- Positional arguments
- Variable-length arguments
- `*args`
- `**kwargs`
- Local variables
- Global variables
- Scope
- Lambda functions
- Recursive functions
- Higher-order functions
- Function practice problems

### Example

```python
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)

print(result)
```

---

# 8️⃣ Modules & Packages

This section focuses on organizing Python code into reusable modules and packages.

### Topics

- What are modules?
- Creating custom modules
- Importing modules
- `import`
- `from ... import`
- Aliases
- Built-in modules
- Packages
- Installing packages using `pip`
- `requirements.txt`
- External libraries

### Example

```python
import math

print(math.sqrt(25))
```

---

# 9️⃣ File Handling in Python

File handling allows Python programs to store and retrieve information from files.

### Topics

- Opening files
- Reading files
- Writing files
- Appending data
- File modes
- `open()`
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `writelines()`
- `with` statement
- Text files
- File paths
- File processing programs

### Example

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

---

# 🔟 Exception Handling

Exception handling allows programs to deal with unexpected situations without crashing unnecessarily.

### Topics

- Errors vs Exceptions
- `try`
- `except`
- `else`
- `finally`
- Multiple exceptions
- Custom exceptions
- `raise`
- User input errors
- Practical exception-handling programs

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

Object-Oriented Programming is used to structure programs around classes and objects.

### Topics

- Classes
- Objects
- Constructors
- `__init__()`
- Instance variables
- Methods
- Public variables
- Protected variables
- Private variables
- Encapsulation
- Getters
- Setters
- Inheritance
- Method overriding
- Polymorphism
- Abstraction
- Abstract classes
- Abstract methods
- `ABC`
- `abstractmethod`
- Operator overloading
- Magic / Dunder methods

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

- Iterators
- Iterables
- Generators
- `yield`
- Generator expressions
- Decorators
- Comprehensions
- Advanced functions
- Memory-efficient programming
- Pythonic programming techniques

### Generators

Generators produce values one at a time using the `yield` keyword.

```python
def numbers():

    for i in range(5):
        yield i


for number in numbers():
    print(number)
```

### Why Generators?

Generators are useful when working with:

- Large datasets
- Data processing
- File processing
- Data pipelines
- Memory-intensive operations

---

# 1️⃣3️⃣ Data Analysis with Python

This section focuses on using Python to load, manipulate, analyze, summarize, and understand data.

### Libraries

- NumPy
- Pandas

---

## 🔢 NumPy

NumPy is a Python library used for numerical computing and efficient array operations.

### Topics

- Installing NumPy
- Importing NumPy
- NumPy arrays
- `ndarray`
- One-dimensional arrays
- Multi-dimensional arrays
- Array indexing
- Array slicing
- Dimensions
- Shape
- Size
- Data type
- Reshaping
- Array operations
- Mathematical operations
- Statistical operations
- Random numbers
- Normalization
- Standardization

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

- Mean
- Median
- Variance
- Standard deviation
- Normalization
- Standardization

---

# 🐼 Pandas

Pandas is a Python library mainly used for data manipulation and data analysis.

### Main Data Structures

### Series

A one-dimensional labeled data structure.

```python
import pandas as pd

marks = pd.Series([80, 90, 75, 88])

print(marks)
```

### DataFrame

A two-dimensional tabular data structure containing rows and columns.

```python
data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)
```

### Pandas Topics

- Creating DataFrames
- Reading data
- CSV files
- Inspecting data
- Selecting columns
- Selecting rows
- Indexing
- Slicing
- Adding columns
- Updating columns
- Removing columns
- Sorting data
- Filtering data
- `loc`
- `iloc`
- Grouping
- Aggregation

### Data Aggregation

```python
df["Marks"].sum()
df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].count()
```

### GroupBy

```python
df.groupby("Department")
```

`groupby()` allows data to be divided into groups and analyzed separately.

---

# 1️⃣4️⃣ Data Visualization

Data visualization helps transform data into visual representations that are easier to understand.

### Topics

- Matplotlib
- Seaborn
- Line plots
- Bar charts
- Pie charts
- Histograms
- Scatter plots
- Box plots
- Violin plots
- Subplots
- Labels
- Legends
- Titles
- Customization
- Data distribution
- Outlier visualization

### Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Sample Line Plot")

plt.show()
```

---

# 1️⃣5️⃣ Python Logging

Logging is used to record information about what happens inside an application.

### Topics

- Python logging
- Logging levels
- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`
- `logging.basicConfig()`
- Log files
- Multiple loggers
- Formatting logs
- Real-world logging

### Example

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG
)

logging.info("Application started")
logging.warning("This is a warning")
logging.error("An error occurred")
```

---

# 1️⃣6️⃣ SQLite3

SQLite is a lightweight relational database that can be used directly from Python.

### Topics

- SQLite introduction
- Creating databases
- Creating tables
- Connecting to databases
- Cursors
- SQL queries
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- Committing transactions
- Closing connections
- Working with Python and SQLite

### Basic Flow

```text
Python Program
      ↓
SQLite Connection
      ↓
Cursor
      ↓
SQL Query
      ↓
Database
```

---

# 1️⃣7️⃣ Memory Management in Python

This section focuses on understanding how Python manages memory internally.

### Topics

- Python memory management
- Memory allocation
- Memory deallocation
- Stack and Heap
- Objects and references
- Reference counting
- Garbage collection
- `gc` module
- Mutable and immutable objects
- Shallow copy
- Deep copy
- `id()`
- Memory optimization
- `sys.getsizeof()`

### Example

```python
import gc

numbers = [1, 2, 3]

print(id(numbers))

del numbers

gc.collect()
```

### Why Learn Memory Management?

Understanding memory management helps with:

- Memory-efficient programming
- Understanding object references
- Debugging memory-related problems
- Working with large datasets
- Understanding Python internals

---

# 1️⃣8️⃣ Flask Framework

Flask is a lightweight Python web framework used to build web applications and APIs.

### Topics

- Introduction to Flask
- Installing Flask
- Creating a Flask application
- Flask application object
- Routes
- URL routing
- HTTP methods
- GET requests
- POST requests
- `render_template()`
- Jinja2 templates
- HTML templates
- Static files
- `request`
- `redirect`
- `url_for`
- Forms
- Handling user input
- Flask project structure
- Running Flask applications
- Building web applications

### Basic Flask Application

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Flask!"


if __name__ == "__main__":
    app.run(debug=True)
```

### Flask Application Flow

```text
Browser
   ↓
HTTP Request
   ↓
Flask Route
   ↓
Python Function
   ↓
Response
   ↓
Browser
```

### Repository Practice

The Flask section includes practical work with:

- Flask routes
- HTML templates
- Jinja2
- Web application structure
- Request handling

---

# 1️⃣9️⃣ Streamlit Framework

Streamlit is a Python framework used to quickly create interactive web applications for data science and machine learning.

### Topics

- Introduction to Streamlit
- Installing Streamlit
- Creating Streamlit applications
- Running Streamlit applications
- Titles
- Headers
- Text
- Markdown
- Sidebar
- Sliders
- Buttons
- Text input
- Checkboxes
- Select boxes
- Radio buttons
- DataFrames
- Tables
- Charts
- Interactive widgets
- Caching
- Machine Learning applications

### Basic Streamlit Application

```python
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}!")
```

### Running Streamlit

```bash
python -m streamlit run filename.py
```

### Streamlit Application Flow

```text
User
  ↓
Streamlit Interface
  ↓
User Input
  ↓
Python Code
  ↓
Processing / ML Model
  ↓
Output
```

---

# 🤖 Machine Learning with Streamlit

The repository also contains an example of integrating Machine Learning algorithms with Streamlit.

### Example

```text
User Input
     ↓
Streamlit Widgets
     ↓
Feature Values
     ↓
Machine Learning Model
     ↓
Prediction
     ↓
Display Result
```

One example uses:

- Scikit-learn
- Iris Dataset
- Random Forest Classifier
- Streamlit widgets

### Iris Classification

The application takes flower measurements such as:

- Sepal length
- Sepal width
- Petal length
- Petal width

and uses a trained machine learning model to predict the flower species.

---

# 📁 Repository Structure

```text
Python/
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
├── 14-SQLite3/
│
├── 15-PythonLogging/
│   ├── logs/
│   ├── 15.1-Basic.ipynb
│   ├── 15.2-LoggingWithMultipleLoggers.ipynb
│   ├── 15.3-LoggingRealWorldExample.py
│   └── log files
│
├── 17-MemoryManagement/
│   └── 17.1-Basic.ipynb
│
├── 18-FlaskFrameWork/
│   ├── flask/
│   └── WorkingWithApp/
│
├── 19-StramLitFrameWork/
│   ├── 19.1-BuildingWebApp.py
│   ├── 19.2-widgets.py
│   └── 19.3-SomeMLAlgoWithStreamlit.py
│
├── Sampledata.csv
│
├── venv/
│
├── .gitignore
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🔢 NumPy | Numerical computing |
| 🐼 Pandas | Data manipulation and analysis |
| 📊 Matplotlib | Data visualization |
| 📈 Seaborn | Statistical visualization |
| 🤖 Scikit-learn | Machine Learning |
| 🌐 Flask | Web development |
| 🚀 Streamlit | Interactive data and ML applications |
| 🗄️ SQLite3 | Database management |
| 📝 Python Logging | Application logging |
| 💻 VS Code | Development environment |
| 📓 Jupyter Notebook | Interactive learning and experimentation |
| 🌱 Virtual Environment | Dependency isolation |
| 📦 pip | Python package management |
| 🔧 Git | Version control |
| 🐙 GitHub | Repository and project management |
| 📄 CSV | Structured data storage |

---

# 📦 Environment Setup

Clone the repository:

```bash
git clone https://github.com/vaishnavilamba/Python-Programming.git
```

Move into the project:

```bash
cd Python-Programming
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Python Programs

For a normal Python file:

```bash
python filename.py
```

For Jupyter Notebook:

```bash
jupyter notebook
```

For Flask:

```bash
python app.py
```

For Streamlit:

```bash
python -m streamlit run filename.py
```

---

# 📊 Data Analysis Workflow

The repository follows a practical data analysis workflow:

```text
Raw Data
   ↓
Load Data
   ↓
Understand Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
Analyze Data
   ↓
Visualize Data
   ↓
Extract Insights
```

---

# 🤖 Machine Learning Workflow

The learning journey gradually moves toward Machine Learning.

```text
Data
 ↓
Data Cleaning
 ↓
Exploratory Data Analysis
 ↓
Feature Engineering
 ↓
Train-Test Split
 ↓
Model Training
 ↓
Prediction
 ↓
Evaluation
 ↓
Deployment
```

---

# 🎯 Learning Objectives

Through this repository, I aim to:

- Build strong Python fundamentals
- Understand Python data structures
- Write clean and reusable Python programs
- Understand Object-Oriented Programming
- Learn advanced Python concepts
- Understand memory management
- Work with files and exceptions
- Work with databases
- Understand logging
- Manipulate real-world datasets
- Understand NumPy
- Learn Pandas
- Learn data visualization
- Build web applications using Flask
- Build interactive applications using Streamlit
- Apply Machine Learning algorithms
- Build ML-powered applications
- Develop problem-solving skills
- Build a strong foundation for AI and Machine Learning

---

# 🧪 Learning Approach

I follow a:

```text
📖 Learn
   ↓
💻 Implement
   ↓
🧪 Practice
   ↓
📊 Work With Data
   ↓
🧠 Understand Why
   ↓
🚀 Build Projects
```

The purpose of this repository is not to collect code blindly.

The goal is to understand:

```text
What is it?
     ↓
Why do we need it?
     ↓
How does it work?
     ↓
How do we implement it?
     ↓
Where is it used?
```

---

# 📈 Progress Tracker

| # | Topic | Status |
|---|---|---|
| 1 | Python Basics | ✅ Completed |
| 2 | Control Flow | ✅ Completed |
| 3 | Lists | ✅ Completed |
| 4 | Tuples | ✅ Completed |
| 5 | Sets | ✅ Completed |
| 6 | Dictionaries | ✅ Completed |
| 7 | Functions | ✅ Completed |
| 8 | Modules & Packages | ✅ Completed |
| 9 | File Handling | ✅ Completed |
| 10 | Exception Handling | ✅ Completed |
| 11 | OOP | ✅ Completed |
| 12 | Advanced Python | ✅ Completed |
| 13 | Data Analysis with Python | 🔄 In Progress |
| 14 | Data Visualization | 🔄 Learning |
| 15 | Python Logging | 🔄 Learning |
| 16 | SQLite3 | 🔄 Learning |
| 17 | Memory Management | 🔄 Learning |
| 18 | Flask Framework | 🔄 Learning |
| 19 | Streamlit Framework | 🔄 Learning |
| 20 | Machine Learning | 🔜 Next Stage |

---

# 🚀 What's Next?

The next stage of this learning journey will focus on:

```text
Python
  ↓
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
Model Evaluation
  ↓
Machine Learning Applications
  ↓
Flask / Streamlit Deployment
  ↓
Deep Learning
  ↓
Real-World ML Projects
```

### Planned Technologies

- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / PyTorch
- Flask
- Streamlit
- SQL
- Jupyter Notebook
- Machine Learning algorithms

---

# 💡 Learning Philosophy

> **Don't just memorize the syntax. Understand what happens behind the syntax.**

Every concept should answer five questions:

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

**Current Focus:** Python, Data Analysis, Flask and Streamlit

**Python Fundamentals:** Completed ✅

**OOP:** Completed ✅

**Advanced Python:** Completed ✅

**NumPy:** Learning / Practicing 🔄

**Pandas:** Learning / Practicing 🔄

**Data Analysis:** In Progress 🔄

**Flask:** Learning / Practicing 🔄

**Streamlit:** Learning / Practicing 🔄

**Machine Learning:** Next Stage 🚀

---

# 👩‍💻 Author

## Vaishnavi

**B.Tech CSE Student**

This repository represents my continuous journey of learning Python, strengthening programming fundamentals, working with data, building applications, and moving toward Machine Learning and AI.

---

# ⭐ Learning Journey

```text
Learn consistently.
Practice deeply.
Understand concepts.
Build projects.
Keep improving.
```

⭐ If you find this repository useful, feel free to explore the individual topic folders and follow the learning journey from Python fundamentals to Machine Learning applications.