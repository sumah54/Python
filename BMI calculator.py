weight = input("Input your weight in pounds:")
height = input("Input your height in inches")

bmi = float(weight *703 / height**2)

if(bmi >= 18.5 and bmi <=25)
	print("You have normal weight")
elif(bmi <18.5)
	print("you are under-weight")
elif(bmi > 25)
	print("You are over-weight")
else
	print("No idea")