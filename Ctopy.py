# 1 sum the following numbers
# 2+4+6+8+12+23+14+15+18+31
print("Question 1")
u = 2 + 4 + 6 + 8 + 12 + 23 + 14 + 15 + 18 + 31
print("the sum of the above numbers : " + str(u))

# 2 and 12 ask students for their names, class, roll: no, marks in different subjects and take the percentage
print("Question 2 ")

name = input("what is your name? ") #Asks name
print("So, " + str(name))
class_name = input("In which class you study? ")#Ask class name
print("And in class " + str(class_name) + ", ")
roll = input("What is your Roll:No? ") #Ask Roll:no
mark1 = int(input("What are your marks in English? ")) #Ask marks in English
total1 = int(input("total marks:"))#Total marks in English
mark2 = int(input("What are your marks in Urdu/Sindhi? ")) # Ask marks in Urdu/Sindhi
total2 = int(input("total marks:"))  # Asks total marks in Urdu/Sindhi
mark3 = int(input("What are your marks in Maths? "))# Ask marks in Maths
total3 = int(input("total marks:")) # Ask total marks in Urdu/Sindhi
mark4 = int(input("What are your marks in Chemistry? "))# Ask marks in Chemistry
total4 = int(input("total marks:")) #Asks total marks in Chemistry
mark5 = int(input("What are your marks in Biology? ")) # Ask marks in Biology
total5 = int(input("total marks:")) #Asks total marks in Biology
mark6 = int(input("What are your marks in Asan Urdu/Sindhi? ")) # Ask marks in Asan Urdu/Sindhi
total6 = int(input("total marks:"))#Asks total marks in Asan Urdu/Sindhi
mark7 = int(input("What are your marks in Pakistan Studies? ")) # Ask marks in Pakistan Studies
total7 = int(input("total marks:"))#Asks total marks in Pakistan Studies
mark8 = int(input("What are your marks in Islamiat? ")) # Ask marks in Islamiat
total8 = int(input("total marks:"))#Asks total marks in Islamiat
marks = (mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7 + mark8)
total = (total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8)
per = marks * 100/ total
a = 0
if per >= 80:
	a = "A"
elif per >= 70:
	a = "B"
elif per >= 60:
	a = "C"
elif per >= 50:
	a = "D"
elif per >= 40:
	a = "E"
else:
	a = "F"
print("the total marks are : " + str(total))
print("the obtained marks are :" + str(marks))
print("the grade of "+ str(name) + " is " + str(a)+" .")
print("and the percentage is : " + str(per) + "%")

#################################OR###################################
name = input("what is your name? ") #Asks name

how_many = int(input("How many subject(s)? "))
for n in range(how_many):
	sub_name = input("Enter name of subject no: " + str(n))
	number = int(input("Enter marks of subject " + str(sub_name) + " . "))
	total = int(input("total marks: "))
percent = int(number * 100/total)
result = int(percent)

print("the percentage of asked marks is: " + str(percent))

#3 Find out velocity of object
print("Question 3")
S = int(input("What is the distance? "))
T = int(input ("What is time? "))
V = S/T
print("the speed is: "+str(V))

#4 Find out distance covered by object
print("Question 4 ")
V = int(input("What is the speed? "))
T = int(input ("What is time? "))
S = V*T
print("the distance is: "+ str(S))

#5  Find the volume of cylinder
print("Question 5 ")
h = int(input("What is height of a cylinder? "))
r = int(input("What is radius of cylinder? "))
p = 3.14
volume = p*(r*r)*h
print("volume of cylinder is: " + str(volume))

#6  Find the square of any number
print("Question 6 ")
x = int(input("Number: "))
sq = x*x
print("then square of the given number will be: "+ str(sq))

#7  Find the sum of numbers and find the average
print("Question 7")
how_many = int(input("How many numbers?"))
for n in range(how_many):
	number = input("Enter number " + str(n) + " .")
	total = int(number)
result = int(total / how_many)
print("the average = " + str(result))

#8 Find the area of triangle
print("Question 8")
g = int(input("enter base"))
h = int(input("enter perpendicular"))
t = g*h
tri = 1/2 *t
print("the area of triangle is : " + str(tri))

#9  Find the area and circumference of circle
print("Question 9")
m= input("provide radius to get both answer")
p = 3.14
ar = p*r*r
cir = 2*r*p
print("the area of circle is : " + str(ar))
print("the circumference of circle is : " + str(cir))

#10 Print odd numbers till twenty

print("Question 10")
n = 1
while n > 20:
	print(n)
	n+=2 
	

#11 Tell which number is greater
w = int(input("Number 1: "))
q = int(input("Number 2: "))
if w > q:
	print("Number 1 is less than Number 2.")
elif w > q:
	print("Number 2 is greater than Number 1.")
elif w == q:
	print("Number are equal.")
else:
	print("Unkown relation.")

#13 Write a program to enter integer type data into an array and print it in reverse order

a = []
while True:
	b = int(input('type a number to convert it into a list'))
	if b == a[3]:
		break
	x=a.append(b)
print(a)
for i in a:
	i = 0
	print(a[i])
	i = i-i
print(x)






