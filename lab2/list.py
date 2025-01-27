# Lists

thislist = ["apple", "banana", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry']

# Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 3

# Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# <class 'list'>

# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# ['apple', 'banana', 'cherry']

# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# banana

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# ['orange', 'kiwi', 'melon']

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Yes, 'apple' is in the fruits list

# Change List Items

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# ['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# ['apple', 'watermelon']

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# ['apple', 'banana', 'watermelon', 'cherry']


# Add List Items

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange']

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# ['apple', 'orange', 'banana', 'cherry']

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# Remove List Items

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []

# Loop Lists

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# apple
# banana
# cherry

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# apple
# banana
# cherry

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# apple
# banana
# cherry

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# apple
# banana
# cherry

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# ['apple', 'banana', 'mango']

# Condition
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]

# Iterable
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]

# Expression
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

# Sort Lists

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# [23, 50, 65, 82, 100]

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# [50, 65, 23, 82, 100]

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# ['cherry', 'Kiwi', 'Orange', 'banana']


# Copy Lists

# Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# ['apple', 'banana', 'cherry']

# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# ['apple', 'banana', 'cherry']

# Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
# ['apple', 'banana', 'cherry']


# Join Lists

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# ['a', 'b', 'c', 1, 2, 3]
