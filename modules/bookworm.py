import os, random, json

with open('modules/nouns.json', 'r') as file:
	nouns = json.loads(file.read())

def randomNoun():
	"""
	Generates a single random noun based on a json file.
	"""
	return random.choice(nouns)

def randomNouns(index):
	"""
	Generates a string of multiple nouns.

	Paramters:

		index (int): amount of words
	"""
	string = ''
	for _ in range(index):
		if _ == index - 1:
			string = string + randomNoun()
		else:
			string = string + randomNoun() + ' '
	return string