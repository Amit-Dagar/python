#27. Write A Program to Create a Class and Compute the Area and the Perimeter of the Circle
import math
class Circle(object):
	"""Calculating Perimeter and Area of circle"""
	def area(self):
		return math.pi*radius**2
	def perimeter(self):
		return 2*math.pi*radius

#getting radius of circle
radius=float(input("Enter radius of circle: "))

#Initiating object of Circle class
cir=Circle()
print("Area of circle:",cir.area())
print("Perimeter of circle:",cir.perimeter())