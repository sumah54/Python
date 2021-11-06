#this program adds stars to the starting of line by passing through following process

import pyperclip # copy pasting module

text = pyperclip.paste() # copy data to clipboard

lines = text.split('\n') # spliting text having starting lines 

for i in range(len(lines)): #enters * symbol to every single of the line
	lines[i] = '*' + lines[i] 
'\n'.join(text)
pyperclip.copy(text) # paste the text into the clipboard