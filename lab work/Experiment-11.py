#11. Write a program to find that given number is Palindrome or not.
#Inputting number
x=int(input("Enter number: "))
num=str(x)
rev=int(num[::-1])

if(x==rev):
	print(x,"is a Palindrome number")
else:
	print(x,"is not a Palindrome number")

