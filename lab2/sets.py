# SETS

thisset = {"apple", "banana", "cherry"}
print(thisset)
# {'cherry', 'banana', 'apple'}

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
# {'apple', 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
# {'apple', True, 2, 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
# {'apple', False, True, 'banana', 'cherry'}

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
# 3

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}


myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# {'cherry', 'banana', 'apple'}


# Access Set Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# cherry
# banana
# apple

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
# True

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
# False


# Add Set Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# {'apple', 'cherry', 'orange', 'banana'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# {'papaya', 'banana', 'pineapple', 'apple', 'mango', 'cherry'}

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# {'cherry', 'apple', 'kiwi', 'banana', 'orange'}


# Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# {'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# apple
# {'banana', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

