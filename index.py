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
