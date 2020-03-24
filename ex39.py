# create a mapping ofa state to abbreviation

states = {
	'Oregon': 'OR', 
	'Florida': 'Fl', 
	'California': 'CA', 
	'New York': 'NY', 
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'Fl': 'Jcaksonville'}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

#print every city in the state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}") 

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")

print('-' * 10)

#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print("Sorry, no Texas")

#get a city with a default value

city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")
