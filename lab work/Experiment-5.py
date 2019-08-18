#5.	Write a program to accept an year from user and find whether given year is leap year or not.
year=int(input("Enter year: "))

#Checking for leap year
if(year%4==0 and year%100!=0):
	print(year,"Year is a leap year")
else:
	if(year%400==0):
		print(year,"Year is a leap year")
	else:
		print(year,"Year is not a leap year")