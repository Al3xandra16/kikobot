import os
import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print("The horse prince is here")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(759869462257205301)
    await channel.send(f"Welcome {member}. If you have a question don't ask me. Ask Hristijan")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    #calculator
    if message.content.startswith('cal'):
        a = message.content.split(" ")
        try:
            x = int(a[1]) + int(a[3])
            await message.channel.send(f"Your calculation is {x}")
        except ValueError:
            try:
                x = float(a[1]) + float(a[3])
                await message.channel.send(f"Your calculation is {x}")
            except ValueError:
                await message.channel.send("No valid number")
    
    #Kick
    if message.content.startswith("kick"):
        if message.mentions == 0:
            await message.channel.send("You didn't mention any user")
        else:
            await message.channel.send(f"The user {message.mentions[0]} was kicked")
            await message.guild.kick(message.mentions[0], reason=None)

    #Purge
    if message.content.startswith("purge"):
        a = message.content.split(" ")
        if a[1].isdigit() == True:
            delt = await message.channel.purge(limit = int(a[1]))
            await message.channel.send("Deleted {} message(s)".format(len(delt)))
        else:
            await message.channel.send("Please enter a number")

    #Hug<3
    if message.content.startswith("hug"):
        await message.channel.send(f"{message.author} hugs {message.mentions[0]}")

    # Hello zdravo
    if message.content.startswith("hello"):
        await message.channel.send("Hello ma4e")

bot.run(os.environ.get('TOKEN'))