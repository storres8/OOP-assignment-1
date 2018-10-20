class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x = (self.coor2[0] - self.coor1[0])**2
        y = (self.coor2[1] - self.coor1[1])**2
        d = (x + y)**(1/2)
        return d

    def slope(self):
        x = (self.coor2[0] - self.coor1[0])
        y = (self.coor2[1] - self.coor1[1])
        s = (y/x)
        return s

    def __str__(self):
        return f"This line has a ditance of {self.distance} and a slope of {self.slope}."

    def __len__(self):
        return f"distance of line: {self.distance}."

    def __del__(self):
        print("Line was deleted")


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        pi = 3.14159265359
        v = (pi)*(self.radius**2)*(self.height)
        return v

    def surface_area(self):
        pi = 3.14159265359
        s = (2*pi*self.radius*self.height) + (2*pi*(self.radius**2))
        return s
