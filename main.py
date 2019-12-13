import discord
import asyncio
import random
from discord.ext import commands
from modules import bookworm, roblox, db

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def verify(ctx):
	if db.userExists(ctx.author.id):
		await ctx.send('Already Verified :white_check_mark:')
		return
	await ctx.send('Input your ROBLOX ID Below! 👍')
	check = lambda message: message.author == ctx.author

	try:
		msg = await client.wait_for('message', check=check, timeout=30)
	except asyncio.TimeoutError:
		await ctx.send('Verification Timed Out 😞')
	else:
		robloxid = msg.content
		phrase = bookworm.randomNouns(random.randint(3, 6))
		await ctx.send('Set your status or description too:\n`' + phrase + '`\nOnce you have react with ✅')
		reactCheck = lambda reaction, user: user == ctx.author and str(reaction.emoji) == '✅'

		try:
			reaction, user = await client.wait_for('reaction_add', timeout=30, check=reactCheck)
		except asyncio.TimeoutError():
			await ctx.send('Verification Timed Out 😞')
		else:
			user = roblox.robloxUser(robloxid)
			if user.getStatus() == phrase:
				db.verify(ctx.author.id, robloxid)
				await ctx.send('Succesfully Verified :white_check_mark:')
			elif user.getDescription() == phrase:
				db.verify(ctx.author.id, robloxid)
				await ctx.send('Succesfully Verified :white_check_mark:')
			else:
				await ctx.send('Verification Failed 😒')

client.run('NDcwNzYzMzAyMTYzODQxMDM0.XfMvkQ.iraGW1D-KG8pMAzQlvOgrCqbQFc')