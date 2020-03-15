from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hello {user_name},  I'm the {script} script.")
print("I would like to ask you some questions.")
print(f"Do you like programming {user_name}?")
likes = input(prompt)
print("What music do you listen to while programming?")
music = input(prompt)
print("What do you like besides programming?")
other = input(prompt)

print(f"""
	So you said {likes} to liking programming. 
	You said you listen to {music} while programming 
	and you also like to {other}.
""")  

