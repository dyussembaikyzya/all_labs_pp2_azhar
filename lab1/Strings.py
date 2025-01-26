# Strings
print("Hello")
print('Hello')
# Hello
# Hello

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# It's alright
# He is called 'Johnny'
# He is called "Johnny"

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt 
# ut labore et dolore magna aliqua.

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Lorem ipsum dolor sit amet, 
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# Arrays
a = "Hello, World!"
print(a[1])
# e

# Looping Through a String
for x in "banana":
  print(x)
# b
# a
# n
# a
# n
# a

# String Length
a = "Hello, World!"
print(len(a))
# 13

# Check String
txt = "The best things in life are free!"
print("free" in txt)
# True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Yes, 'free' is present.

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
# True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# No, 'expensive' is NOT present.


# Slicing Strings
b = "Hello, World!"
print(b[2:5])
# llo

# Slice From the Start
b = "Hello, World!"
print(b[:5])
# Hello

# Slice To the End
b = "Hello, World!"
print(b[2:])
# llo, World!

# Negative Indexing
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
# orl

# Modify Strings
# Upper Case
a = "Hello, World!"
print(a.upper())
# HELLO, WORLD!

# Lower Case
a = "Hello, World!"
print(a.lower())
# hello, world!

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# Hello, World!

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
# Jello, World!

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
# HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# Hello World

# Format - Strings
age = 36
txt = "My name is John, I am " + age
print(txt)
# TypeError: can only concatenate str (not "int") to str

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# My name is John, I am 36

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
# The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt)
# The price is 1180 dollars

# Escape Characters
txt = "We are the so-called "Vikings" from the north."
# invalid syntax

txt = "We are the so-called \"Vikings\" from the north."
# We are the so-called "Vikings" from the north.
