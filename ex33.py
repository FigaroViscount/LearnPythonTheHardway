i = 1 
numbers = []

while i < 18:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i * 2

	print("Numbers now:  ", numbers)
	print(f"At the bottom i is {i}")
	print(f"\n")

print("The numbers:  ")

for  num in numbers:
	print(num)


