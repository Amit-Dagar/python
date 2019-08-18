#19. Write a function to accept a four digit number and print its sum of digits with recursion and without recursion.
#Getting number
num=int(input("Enter number: "))
sum=0
def rec(sum,num):
	if num<=0:
		return sum
	sum+=num%10
	return rec(sum,num//10)
print(rec(sum,num))