#16. Write a program to convert decimal number into equivalent binary numbers.
#Getting a number
num=int(input("Enter number: "))
#calculating binary number
bin=''
while num>0:
	bin+=str(num%2)
	num//=2
print(int(bin[::-1]))