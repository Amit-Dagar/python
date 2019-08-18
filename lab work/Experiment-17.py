#17. Program to calculate average of numbers using function.
#getting length
def avg(sum,length):
	'''calculating average'''
	return sum/length

length=int(input("How many numbers do you want to insert: "))

#declaring variables and array
arr=[];sum=0
#getting array elements
print("Enter",length,"numbers: ")
for i in range(length):
	arr.append(int(input()))
	sum+=arr[i]
print("Average =",avg(sum,length))