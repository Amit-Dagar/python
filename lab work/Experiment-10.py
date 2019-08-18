#10.	Write a program to find factorial of a given number.
#Inputting number
num=int(input("Enter number: "))
sum=1
#calculating factorial
while(num>1):
	sum*=num
	num-=1
print("Factorial :",sum)