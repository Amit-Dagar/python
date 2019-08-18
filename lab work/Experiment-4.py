#4.	Write a program to calculate simple interest.
#Inputting Amount,Rate and time 
p=int(input("Enter amount:"))
r=float(input("Enter rate of interest:"))
t=int(input("Enter time(in years):"))

#Calculating Simple Interest
interest=p*r*t/100

#printing SI(Simple Interest)
print("Simple Interest is:",interest)