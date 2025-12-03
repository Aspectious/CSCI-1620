import math;

def numcheck(num):
    float(num)
    if (float(num) <= 0):
            raise TypeError("Values must be Positive")

def circle(radius):
    numcheck(radius)
    return math.pi * square(radius)

def square(side):
    return rectangle(side, side)

def rectangle(side1, side2):
    numcheck(side1)
    numcheck(side2)
    return float(side1) * float(side2)

def triangle(base, height):
    return rectangle(base, height) / 2;
