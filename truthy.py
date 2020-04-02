print('Welcome! Please enter your name')
name  = input(">   ") 
while not name:
	print('Enter your name: ')
	name = input()

print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
	print('Be sure to have enought room for all your guests.')
print('Done')


