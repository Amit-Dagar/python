#6.	Write  a program to find the root to the quadratic equations

#import Complex Math Library
import cmath

#inputting equation variables
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))

#calculating root of the quadratic equations
rootP=(-b+cmath.sqrt((b**2) - (4*a*c)))/(2*a)
rootN=(-b-cmath.sqrt((b**2) - (4*a*c)))/(2*a)

#printing values of quadratic equation
print("Positive =",rootP,"\nNagative =",rootN)