#12.	Write a program to find that given number is Armstrong or not.
#Inputting number
num=int(input("Enter number: "))
#declaring variables
temp=num;sum=0;length=len(str(num))

while temp>0:
	#calculating sum of digits with respective powers
	sum+=(temp%10)**length
	temp//=10
#Checking for Armstrong number
if(num==sum):
	print(num,"is an Armstrong number")
else:
	print(num,"is not an Armstrong number")