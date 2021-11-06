finished = False 
print("hello, I am CEO of Muhammad Ahsan Studio's")
name = input("what is your name?") # name for user
p = input("How may I help you " + name + " ?" ) #question for user
#for real bot
if p == "add" or p == "+":
	print("Okay then give me your number down for add")
	num1=int(input("Number1")) 
	num2=int(input("Number2"))
	result = num1+ num2  #add of two numbers
	print(str(num1) + " + " + str(num2) + " = " +str(result))
elif p == "substract" or p == "-":
	print("Okay then give me your number down for substract")
	num1=int(input("Number1"))
	num2=int(input("Number2"))
	result = num1 - num2  #substract of two number
	print(str(num1) + " - " + str(num2) + " = " +str(result))
elif p == "multiply" or p == "x":
	print("Okay then give me your number down for multiply")
	num1=input("Number1")
	num2=input("Number2")
	result = num1 * num2  #multiply of two number
	print(str(num1) + " X " + str(num2) + " = " +str(result))
elif p == "divide" or p == "/":
	print("Okay then give me your number down for divide")
	num1=input("Number1")
	num2=input("Number2")
	result = num1 // num2  #divide of two number
	print(str(num1) + " / " + str(num2) + " = " +str(result))
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
		price_many = int(input("How much does it costs?"))
		price.append(price_many)
	print(shopping)
	print("These are "+ str(how_many)+ " items added to your list.")
	print(price)
	print("And there price are as above.")
else:
	print("Sorry, Wrong Statment")
	print("See you soon :)")