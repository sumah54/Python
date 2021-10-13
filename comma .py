def nameChanger(para):
		para[-1] = 'and ' + para[-1]
		return ", ".join(para)
		
		
		
things = ['ahsan','cats','dog','animals']

	

print(nameChanger(things))	