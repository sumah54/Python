print("hello")

user_name = input("what is your name?")

print("So, Your name is "+ user_name + ".")


print("Give us two numbers then.")

while True:
	a = int(input("Number 1"))
	b = int(input("Number 2"))
	if a == a.isalnum and b == b.isalnum:
		print("good you chose both of the numbers")
		break	
	else:
		print("put in the numbers next time.")

symbol = input("Give Name of Symbol")

output_plus = a+b
output_subs = a-b
output_sq = a ** b

if symbol == "+" or symbol == "plus":
	print(output_plus)
elif symbol == "-" or symbol == "minus":
	print(output_subs)
elif symbol == "square":
	print(output_sq)
else:
	print("wrong message :(")

numbers = int(input("how many"))
for n in range(numbers):
	print(2+n)