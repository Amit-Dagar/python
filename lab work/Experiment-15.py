'''15.	Write nested if statements to print the appropriate message depending on the values of the variable temperature and humidity as given below; Assume that the temperature can only be warm and cold and the humidity can only be dry and humid.'''
#Geting Temprature and humidity
tmp=input("Enter Temprature state: ").lower()
hum=input("Enter Humidity: ").lower()
#calculating activity
if(tmp=='warm' or tmp=='cold'):
	if(hum=='dry' or hum=='humid'):
		if(tmp=='warm'):
			if(hum=='dry'):
				print("Play Cricket!")
			else:
				print("Play Tenis!")
		else:
			if(hum=="dry"):
				print("Basketball")
			else:
				print("Swim")
	else:
		print('wrong input for Humidity!!')

else:
	print("wrong input for temperature!!")