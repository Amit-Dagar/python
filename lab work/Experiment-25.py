#25. Write A Program to Find the Area of a Rectangle Using Classes
length=int(input("Enter length of the circle: "))
bredth=int(input("Enter Breadth of the circle: "))
class Area:
	"""Class for calculating area of Rectangle"""
	def __init__(self,length,bredth):
		print("Area of the Rectangle:",length*bredth)

Area(length,bredth)