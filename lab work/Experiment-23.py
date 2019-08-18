#23. Write a  function that accepts a string and prints number of vowels in that string.
#Accepting sctring
string=input("Enter any string: ").lower()
vowels=['a','e','i','o','u']
counter=0
#checking for vowels
for i in range(len(string)):
	if string[i] in vowels:
		counter+=1

print(counter,"vowels found in string : "+string)