#9.	Write a program to accept an integer and print sum of its digits.
#Enter number
num=int(input("Enter number: "))
sum=0
while(num>0):
	sum+=num%10
	num//=10
print("Sum of digits",sum)