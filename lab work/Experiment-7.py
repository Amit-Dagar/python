#7.	Write a program to implement linear search
#Enter length of array
length=int(input("Enter length of array: "))
arr=[]
#inputting array elements
print("Enter",length,"elements:")
for i in range(length):
	arr.append(int(input()))

#input element to search
item=int(input("Enter item to be search: "))

#Implementing linear search
for i in range(length):
	if(arr[i]==item):
		print("Item",item,"found at position",i+1)
		break
else:
	print("Item",item,"Not found in array")