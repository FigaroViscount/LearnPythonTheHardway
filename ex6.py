#this is the first and second string written
types_of_people = 10
#here a string is put inside a string
x = f"There are {types_of_people} types of people."
#this is three more strings
binary = "binary"
do_not = "don't"
#Here a string is put inside a string
y = f"Those who know {binary} and those who {do_not}."
#this prints two strings
print(x)
print(y)
#this prints other strings. Note that the print is added in x and y
#Here are two places a sting is put inside a  string
print(f"I said: {x}")
print(f"I also said: {y}")
#this defines another string
hilarious = False
#this defines another string
#Here a string is put inside a string
joke_evaluation = "Isn't that joke so funny?! {}"

#Here is where a Joke is printed
print(joke_evaluation.format(hilarious))
#This defines another string
w = "This is the left side of ..."
e = "a string with a right side."
#This prints the two strings defined above
print(w + e) 

