#!/usr/bin/python3

# use pi value from math library python
import math

# value of pi defined in this variable
pi = math.pi

# function to convert from degree into radian
def rad(degree,point):
    # this will return the value from formula calculation
    return f"{(degree*(pi/180)):.{point}f} radian"
  
# function to convert from radian into degree
def deg(radian,point):
    # this will return the value from formula calculation
    return f"{(radian*(180/pi)):.{point}f} degree"

# you can set limit of decimal point in the second argument
print(deg(0.87,2))
