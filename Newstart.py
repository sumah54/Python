#! python3
# An insecure password locker program


import pyperclip, sys
PASSWORDS = {
	'email': "Solo123/"
	'blog' : "Ahsan123/"
	'luggage': "ahsan123/"
	}
if len(sys.argv) < 2:
	print("usage: pw.py [account] -copy account password")
	sys.exit
account = sys.argv[1]
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + [account] + 'copied to clipboard')
else:
	print('there is no account names' + account)