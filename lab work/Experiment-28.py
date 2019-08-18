#28. Write A Program to Create a Class which Performs Basic Calculator Operations
class Calculator:
	'''Calculates basic operations of calculator'''
	def addition(self):
		print("Enter Two numbers: ")
		print("Addition =",int(input())+int(input()))
	def subtraction(self):
		print("Enter Two numbers: ")
		print("Subtraction =",int(input())-int(input()))
	def multiplication(self):
		print("Enter Two numbers: ")
		print("Multiplication =",int(input())*int(input()))
	def division(self):
		print("Enter Two numbers: ")
		print("Division a/b =",int(input())/int(input()))
#initialize counter variable
counter=1
#Initiaing cal object for class Calculator
cal=Calculator()
while counter!=0:
	print("\nEnter 1 for Addition.\nEnter 2 for Subtraction.\nEnter 3 for Multiplication.\nEnter 4 for Division.\nEnter 0 for exit()\n")
	counter=int(input("Enter Choice:"))
	if(counter==0):
		break
	if counter==1:
		cal.addition()
	elif counter==2:
		cal.subtraction()
	elif counter==3:
		cal.multiplication()
	elif counter==4:
		cal.division()
	else:
		print("Wrong Input! Try again")