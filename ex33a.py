i = 0
numbers = []
#this is the beginning of the loop
i = int(input("> "))
print(f"At the top i is {i}.") #This prints the beginning number.
numbers.append(i) #this adds the number to set being created (Numbers)
i = i + 1  #This adds a number to the original number
numbers.append(i)
print("Numbers now: ", numbers) #This adds this number to the set
print(f"At the bottom i is {i}") #The prints the new number 
					  #and loops back


print("The numbers:  ")  #This sets up for printing the numbers

for num in numbers:	#this tells what numbers to print.  This prints the set
	print(num)	#This printing  is independent of the print above.
