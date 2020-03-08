from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ....")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you to  write three lines.")

line1 = target.write(input("line 1: "))
target.write("\n")
line2 = target.write(input("line 2: "))
target.write("\n")
line3 = target.write(input("line 3: "))
target.write("\n")
print("I'm goint to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally we close it.")
target.close()

