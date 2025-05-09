# Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)
# True
# False
# False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# b is not greater than a

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
# True
# True

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# True
# True

# Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# True
# True
# True

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# False
# False
# False
# False
# False
# False
# False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# False

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())
# True

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
# YES!

x = 200
print(isinstance(x, int))
# True


# Operators
print(10 + 5)
# 15

print((6 + 3) - (6 + 3))
# 0

print(100 + 5 * 3)
# 115

