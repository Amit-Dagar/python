#8.	Write a program to implement binary search.

#enter the length of array
length=int(input("Enter the number of elements: "))

#declare array
arr=[]
print("Enter",length,"elements:")

#inputting array elements
for i in range(length):
	arr.append(int(input()))

#sorting array
arr.sort()

#Take item to be search
item=int(input("Enter item to be search: "))

#Implementing binary search
first,last=0,length-1
mid=first+last//2
while first<last:
	if(arr[mid]==item):
		print("Item",item,"found")
		break;
	elif(arr[mid]>item):
		first=mid+1
		mid=last+first//2
	else:
		last=mid-1
		mid=last+first//2