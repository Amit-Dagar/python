'''21. Write a function cal_gcd(a,b) that accepts two positive integers a and b and returns one integer as gcd (greatest common divisdor).'''

def cal_gcd(a,b):
	'''calculatin gcd'''
	if(a==0):
		return b
	elif b==0:
		return a
	elif a==b:
		return a
	elif a>b:
		return cal_gcd(a-b,b)
	return cal_gcd(a,b-a)

#getting two numbers
a=int(input("Enter a = "))
b=int(input("Enter b = "))

#checking for positive values
if(a>0 and b>0):
	print('GCD for',a,'and',b,'= ',cal_gcd(a,b))
else:
	print("Values are not positive.")