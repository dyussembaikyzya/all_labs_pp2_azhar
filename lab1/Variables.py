# Variables

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# Sally

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))
# <class 'int'>
# <class 'str'>

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
# A will not overwrite a


# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''
# SyntaxError: invalid decimal literal


# Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Orange
# Banana
# Cherry

x = y = z = "Orange"
print(x)
print(y)
print(z)
# Orange
# Orange
# Orange

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# apple
# banana
# cherry

# Output Variables

x = "Python is awesome"
print(x)
# Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Python is awesome

x = 5
y = 10
print(x + y)
# 15

x = 5
y = "John"
print(x + y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = 5
y = "John"
print(x, y)
# 5 John

# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
# Python is awesome

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# Python is fantastic
# Python is awesome

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Python is fantastic

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Python is awesome

