#2.	Write a program to read radius of a circle and print the area of the circle.
#Importing math library
import math

#Getting radius of circle
radius=float(input("Enter radius:"))

#calculating area of circle
area=math.pi*radius**2

#printing area of circle
print("Area of circle with radius",radius,"is equals to",area)