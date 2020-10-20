import math

def area(radius):
    area = round(math.pi*radius**2,2)
    print("area of circle with radius {0} is = {1}".format(radius,area))

def peri(radius):
    peri = round(2*math.pi*radius,2)
    print("perimeter Of circle with radius {0} is = {1}".format(radius,peri))

