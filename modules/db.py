import sqlite3
connection = sqlite3.connect('./bot.db')
c = connection.cursor()

def verify(discord_id, roblox_id):
	"""
	Creates a new user in verified table.

	Paramaters:
		discord_id (int): discord id
		roblox_id (int): roblox id
	"""
	#Insert
	c.execute("INSERT INTO verified VALUES ("+ str(discord_id) + "," + str(roblox_id) +")")

	#Commit
	connection.commit()

def userExists(discord_id):
	"""
	Checks if a user exists

	Paramaters:
		discord_id (int): discord id
		roblox_id (int): roblox id
	"""
	if c.execute("SELECT EXISTS(SELECT 1 FROM verified WHERE discord_id=" + str(discord_id) + ");"):
		return True
	else:
		return False