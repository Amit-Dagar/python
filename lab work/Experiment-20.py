#20. Write a function to accept an integer and print factors of it.
#getting number
num=int(input("Enter number: "))
print("1 *",num,end='')
for i in range((num//2)+1):
	for j in range((num//2)+1):
		if(i*j==num):
			print(',',i,"*",j,end='')