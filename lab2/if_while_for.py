# If ... Else

a = 33
b = 200
if b > a:
  print("b is greater than a")
# b is greater than a

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# a and b are equal

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# a is greater than b

# Short Hand If
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")
#B

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# = 

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Both conditions are True

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# At least one of the conditions is True

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# a is NOT greater than b

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# Above ten, and also above 20!

a = 33
b = 200

if b > a:
  pass

# While Loops

i = 1
while i < 6:
  print(i)
  i += 1
# 1
# 2
# 3
# 4
# 5

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 1
# 2
# 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# 1
# 2
# 3
# 4
# 5
# 6

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6

# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# apple
# banana
# cherry

for x in "banana":
  print(x)
# b
# a
# n
# a
# n
# a

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple
# banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# apple
# cherry

for x in range(6):
  print(x)
# 0 
# 1 
# 2 
# 3 
# 4 
# 5

for x in range(2, 6):
  print(x)
# 2 
# 3 
# 4 
# 5

for x in range(2, 30, 3):
  print(x)
# 2 
# 5 
# 8 
# 11
# 14 
# 17 
# 20 
# 23 
# 26 
# 29

for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0 
# 1 
# 2 
# 3 
# 4 
# 5
# Finally finished!

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# 0 
# 1 
# 2 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

for x in [0, 1, 2]:
  pass