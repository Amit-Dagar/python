#3.	Write a program that declares 3 integers, determines and prints the largest and smallest in the group.
#Inputting three numbers
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))

#Comparing for Largest Number
if(x>=y and x>=z):
	print(x,"is the largest number")
elif(y>=x and y>=z):
	print(y,"is the largest number")
else:
	print(z,"is the largest number")

#Compairing for Smallest number
if(x<=y and x<=z):
	print(x,"is the smallest number")
elif(y<=x and y<=z):
	print(y,"is the smallest number")
else:
	print(z,"is the smallest number")