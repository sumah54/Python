finished = False 
print("hello, I am CEO of MA Studio's")
name = input("what is your name?") # name for user
p = input("How may I help you " + name + " ?" ) #question for user
#for real bot
if p == "add" or p == "+":
	print("Okay then give me your number down for add")
	input1=input("Number1") 
	input2=input("Number2")
	w=int(input1)
	q=int(input2)
	result = w + q #add of two numbers
	output = str(result)
	print(input1 + " + " + input2 + " = " +output)
elif p == "substract" or p == "-":
	print("Okay then give me your number down for substract")
	input1=input("Number1")
	input2=input("Number2")
	w=int(input1)
	q=int(input2)
	result = w - q #substract of two number
	output = str(result)
	print(input1 + " - " + input2 + " = " +output)
elif p == "multiply" or p == "x":
	print("Okay then give me your number down for multiply")
	input1=input("Number1")
	input2=input("Number2")
	w=int(input1)
	q=int(input2)
	result = w * q #multiply of two number
	output = str(result)
	print(input1 + " X " + input2 + " = " +output)
elif p == "divide" or p == "/":
	print("Okay then give me your number down for divide")
	input1=input("Number1")
	input2=input("Number2")
	w=int(input1)
	q=int(input2)
	result = w / q #divide of two number
	output = str(result)
	print(input1 + " / " + input2 + " = " +output)
elif p == "average": #taking average on numbers
	how_many = int(input("How many numbers?"))
	for n in range(how_many):
		number = input("Enter number " + str(n) + " .")
		total = int(number)
	result = int(total / how_many)
	print("the average = " + str(result))
elif p == "want to shopping" or p == "shopping": # for shopping stuff and making set of prices
	shopping = [] #using for loop for counting purchased items
	price = []
	how_many = int(input("how many you want to add to your shopping list "+ name + "?"))
	for item_number in range(how_many):
		item = input("what is item name of " + str(item_number) + "?")
		shopping.append(item)
		price_many = int(input("How much is it ?"))
		price.append(price_many)
	print(shopping)
	print("These are "+ str(how_many)+ " items added to your list.")
	print(price)
	print("And there price are as above.")
else:
	print("Sorry, Wrong Statment")
	print("See you soon :)")