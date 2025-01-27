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


# Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# {3, 2, 'c', 'a', 'b', 1}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
# {'c', 'a', 1, 3, 2, 'b'}

# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
# {John, 2, 1, apple, cherry, 'c', 'b', 'a', banana, 3, Elena}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
# {'a', 3, 'c', Elena, cherry, 1, apple, 'b', banana, 2, John}

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# {3, 'a', 2, 'c', 1, 'b'}

# Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# {1, 2, 3, 'b', 'a', 'c'}

# Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
# {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
# {'apple'}

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)
# {False, True, 'apple'}

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
# {'banana', 'cherry'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# {'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
# {'banana', 'cherry'}

# Symmetric Differences
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
# {'google', 'banana', 'microsoft', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)
# {'google', 'banana', 'microsoft', 'cherry'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)
# {'google', 'banana', 'microsoft', 'cherry'}
