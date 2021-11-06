import random 
import sys



#it is the secret number
secretNum = random.randint(1,20)


#try your luck to match with the number
def guessGame():	
	print("I am guessing a number between 1 and 20.")
	for number in range(1,7):
		print("Make a quick guess.")
		number = int(input('Give the number '))
		if number < secretNum :
			print("your number is very low")
		elif number > secretNum :
			print("your number is very high")
		else:
			break
	#if your luck matches with mine then:
	if number == secretNum:
			print("Congrats. you have the mind reading power like Prof.Xavier. ;)")
			
	#the real answer of the question is:
	print("It is "+str(secretNum))


guessGame()
#if you want to continue then
while True:
	ask = input ("do you want to play it again? ")
	if ask == "yes" or ask == "YES" or ask == "Yes":
		print(guessGame())
	elif ask == "no" or ask == "NO" or ask == "No":
		print("Okay")
		sys.exit()
	else:
		print("you typed "+ ask + "which was not part of the program. so shuting down. :(")
		sys.exit
		
