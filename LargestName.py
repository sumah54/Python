def Namelen():
		num = None
		nam = None
		names = ['Ahsan', 'MuhammadAhsanasdfjklasdfjkl','kdjfakljfaklfjakfsajfklfjfjkdsfjldsafjakflajfklsafjaksfjaklfajslfkjalskfjalskdjflaksdjfklasjflaksdjflkasdjflaskdfajalskjflasfjsalfjlasdj','MuhammadAhsanSiddiqui','MuhammadAhsanSiddiquee', 'adfjkl;asdjfl;asdfjahhjkasdfhjkadsflahsdkjfasdhfkladfhkladfhkladfa']
		for name in names:
			print (name)
			if num is None or num < len(name):
				num = len(name)
			if  num == len(name):
				nam = name
				
		print(num)
		print('Largest name is: ' + nam)
Namelen()