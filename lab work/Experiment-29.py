#29. Write A Program to Create a Class in which One Method Accepts a String from the User and Another Prints it.
class Strings:
	'''Input string via one methond and printing via another one'''
	string=''
	def strIn(self):
		self.string=input("Enter String: ")

	def strOut(self):
		print("String is: "+self.string)

#initiating object for class Strings;
obj=Strings()

#calling functions of class
obj.strIn()
obj.strOut()