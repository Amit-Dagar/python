#18. Write a function eval_quad_equation(a,b,c,x) which returns the value of the quadratic equation of the form
#Getting equation values
a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
x=int(input("Enter value of x = "))

def eval_quad_equation(a,b,c,x):
	'''calculating quadratic equation'''
	return (a*x**2)+(b*x)+c
print("Value of the quadratic equation :",eval_quad_equation(a,b,c,x))