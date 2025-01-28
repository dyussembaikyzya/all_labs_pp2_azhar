class Shape:
    def area(self):
        return 0
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("a = "))
width = float(input("b = "))
s =Rectangle(length,width)
print("S = ",s.area())
