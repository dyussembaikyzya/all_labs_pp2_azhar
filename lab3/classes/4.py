import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates = ({self.x}), ({self.y})")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point):
        distance = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return distance
    
a = float(input("x = "))
b = float(input("y = "))
point1 = Point(a,b)
point1.show() 

c = float(input("x1 = "))
d = float(input("y1 = "))
point1.move(c,d)
point1.show() 

distance = point1.dist(Point(a,b))
print(f"Distance = {distance}")