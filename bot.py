from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import random
import os
import discord

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = commands.Bot(command_prefix = '.')

#Confirms that bot is connected to server
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with fellow humans"))
    print("Logged in as " + client.user.name)
    servers = list(client.servers)
    print("Connected on " + str(len(client.servers)) + " servers:")
    for x in range(len(servers)):
        print('    ' + servers[x-1].name)

@client.event
async def on_message(message):
    #Checks if message is a command
    await client.process_commands(message)

    #Prevents bot from responding to other bots
    if message.author == client.user:
        return

    channel = message.channel
    username = message.author.name
    time = str(message.timestamp)

    #responds ONLY if it's daniel's bot
    if message.author.id == "563857467444953091":
        await client.send_message(channel, message.content)

    if message.author.bot:
        return

    #Ping Pong
    if message.content.lower().startswith('ping'):
        print(username + " has triggered pong at " + time)
        await client.send_message(channel, "Pong!")

    #Hello
    if "hello" in message.content.lower() or " hi " in message.content.lower():
        print(username + " has triggered hello at " + time)
        await client.send_message(channel, "Hello {0.author.mention}".format(message))

    #Wew lad
    if message.content.lower().startswith('wew'):
        print(username + " has triggered wew at " + time)
        await client.send_message(channel, "lad")

    #no u
    if message.content.lower().startswith("no u"):
        print(username + " has triggered no u at " + time)
        await client.send_message(channel, "no u")

    #waterloo
    if "waterloo" in message.content.lower():
        print(username + " has triggered waterloo at " + time)
        await client.send_message(channel, "Praise Mr. Goose!")
    
    #loo
    if " loo " in message.content.lower():
        print(username + " has triggered the loo at " + time)
        embedA = discord.Embed()
        embedB = discord.Embed()
        embedA.set_image(url='https://www.etac.com/c4images/Etac-Hi-Loo-with-Brackets_548785.jpg')
        embedB.set_image(url='https://uwaterloo.ca/future-students/sites/ca.future-students/files/uploads/images/engineering_5_2_.jpg')
        # toilet emoji ":toilet:"
        emojiA = '\U0001f6bd'
        # grad cap emoji ":mortar_board:"
        emojiB = '\U0001f393'
        await client.send_message(channel, "Which loo r u talking about?")
        await client.send_message(channel, embed=embedA)
        await client.send_message(channel, embed=embedB)
        await message.add_reaction(emojiA)
        await message.add_reaction(emojiB)

    #AP
    if " ap " in message.content.lower():
        print(username + " has triggered ap at " + time)
        await client.send_message(channel, "Haha Ay Pee")

    #weeb alert
    if "anime" in message.content.lower() or "manga" in message.content.lower():
        print(username + " has triggered anime at " + time)
        await client.send_message(channel, "F-ing weebs")

    #nuts
    if "nuts" in message.content.lower():
        print(username + " has triggered nuts at " + time)
        await client.send_message(channel, "nuts")

    if "ib" in message.content.lower():
        print(username + " has triggered ib at " + time)
        await client.send_message(channel, "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the International Baccalaureatte Programme, and I've been involved in numerous secret raids on IB past papers, and I have over 300 CAS hours. I am trained in topnotch bullshitting and I'm the top student in the entire world. You are nothing to me but just another failure. I will wipe you the fuck out with all my 7s of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of TOK gods around the world and your IB candidate number is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little mark that you call a 4. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my extensive EE knowledge. Not only am I extensively trained in Creativity, Action and Service, but I have access to the entire arsenal of the IB Higher Level curriculum and I will use it to its full extent to wipe your miserable Math Studies ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot who only took 4 HLs. I will shit Mathematics and Physics HL all over you and you will drown in it. You're fucking dead, kiddo.")

    #cecil
    if "cecil" in message.content.lower():
        if random.randint(1, 4) == 1:
            print(username + " has triggered cecil at " + time)
            await client.send_message(channel, "i think its hilarious u kids talking shit about cecil. u wouldnt say this shit to him at lan, hes jacked. not only that but he wears the freshest clothes, eats at the chillest restaurants and hangs out with the hottest dudes. yall are pathetic lol")

    #neko
    if message.content.lower().startswith('neko'):
        print(username + " has triggered neko at " + time)
        embed = discord.Embed(
            title = 'Neko',
            description = "F-ing weebs",
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://www.dictionary.com/e/wp-content/uploads/2018/04/neko-300x300.jpg')
        await client.send_message(channel, embed=embed)

    #carlos
    if "carlos" in message.content.lower():
        print(username + " has triggered carlos at " + time)
        embed = discord.Embed(
            title = 'CarlosFlex',
            description = "TOK GOD",
            colour = discord.Color.blue()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/320569792048267264/525524309968420865/IMG_20181220_212849.jpg')
        await client.send_message(channel, embed=embed)

    #tony
    if "tony" in message.content.lower():
        print(username + " has triggered tony at " + time)
        embed = discord.Embed(
            title = 'TonyWUT',
            colour = discord.Color.blue()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/370348514523217922/564518457153028117/TonyMeme2.PNG')
        await client.send_message(channel, embed=embed)

    #richard
    if "richard" in message.content.lower():
        print(username + " has triggered richard at " + time)
        embed = discord.Embed(
            title='RichardAmuse',
            colour=discord.Color.blue()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/370348514523217922/564518542964162669/RichardAmuse.png')
        await client.send_message(channel, embed=embed)

    #sieg hail
    if "sieg hail" in message.content.lower():
        print(username + " has triggered sieg hail at " + time)
        embed = discord.Embed(
            title='SiegHail',
            colour=discord.Color.blue()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/370348514523217922/564518611578781706/CarlosMeme4.png')
        await client.send_message(channel, embed=embed)

    #western
    if "western" in message.content.lower():
        print(username + " has triggered western at " + time)
        embed = discord.Embed(
            title='DanielWestern',
            colour=discord.Color.blue()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/370348514523217922/564518722237235240/DanMeme2.png')
        await client.send_message(channel, embed=embed)

@client.command(name="ping",
                description="Ping Pong",
                pass_context=True)
async def ping(ctx):
    print(ctx.message.author.name + " has triggered ping command at " + str(ctx.message.timestamp))
    await client.say('Pong!')

#Rolls a dice from given numbers
@client.command(name="roll",
                description="Rolls a NdN dice where the first N is the number of rolls and the second N is the number of faces",
                pass_context=True)
async def roll(ctx, dice: str):
    print(ctx.message.author.name + " has triggered roll command at " + str(ctx.message.timestamp))
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say("Format has to be NdN")
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    author = ctx.message.author.mention
    await client.say(author + " rolled " + result)

#Clears logs
@client.command(name="clear",
                description="Clears past x messages. Be careful when using this command",
                pass_context=True)
async def clear(ctx, amount=100):
    #channel = ctx.message.channel
    #messages = []
    #async for message in client.logs_from(channel, limit=int(amount)):
    #    messages.append(message)
    #await client.delete_messages(messages)
    #await client.say("Messages deleted.")
    print(ctx.message.author.name + " has triggered clear command at " + str(ctx.message.timestamp))
    await client.say("This is supposed to clear the past x amount of messages but I disabled it so that someone won't accidentally trigger it.")

#Voting on something
@client.command(name="vote",
                description="Adds thumbsup and thumbsdown reaction to a message for user voting",
                pass_context=True)
async def vote(ctx, *args):
    print(ctx.message.author.name + " has triggered vote command at " + str(ctx.message.timestamp))
    msg = ctx.message
    await client.add_reaction(msg, "👍")
    await client.add_reaction(msg, "👎")

client.run(TOKEN)
