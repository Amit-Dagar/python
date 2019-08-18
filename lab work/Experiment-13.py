#13. Write a program to print Fibonacci Series.
#Inputting first and second number
first=int(input("Enter first number: "))
second=int(input("Enter second number: "))

#how many numbers do you want to show
loops=int(input("Enter how many numbers do you want to show in series: "))
print(first,',',second,end='')
for i in range(loops-1):
	#assigning new values to variables 
	first,second=second,first+second
	print(',',second,end='')