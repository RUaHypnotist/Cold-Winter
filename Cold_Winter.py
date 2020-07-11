import time

health = 100
hunger = 50
temperature = 50
sanity = 100
equipment = {"head": "NONE", "body": "T-SHIRT", "legs": "JEANS"}
character1 = {"STR": 1, "AGI": 1, "INT": 1, "LCK": 1}
character2 = "{'CLASS': 'VETERAN'}"
inventory = []
answer = 0

def response():
	answer = input()
	if answer == "INVENTORY":
		print(inventory)
	elif answer == "EQUIPMENT":
		print(equipment)
	else:
		print("ERROR: PLEASE TRY AGAIN")

def classChoose():
	print("Choose your class: CRAFTSMAN, VETERAN, SCHOLAR, DOCTOR")
	print("The CRAFTSMAN has an affinity for repairing and fixing structures, and designs trinkets as a hobby.")
	print("(50 percent less time on building tasks, and regain sanity by using trinkets during night. Starts with extra strength and a sturdy hammer.)")
	print("A former U.S. Marine, the VETERAN has spent time on the battlefield, and has extensive combat knowledge.")
	print("(Starts with an empty BERETTA M9, 50 percent less sanity decrease, more starting strength and agility.)")
	print("The SCHOLAR is an avid lover of books, and unconsciously quotes many in casual conversation. And who knows what could be learnt in these wastelands?")
	print("(Starts with extra intelligence, can read many books to gain EXP. )")
	print("The DOCTOR has experience working with diseases and sicknesses, and has medical knowledge on a variety of valuable subjects, from crafting medicine to wooden limb splints.")
	print("(Starts with a full medical kit and preliminary knowledge of plants and crafting medicines.")
	answer = input("Who would you like to be?")
	if answer == "CRAFTSMAN":
		print("You have chosen CRAFTSMAN as your character's class.")
		character1["STR"] = 2
		inventory.append("STURDY HAMMER")
	elif answer == "VETERAN":
		print("You have chosen VETERAN as your character's class.")
		character1["STR"] = 2
		character1["AGI"] = 2
		inventory.append("BERETTA M9")

def boot():
	answer = input("Launch COLD WINTER.py?")
	if answer == "YES":
		classChoose()
	else:
		print("ERROR: PLEASE TRY AGAIN")

boot()