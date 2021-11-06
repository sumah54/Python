grid =  [[0, 0, 0 ,0, 0, 0]
		    ,[0, 1, 0, 0, 0, 0]
			,[0, 1, 1, 0, 0, 0]
			,[0, 1, 1, 1, 0, 0]
			,[0, 1, 1, 1, 1, 0]
			,[0, 1, 1, 1, 1, 1]
			]

for col in range(len(grid)):

	for row in range(len(grid)):
		print(grid[row][col] end="")
	print()

