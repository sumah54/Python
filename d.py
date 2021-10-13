from random import randint

player = input("Rock (r), Paper (p), Scissors (s)?") #ask for input by player
print(player, "vs",end =" ") 
n = randint(1,3)
#print(chosen)
if n == 1:
	computer = 'r'
elif n == 2:
	computer = 'p'
else:
	computer = 's'
print(computer)
if player == computer:
	print("Game Draw")
elif player == 'r'and computer == 's':
	print("Player wins")
elif player == 's' and computer == 'p':
	print("Player wins")
elif player == 'p'and computer == 's':
	print("Computer wins")
elif player == 's' and computer == 'r':
	print("Computer wins")
elif player == 'p' and computer == 'r':
	print("Player wins")
elif player == 'r' and computer == 'p':
	print('Computer wins')

if n == 1: 
	computer = 'r'
	print(0)
if player == 'r':
	print(0,end=" ")
x = int(input("what is your weight in grams: "))
y = x/1000
print(str(y) + " in Kilograms.")