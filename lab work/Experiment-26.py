#26. Write A Program to Append, Delete and Display Elements of a List Using Classes
class List:
	"""List class for performing append,delete and display list items"""
	def append(self,num):
		arr.append(num)

	def delete(self,num):
		try:
			arr.remove(num)
		except ValueError:
			print("Item not found in the list.")

	def display(self):
		print(arr)

arr=[];counter=1
#Getting number of elements
length=int(input("Enter number of elements in list : "))
#Getting List numbers
print("Enter",length,"items of list: ")
for i in range(length):
	arr.append(int(input()))

#Initiating Object for class List
obj=List()
print("Enter 1 for append.\nEnter 2 for Delete.\nEnter 3 for Display List.\nEnter 0 for exit()")
while counter!=0:
	counter=int(input("Enter Choice:"))
	if(counter==0):
		break
	if counter==1:
		obj.append(int(input("Enter number that you want to append: ")))
	elif counter==2:
		obj.delete(int(input("Enter number that you want to delete: ")))
	elif counter==3:
		obj.display()
	else:
		print("Wrong Input! Try again")