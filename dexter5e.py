import json
import random


with open('pokemon_data.json') as json_file:
	data = json.load(json_file)

	nature = []
	items = []
	tms = []
	feats = []
	moves = []
	pokemon = []
	abilities = []
	encounters = []
	for p in data["nature"]:
		nature.append(p)
	for p in data["items"]:
		items.append(p)
	for p in data["tms"]:
		tms.append(p)
	for p in data["feats"]:
		feats.append(p)
	for p in data["moves"]:
		moves.append(p)
	for p in data["pokemon"]:
		pokemon.append(p)
	for p in data["abilities"]:
		abilities.append(p)
	for p in data["encounters"]:
		encounters.append(p)


def enc(name):
	try:
		base = data["encounters"][name]
		grouping = base["grouping"]
		levels = base["levels"]
		pokemon_choices = []
		pokemon_weights = []
		for p in base["pokemon_rate"]:
			pokemon_choices.append(p)
		for p in range(len(base["pokemon_rate"])):
			pokemon_weights.append(base["pokemon_rate"][pokemon_choices[p]])
		num_pokes = random.randrange(grouping["low"],grouping["high"]+1)
		for i in range(num_pokes):
			choice = random.choices(pokemon_choices,weights=pokemon_weights)
			level = random.randrange(levels["low"],levels["high"]+1)
			print("A level %d %s appears!" % (level, choice[0]))
	except:
	 	print("Encounter not found")


def poke_print(name):
	base = data["pokemon"][name]
	print(name)
	print("desc: " + base["desc"])
	print("size: " + base["size"] + "    " + "SR: " + base["sr"])
	print("AC: " + str(base["ac"]) + "    " + "HP: " + str(base["hp"]))
	print("STR: " + str(base["str"]) + "    " + "DEX: " + str(base["dex"]))
	print("CON: " + str(base["con"]) + "    " + "INT: " + str(base["int"]))
	print("WIS: " + str(base["wis"]) + "    " + "CHA: " + str(base["cha"]))
	print("Proficiencies: " + str(base["proficiency"]))
	print("Saving Throws: " + str(base["saving_throws"]))
	print("Vulnerable: " + str(base["vuln"]))
	print("Resists: " + str(base["resist"]))
	print("Immune: " + str(base["immune"]))
	print("Senses: " + str(base["senses"]))
	print("Abilities: " + str(base["abilities"]))
	print("Evolve: " + str(base["evolve"]))
	print("Starting moves: " + str(base["moves"]["1"]))
	print("Level two moves: " + str(base["moves"]["2"]))
	print("Level six moves: " + str(base["moves"]["6"]))
	print("Level ten moves: " + str(base["moves"]["10"]))
	print("Level fourteen moves: " + str(base["moves"]["14"]))
	print("Level eighteen moves: " + str(base["moves"]["18"]))
	print("TMs: " + str(base["moves"]["tms"]))
	print("HMs: " + str(base["moves"]["hms"]))


# class Mon:
# 	def __init__(self,species,level,shiny_rate=0.01):


for i in range(10):
	print("Set %d" % (i+1))
	enc("example")
	print(" ")
