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
	#try:
		base = data["encounters"][name]
		grouping = base["grouping"]
		levels = base["levels"]
		pokemon_choices = []
		pokemon_weights = []
		poke = []
		for p in base["pokemon_rate"]:
			pokemon_choices.append(p)
		for p in range(len(base["pokemon_rate"])):
			pokemon_weights.append(base["pokemon_rate"][pokemon_choices[p]])
		num_pokes = random.randrange(grouping["low"],grouping["high"]+1)
		print("Number to generate: " + str(num_pokes))
		for i in range(num_pokes):
			choice = random.choices(pokemon_choices,weights=pokemon_weights)
			level = random.randrange(levels["low"],levels["high"]+1)
			poke.append(Mon(choice[0],level))
		for i in range(len(poke)):
			print(poke[i].id)
			if poke[i].isShiny[0] == 1:
				print("*+ " + poke[i].species + " +* (shiny)")
			else:
				print(poke[i].species)
			print("lvl: " + str(poke[i].level) + "    SR: " + poke[i].sr)
			print("AC: " +str(poke[i].ac) + "    HP: " + str(poke[i].hp))
			print("STR: " + str(poke[i].str) + "  DEX: " + str(poke[i].dex) + "  CON: " + str(poke[i].con))
			print("INT: " + str(poke[i].int) + "  WIS: " + str(poke[i].wis) + "  CHA: " + str(poke[i].cha))
			print(poke[i].moves)
			print(poke[i].moveset)
			print(" ")

	# except:
	#  	print("Encounter not found")


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


def nature_boost(nat):
	stat_ac = "ac"
	stat_str = "str"
	stat_dex = "dex"
	stat_con = "con"
	stat_int = "int"
	stat_wis = "wis"
	stat_cha = "cha"
	stats = (stat_ac,stat_str,stat_dex,stat_con,stat_int,stat_wis,stat_cha)
	inc = stats.index(data["nature"][nat]["good_stat"])
	dec = stats.index(data["nature"][nat]["bad_stat"])
	stat_bonus = [0,0,0,0,0,0,0]
	if nat == "hardy":
		stat_bonus[inc] +=1
		stat_bonus[dec] -=2
	elif nat == "nimble":
		stat_bonus[inc] +=1
		stat_bonus[dec] -+2
	else:
		stat_bonus[inc] +=2
		stat_bonus[dec] -=2
	return stat_bonus


class Mon:
	def __init__(self,species,level,shiny_rate=0.01):
		self.id = random.random()
		self.species = species
		self.level = level
		self.shiny_rate = shiny_rate
		self.isShiny = random.choices([0,1],weights=[1.0-shiny_rate,shiny_rate])
		self.size = data["pokemon"][self.species]["size"]
		self.type = data["pokemon"][self.species]["type"]
		self.sr = data["pokemon"][self.species]["sr"]
		self.nature = random.choice(nature)
		self.bonus = nature_boost(self.nature)
		self.stats = [data["pokemon"][self.species]["ac"],data["pokemon"][self.species]["str"],data["pokemon"][self.species]["dex"],data["pokemon"][self.species]["con"],data["pokemon"][self.species]["int"],data["pokemon"][self.species]["wis"],data["pokemon"][self.species]["cha"]]
		self.stats = [self.stats[i]+self.bonus[i] for i in range(len(self.stats))]
		self.ac = self.stats[0]
		self.str = self.stats[1]
		self.dex = self.stats[2]
		self.con = self.stats[3]
		self.int = self.stats[4]
		self.wis = self.stats[5]
		self.cha = self.stats[6]
		self.hd = int(data["pokemon"][self.species]["hit_die"][+2:])
		self.hp = data["pokemon"][self.species]["hp"]
		if self.level > 1:
			for _ in range(self.level-1):
				self.hp += random.randrange(self.hd)+1
		self.moves = data["pokemon"][self.species]["moves"]["1"]
		if self.level >1:
			for i in range(len(data["pokemon"][self.species]["moves"]["2"])):
				self.moves.append(data["pokemon"][self.species]["moves"]["2"][i])
		if self.level >5:
			for i in range(len(data["pokemon"][self.species]["moves"]["6"])):
				self.moves.append(data["pokemon"][self.species]["moves"]["6"][i])
		if self.level >9:
			for i in range(len(data["pokemon"][self.species]["moves"]["10"])):
				self.moves.append(data["pokemon"][self.species]["moves"]["10"][i])
		if self.level >13:
			for i in range(len(data["pokemon"][self.species]["moves"]["14"])):
				self.moves.append(data["pokemon"][self.species]["moves"]["14"][i])
		if self.level >17:
			for i in range(len(data["pokemon"][self.species]["moves"]["18"])):
				self.moves.append(data["pokemon"][self.species]["moves"]["18"][i])
		if len(self.moves) > 4:
			self.moveset = random.choices(self.moves, k=4)
		else:
			self.moveset = self.moves



for i in range(3):
	print("Set %d" % (i+1))
	enc("example")
	print(" ")
