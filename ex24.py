print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """

\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\t\twhere there is none.
"""

print("----------------------------")
print(poem)
print("----------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars/100
	return jelly_beans, jars, crates

started = 10000
beans, jars, crates = secret_formula(started)

#renenber that this is another way to format a string

print("With a starting point of: {}".format(started))

#it's just like with an f"" string

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.".format(secret_formula))

