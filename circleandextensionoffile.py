#area of circle
from math import pi
r = float(input ("Input the radius of the circle : "))
area = pi * r * r
print ("The area of the circle with radius " + str(r) + " is: " + str(area))


#extension of file
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
