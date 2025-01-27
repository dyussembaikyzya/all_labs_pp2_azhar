# Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Ford

# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Length
print(len(thisdict))

# Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
# <class 'dict'>

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
# {'name': 'John', 'age': 36, 'country': 'Norway'}


# Access Dictionary Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
# Mustang

x = thisdict.get("model")
# Mustang

# Get Keys
x = thisdict.keys()
# dict_keys(['brand', 'model', 'year'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])

# Get Values
x = thisdict.values()
# dict_values(['Ford', 'Mustang', 1964])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 1964, 'red'])

# Get Items
x = thisdict.items()
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Yes, 'model' is one of the keys in the thisdict dictionary


# Change Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Add Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Remove Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# {'brand': 'Ford', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# {'brand': 'Ford', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# {}

# Loop Dictionaries
# Loop Through a Dictionary
for x in thisdict:
  print(x)
# brand
# model
# year

for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

for x in thisdict.values():
  print(x)
# Ford
# Mustang
# 1964

for x in thisdict.keys():
  print(x)
# brand
# model
# year

for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964

# Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])
# Tobias

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011