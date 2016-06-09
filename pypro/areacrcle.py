class circle():
    def __init__(self,r):
        self.radius = r

    def circumference(self):
        return self.radius*2*3.14

    def area(self):
        return self.radius**2*3.14

    def volume(self):
        return self.radius**3*(4/3)*3.14


x = circle(3)
print x.area()
print x.circumference()
print x.volume()
