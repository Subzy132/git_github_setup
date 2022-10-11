# Solo Practice
#### This is the coding practise i carried out by myself using w3schools

```python
print("Hello World")

if 5 > 2:
    print("Five is greater than two!")

# This is a comment

'''
This is a comment
written in 
more that just one line
'''

carname = "Volvo"
x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

myfirst_name = "John"

x = y =  z = "Orange"

def myfunc():
  global x
  x = "fantastic"

x = 5
print(type(x))

# type int

x = "Hello World"
print(type(x))

# type str

x = 20.5
print(type(x))

# Type float

x = ["apple", "banana", "cherry"]
print(type(x))

# type list

x = ("apple", "banana", "cherry")
print(type(x))

# Type tuple

x = {"name" : "John", "age" : 36}
print(type(x))

# Type Dict

x = True
print(type(x))

# Type bool

x = 5
x = float(x)
#turns int into a float = 5.0

x = 5.5
x = int(x)
# Turns float into an int = 5

x = 5
x = complex(x)

# Turns int into a complex number 

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(10 > 9)

# True

print(10 == 9)

# False

print(10 < 9)

# False

print(bool("abc"))

# True any non empty string is considered true when in reality its none

print(bool(0))

# False


print(10 * 9)
print(10 / 2)

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

if 5 != 10:
  print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))




```