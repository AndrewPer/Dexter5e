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


# def enc(name):
# 	pass


# class mon:
# 	def __init__(self,species,level,shiny_rate=0.01):


print(pokemon[6])