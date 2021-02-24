import discord
import random
import math
import datetime

client = discord.Client()

@client.event
async def on_ready():
	print("I am ready!")


@client.event
async def on_message(message):
	if message.author == client.user:
		return


	if message.channel.id == 809393742637170708:
		await message.add_reaction("✅")
		await message.add_reaction("❌")


	if "gaming" in message.content.lower().replace(" ", ""):
		if message.channel.id == 809483972282810390 or message.channel.id == 780765093343395880:
			if math.floor(random.random() * 100) > 86:
				await message.channel.send("**GAMING! 🎮**")
		
	if "christerpog" in message.content.lower() or "cristerpog" in message.content.lower():
		if message.channel.id == 809483972282810390 or message.channel.id == 780765093343395880:
			await message.channel.send("<:ChristerPOG:810255466952917052>")
			await message.add_reaction("<:ChristerPOG:810255466952917052>")

	if "<@!" + str(client.user.id) + ">" in message.content:
		await message.channel.send("Hej, jag är en bot som gamear på min fritid!")

	if "hur mycket är klockan" in message.content.lower():
		await message.channel.send(datetime.datetime.now().strftime("%H:%M:%S"))

client.run(token)
