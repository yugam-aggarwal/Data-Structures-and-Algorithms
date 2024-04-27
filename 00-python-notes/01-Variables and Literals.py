# Assigning values to Variable
site_name = 'programiz.pro'
print(site_name)
# Changing the Value of a Variable
site_name = 'apple.com'
print(site_name)

# Assigning multiple values to multiple variables
a, b, c = 5, 3.2, 'Hello'
print(a)
print(b)
print(c)

# Assigning the same value to multiple variables
x = y = z = 'same'
print(x)
print(y)
print(z)

# Literals Definition
# Literals can be defined as a data that is given in a variable or constant. Python supports the following literals:
# - String literals
# - Numeric literals
# - Boolean literals
# - Special literals
# - Literal Collections
# - String literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function
print('Hello')
print("Hello")

# Numeric literals
# Numeric literals are unchangeable. Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.
# - An integer is a positive or negative whole number without a decimal point.
# - A float is a real number with a decimal point.
# - A complex number is written in the form, x + yj, where x is the real part and y is the imaginary part.
# Integer literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

# Float literals
float_1 = 10.5
float_2 = 1.5e2

# Complex literals
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# Boolean literals
# A Boolean literal can have any of the two values: True or False.
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Special literals
# Python contains one special literal i.e. None. We use it to specify that the field has not been created.
drink = 'Available'
food = None
print(drink)
print(food)

# Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
# List literals
fruits = ['apple', 'orange', 'mango']
numbers = [1, 2, 3]
print(fruits)
print(numbers)

# Tuple literals
# Tuple literals are written within parentheses ().
# Tuples are immutable, and usually, contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
# Tuple literals are used to create a tuple object.
# Tuple literals are written within parentheses ().
# Tuples are immutable, and usually, contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
# Tuple literals are used to create a tuple object.
fruits = ('apple', 'orange', 'mango')
numbers = (1, 2, 3)
print(fruits)
print(numbers)

# Dict literals
# Dict literals are written within braces {}.
# It is an unordered set of key: value pairs.
# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this: {}.
# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
data = {'name': 'John Doe', 'age': 32}
print(data)

# Set literals
# Set literals are written within braces {}.
# It is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# Set literals are written within braces {}.
# It is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
numbers = {1, 2, 3}
print(numbers)

# Constants
# Constants are usually declared and assigned on a module. Here, the module is a new file containing variables, functions, etc which is imported to the main file.
# Constants are written in capital letters and underscores separating the words.
# Example: PI = 3.14
# Constants are usually declared and assigned on a module. Here, the module is a new file containing variables, functions, etc which is imported to the main file.
# Constants are written in capital letters and underscores separating the words.
# Example: PI = 3.14
PI = 3.14
GRAVITY = 9.8
print(PI)
print(GRAVITY)
# Note: We can use the dir() function to see the list of constants and variables defined in a module. Here's an example:
# import math
# print(dir(math))

# difference between literals and variables and constants
# Variables are used to store data values. Variables are created when they are assigned a value.
# A variable is a name that refers to a value.
# Constants are special variables that are used to store constant values.
# Literals are data used in Python. These are raw data given in a variable or constant.
