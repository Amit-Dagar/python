'''14.	An ATM contains Indian Currency notes of 100,200,500 and 2000. Once the user enters amount to be with drawn. Display the minimum number of notes required to dispence from the ATM'''
#inputting amount
amount=int(input("Enter amount to be withdraw: "))
if(amount%100!=0):
	print("Notes of below 100 is not available so you can only withdraw Rs.",amount-amount%100)
else:
	if(amount>=2000):
		notesof2000=amount//2000;
		print("Notes of Rs.2000 =",notesof2000)
		if(amount%2000!=0):
			notesof500=(amount%2000)//500
			print("Notes of Rs.500 =",notesof500)
			if((amount%2000)%500!=0):
				notesof200=((amount%2000)%500)//200
				print("Notes of Rs.200 =",notesof200)
				if(((amount%2000)%500)%200!=0):
					notesof100=(((amount%2000)%500)%200)//100
					print("Notes of Rs.100 =",notesof100)
	elif(amount>=500 and amount<2000):
		notesof500=amount//500
		print("Notes of Rs.500 =",notesof500)
		if(amount%500!=0):
			notesof200=(amount%500)//200
			print("Notes of Rs.200 =",notesof200)
			if((amount%500)%200!=0):
				notesof100=((amount%500)%200)//100
				print("Notes of Rs.100 =",notesof100)
	elif(amount>=200 and amount<500):
		notesof200=amount//200
		print("Notes of Rs.200 =",notesof200)
		if(amount%200!=0):
			notesof100=(amount%200)//100
			print("Notes of Rs.100 =",notesof100)
	else:
		print("Notes of Rs.100 = 1")