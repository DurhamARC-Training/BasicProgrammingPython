---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
ARC course "Learning to programme with Python" (beginner level)
===============================================================
![icons8-python-48.png](images/icons8-python-48.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
Welcome to our ARC course "Learning to programme with Python".

Some general information on how the course will run:

* The course will run from 09:00 to 12:30. We plan a coffee break between 2 parts at around 10:45 for ~10-15 min.

* The material does not expect any prior programming experience.

* Each topic will be presented wih code demonstrations followed by practical exercises.

* We are happy to answer any questions during the course and to help during the exercises.

Enjoy learning Python!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Set up your Python environment
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
<ins>Preferred</ins>: Jupyter Notebook server or Jupyter Lab as a local Python environment installed on your laptops (hopefully, you've already received a welcome email with installation instructions).

<ins>Other</ins>: Google Colab (https://colab.research.google.com).

Go to the repository:
```https://github.com/DurhamARC-Training/BasicProgrammingPython```

copy the `pull_files_from_repo.py` file into your environment

execute it with `python pull_files_from_repo.py`
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>0.</ins> Introduction
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Course objectives
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
By the end of this course you should know:
 - how a basic computer program is written and executed,
 - what basic data types and control statements are,
 - how to get and process user input and data,
 - how to structure your code using functions,
 - what can lead to your program not working, and what to do about it,
 - where to find further resources to practice your Python programming.
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
## Useful resources
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
#### Materials used and recommended:
 - [Python Wiki - Python for Non-Programmers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
 - [How to think like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/index.html)
 - [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython)
 - [Software Carpentry - Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/index.html)
<!-- #endregion -->





<!-- #region slideshow={"slide_type": "slide"} -->
## Programming crash course
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Programming means: make the computer do the work for you!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
 - Do the maths
 - Boring repetitions
 - Too complicated/extensive tasks
 - Big data sets 
 - Make your analysis reproducible
 -  ...
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Running code in a compiled language (such as C)
<!-- #endregion -->

1. Write your code in a high-level programming language.
2. Translate into low-level (machine/assembly) language.
3. Execute the program.



<!-- #region slideshow={"slide_type": "slide"} -->
### Running code in an interpreted language (such as Python)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
1. Write your code in high-level programming language.
2. Interpret code and execute directly
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
### Python can be executed in different ways
#### Command line script
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
1. Create a `myname.py` file
2. run python `myname.py`
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
### Demonstration of using _Jupyter_ notebook
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
Jupyter works with cells such as these, which you execute with the play button or `Shift/Strg + Enter`:
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Add just a one to the cell and execute
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": ""} -->
If the box on the left is empty, you have not executed it. Otherwise a number indicates in which order the execution took place.

You can add cells with the plus. You can also change the type
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
##### Now it is markdown and the `#` indicates a header (or `##`, etc., up to 6 times, with smaller font sizes)
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>**Part I**</ins>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>1.</ins> Basics
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
## Basic data types
As any programming language, Python can deal with many different data types. Among the basic ones are `str` strings, `int` integers, `float` floating-point numbers and `bool` booleans.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
- Strings: "Heinz", 'Banana', 'He said "Hello"'
- Integers: 1, 2, 3, 22222222, -777
- Floats: -1.2, 0.0, 2.7182
- Booleans: True, False
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
## Variables
Values are stored in _variables_, which are of data types listed above or more complex ones.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
- “I reserve a space in memory for my data bit, and I call it 
by the name x
- Syntax: name = value”
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Example</ins>:_ Print type of a variable
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# print statement "Hello"
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# put the content of the print statement in a variable
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# check the type of that variable
```
<!-- #endsolution -->



<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Example</ins>:_ Try to assign the data types at the following qr code
<!-- #endregion -->

Try not to overthink. If something is ambiguous pick what fits best

![QRCode](images/qr_question1.png)



<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Example</ins>:_ Add integers
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Adding two integers (2 and 5)
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Adding integers to a string ("2+5 = ") naively
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Solution: call the result into a string
```
<!-- #endsolution -->



<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Example</ins>:_ Boolean type
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# boolean have to be capitalized
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Checking the type of a boolean
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Adding a boolean to an integer
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Checking the type of the result
```
<!-- #endsolution -->



<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Example</ins>:_ Boolean operators
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Adding booleans
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Logical AND
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Logical OR
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Negating boolean
```
<!-- #endsolution -->



<!-- #region slideshow={"slide_type": "slide"} -->
## Basic operators
New values can be obtained by applying operators to old values, for example, mathematical operators on numerical data types `int` or `float`.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
- String: concatenation with `+`
- Bool: `and`, `or`, `not`
- Numerical data: `+`, `-`, `*`, `/`, `%`, `**`, built-in functions `abs`, ...
- Order of execution:
    1. `()`
    2. `**`
    3. `*`, `/`
    4. `+`, `-`
    5. Left-to-right (except exponentiation!)

So, use parenthesis to make sure!
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
## Comments (and documentation)
Anything following the `#` character on a line is ignored by Python interpreter and becomes a comment. Comments are useful to document the code.
<!-- #endregion -->

```python slideshow={"slide_type": ""}
# This is my programme to demonstrate how to
# do simple calculations in Python.

my_number = 2

my_other_number = my_number + 5

my_number = my_other_number / 2 # I have to divide
                                # by 2 here, as the
                                # results are
                                # otherwise rubbish

print(my_number)
```



<!-- #region slideshow={"slide_type": "slide"} -->
## Debugging and Types of Errors
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
- Errors in computer programs are called ``bugs'' for historic reasons.
- For complex projects, you will usually spend more time testing and debugging than writing code.
- Three types of errors:
    - Syntax errors - written the code wrongly
    - Semantic errors - written the wrong code
    - Runtime errors - something's wrong with the code (during execution)
<!-- #endregion -->




<!-- #region slideshow={"slide_type": "slide"} -->
## Have a play!
<!-- #endregion -->

### _Exercises_

<!-- #region slideshow={"slide_type": ""} -->
You could try
 - what happens if you add a float and an integer,
 - what happens if you mix numbers and bools in arithmetic expressions,
 - how setting parenthesis changes the result of a large arithmetic expression,
 - to print statements that include variables of different data types,
 - try to reproduce each of the error types,
 - ...
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
#### _Example solution_
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# What happens if you add a float and an integer?
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": "slide"} -->
#### _Example solution_
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# What happens if you mix numbers and bools in arithmetic expressions?
```
<!-- #endsolution -->



<!-- #region slideshow={"slide_type": "slide"} -->
#### _Example solution_
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# How setting parenthesis changes the result of a large arithmetic expression?
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": "slide"} -->
#### _Example solution_
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print statements that include variables of different data types.
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": "slide"} -->
#### _Example solutions_
Try to reproduce each of the error types

<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
##### 1. Syntax Error
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": ""} -->
##### 2. Semantic Error
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": ""} -->
##### 3. Runtime Error
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Interlude: Indented blocks in python
Python uses indention to separate blocs after a `:`
```python
some_functionality_on_block:
   first_statement_in_block()
   second_statement_in_block()
statement_not_in_block()
```

<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>2.</ins> Functions
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
A function is a block of reusable code that performs a specific task. Functions help reduce repetition and make code easier to manage. A function is defined using the `def` keyword.
<!-- #endregion -->

* You can pass data to functions (parameters).
* Functions can return values.
* Functions help break down complex programs into smaller, manageable parts.

```python
# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Call the function
result = add_numbers(3, 4)
print(result)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Have a play!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### _Exercises_

**1)** Write a function that converts Celsius to Fahrenheit. Use the formula  
$
\text{Fahrenheit} = (\text{Celsius} \times \frac{9}{5}) + 32
$

<!-- #solution -->
<!-- #endregion -->
```python
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>**Part II**</ins>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>3.</ins> Getting Data in and out
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
## User input
The `print` function enables a Python program to display textual information to the user. The `input` function maybe used to obtain information from the user.
<!-- #endregion -->

```python slideshow={"slide_type": ""}
# Get some user input
x = input()
# print it
print(x)
# check the type of the input
type(x)   # This will be a string if you don't convert it
```

```python slideshow={"slide_type": ""}
# Implement a greeting function with user input
name = input("What's you name?")
print("Hello " + name)
```



<!-- #region slideshow={"slide_type": "slide"} -->
## Reading and writing files
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
```python
# Create a file object
with open("testfile.txt", 'w') as my_file:
    ...
```
Two things to note here:
 - My object `my_file` is different from my file `"testfile"`!
 - There are different modes:
     - read: `'r'`
     - (over-)write: `'w'`
     - append: `'a'`
     - read+write: `'w+'` or `'r+'`
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
### Writing files and formatting strings (C-style)
<!-- #endregion -->

```python slideshow={"slide_type": ""}
with open("testfile.txt", "w") as my_file:
    # Write - note special characters!
    my_file.write("This is some text. \n And some more.")
    my_file.write("\n\nI can also add numbers like this: %d %d \n" %(22, 333))

    my_file.write(str(222))
```

<!-- #region slideshow={"slide_type": ""} -->
see also [https://www.learnpython.org/en/String\_Formatting](https://www.learnpython.org/en/String_Formatting)
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
### Writing files (f-strings)
<!-- #endregion -->

```python slideshow={"slide_type": ""}
number1 = 44
number2 = 111

with open("testfile.txt", "a") as my_file:
    # Append to the opened file
    my_file.write(f"\n I have opened the same file again.\n More numbers: {number1} {number2}.")
```

<!-- #region slideshow={"slide_type": ""} -->
see also [f-strings](https://realpython.com/python-f-strings/)
<!-- #endregion -->



<!-- #region slideshow={"slide_type": "slide"} -->
### Reading files
<!-- #endregion -->

```python slideshow={"slide_type": ""}
with open("testfile.txt", "r") as my_file:
    # Read it and print it to screen
    print(my_file.read())

    # Try this:
    #print(my_file.read(7))
    #print(my_file.readline())
    #print(my_file.readlines())
```



<!-- #region slideshow={"slide_type": "slide"} -->
## Have a play!
<!-- #endregion -->

### _Exercises_

<!-- #region slideshow={"slide_type": ""} -->
Here are some exercise ideas for "Getting data in and out":
- Prompt the user for a filename and write a short text into it.
- Read it back and print the lines to the screen.
- Experiment with different modes: 'r', 'w', 'a' to see how the file content changes.
<!-- #endregion -->

```python

```

<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>4.</ins> Data structures
<!-- #endregion -->

Python can work not only with basic data types mentioned before, but also with compound ones. Compound data types in Python are a powerful tool for organizing and storing data. Among the most commonly used are _lists_ and _dictionaries_. `For`-loops described in the next section often iterate over elements of lists or pairs of keys and values in dictionaries. But they can also iterate over a series of numbers generated for indexing or calculations by the `range()` function.

<!-- #region slideshow={"slide_type": "slide"} -->
## Lists
<!-- #endregion -->

_Lists_ are ordered collections of items.

<!-- #region slideshow={"slide_type": ""} -->
* A list contains items separated by commas and enclosed with square brackets `[]`
* A list can contain different datatypes (`int`, `float`, `str`, etc.)
* Similar to strings, list members can be accessed using their associated index which is zero-based
* Common list functions: `append()`, `remove()`, `pop()`
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Examples:</ins>_

<!-- #solution -->
<!-- #endregion -->
```python
# Creating/Initialising a list
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print a list
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print an element of the list. Note: use [] not () for item indexing
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print the first element of the list. Indexing starts with 0!
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print the last element of the list using backward indexing
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print an internal slice of the list
```
<!-- #endsolution -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
# Print a slice of the list from the beginning
```
<!-- #endsolution -->

<!-- #solution -->
```python
# Different datatypes in lists, length of lists
```
<!-- #endsolution -->

<!-- #solution -->
```python
# Print out `list1`, a slice containing the last element
```
<!-- #endsolution -->

<!-- #solution -->
```python
# Concatenate two lists
```
<!-- #endsolution -->





<!-- #region slideshow={"slide_type": "slide"} -->
## _Range()_ function
<!-- #endregion -->

The `range()` function in Python is used to generate a sequence of numbers. It takes up to three arguments: `start`, `stop`, and `step`. By default, `start` is 0, `step` is 1, and the sequence ends just before the `stop` value.


* `range(stop)`: Generates numbers from 0 to stop - 1.
* `range(start, stop)`: Generates numbers from start to stop - 1.
* `range(start, stop, step)`: Generates numbers from start to stop - 1, stepping by step.
* `range()` can generate both increasing and decreasing sequences by changing the step argument.
* The generated sequence is immutable, but can be converted to a list or iterated directly.

<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Examples:</ins>_
<!-- #endregion -->

```python
range(10)
```

```python
list(range(10))
```

```python
list(range(1,10))
```

```python
list(range(3,7))
```

```python
list(range(2,15,3))
```

```python
list(range(9,2,-1))
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Have a Play!
<!-- #endregion -->

### _Exercises_


**1) Lists**: Create a list of numbers from 1 to 20 and then print the elements at every second index.

<!-- #solution -->
```python
```
<!-- #endsolution -->

<!-- #region slideshow={"slide_type": ""} -->
**2) Range**: Create a list of even numbers between 10 and 30 using `range()`, and print it.
<!-- #endregion -->

<!-- #solution -->
```python slideshow={"slide_type": ""}
```
<!-- #region slideshow={"slide_type": "slide"} -->
# <ins>5.</ins> Conditional and control flow statements
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
## _If_-statements
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Examples:</ins>_
<!-- #endregion -->
```python
```
```python
```
```python
# using only `if`
```
```python
# using `if`, `elif` and `else`
```
<!-- #region slideshow={"slide_type": "slide"} -->
## _For_-loops
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Examples:</ins>_
<!-- #endregion -->
```python
# Iterating over a list
# Using range to loop through numbers
```
```python
```
<!-- #region slideshow={"slide_type": "slide"} -->
## _While_-loops
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
### _<ins>Examples:</ins>_
<!-- #endregion -->
```python
```
```python
```
<!-- #region slideshow={"slide_type": "slide"} -->
## Have a Play!
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
### _Exercises_
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
<!-- #endregion -->
<!-- #solution -->
```python
```
<!-- #region slideshow={"slide_type": "slide"} -->
<!-- #endsolution -->

**2) `For`-loops**: Use a `for`-loop to print the square of numbers from 1 to 10.

<!-- #solution -->
<!-- #endregion -->
```python
```
<!-- #region slideshow={"slide_type": "slide"} -->
<!-- #endsolution -->

**3) `While`-loops**: Write a program that keeps asking the user for a number and prints the number. Stop when the user enters a negative number.

<!-- #solution -->
<!-- #endregion -->
```python
```
<!-- #region slideshow={"slide_type": "slide"} -->
<!-- #endsolution -->

**4) Functions**: Write a program to calculate the factorial of a number

<!-- #solution -->
<!-- #endregion -->
```python
```
<!-- #endsolution -->
