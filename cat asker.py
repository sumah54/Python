names = []
while True:
	name = input("enter the name of cat "+ str(len(names)+ 1) + '(or enter nothing to stop.)')
	if name == '':
		break
	names = names + [name]
print("the name of cats are :")
for name in names:
	print("  "+ name)