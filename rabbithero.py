import  time
print("The Rabbit Hero")
time.sleep(2)
print("\n\t\tThe Adventure Continues")
time.sleep(3)
print("""
	The Rabbit Hero lit his pipe on the darkest night of the year. He had not smoked 
	in a long time, but he knew his enemy had now entered the solar system. 
	His nemesis had arrived and he needed to decide whether to sit and wait 
	or get in his space ship and fly into the danger.

\n 	1. Sit and wait
	2. Go to the space ship
""")

move = input(">  ")

time.sleep(3)

if move == "1":	
	print("""
	Hours pass. The Rabbit Hero's pipe dies down to embers. An even-fuzzier-than-usual 
	feeling pervades his bones. Danger tickles his whiskers, and he knows
	his enemy has arrived on Earth. He now needs to decide whether to relight his 
	pipe or unlock his chest of weapons.
	
\n 	1.  Relight the pipe
	2.  Unlock the chest of weapons
""")

	danger = input("> ")
	time.sleep(2)		
	if danger == "1":
		print("""
	The match flares. Light and hope pervades the burrow. Instantly, 
	our hero feels slightly better. But the flame is small and flickering. What does he do?

\n	1.  Throw the match in the fireplace
	2.  Realize the Greatest Weapon is needed
""")
		fire = input("> ")
		time.sleep(2)		
		if fire == "1":
			print("""
			The tinder piled high in the fireplace catches instantly, and the burrow is flooded with light.
			Still, the Rabbit Hero knows that this is not enough to defeat his nemises: DARK MATTER!
			He needs the Greatest Weapon! Quickly the Rabbit Hero draws his Supernova Sword from his 
			ancient iron-bound chest. The firelight BLINGS off the blade, chasing out the darkness 
			and revealing all the room's crevices.
			Once again, Dark Matter has been kept at bay. 
""")
		elif fire == "2":
			print("""
			From his ancient sock drawer, the Rabbit Hero draws the Greatest Weapon: The SUPERNOVA SWORD!
			The sword seeks the darkness in the room and its point instantly pierces the lurking nemesis: DARK MATTER!  
			Victory prevails and the Rabbit Hero has saved the solar system. Though he knows
			Dark Matter always returns...
""")
		else:
			print("The Rabbit Hero sees Josh NOT choosing a valid option! This will NOT help the Rabbit Hero win his battle!")

	elif danger == "2":
		print("""
		Upon opening his ancient chest, the Rabbit Hero realizes that this is where he stored last year's turnips.
		He runs towards his sock drawer and  draws his Greatest Weapon: The SUPERNOVA SWORD!
                The sword seeks the darkness in the room and thrusts its point towards the danger and instantly 
		pierces the lurking nemesis: DARK MATTER! Victory prevails and the Rabbit Hero has 
		saved the solar system. Though he knows Dark Matter always returns!
""")
 
	else:
		print("Josh is still not actually following these directions. BAD INSTRUCTOR!")

elif move == "2":
	print("""
	The Rabbit Hero hurls his spacecraft toward the growing inky black blob known as DARK MATTER! Only light and
	goodness will defeat this enemy! He can choose to: 
	1.  Turn on his highbeams
	2.  Arm his spacecraft with the SUPERNOVA SWORD!
	""")
	space = input("> ")
	time.sleep(2)
	if space == "1":
		print("""
	The light obliterates the DARK MATTER into tiny pieces that will reassemble in 100 years. The Rabbit Hero 
	will be waiting...
	""")
	elif space == "2":
		print("""
	ZXORNGG!!!! With the SUPERNOVA SWORD armed and ready, the Rabbit Hero executes a complicated slice and dice 
	maneuver, chopping the Dark Matter into infinitessimal pieces like the finest teppanyaki chef! 
	Darkness is scattered and dissolved! The Rabbit Hero knows it will reassemble slowly over the next aeon. 
	But he will be ready with his Ginzu knives by then...
	""")

else:
	print("""We still have Josh not able to figure out where 1 and 2 are located on a keyboard. Press 1 for help or 2 to call me a dick! Oh no, you can't!""")
