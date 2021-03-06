from json import load
from discord.ext.commands import Bot

BOT_PREFIX = "?"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    #Prevents bot from responding to other bots, including itself.
    if message.author.bot:
        return

    #Checks if sent message starts with "hello" and responds
    if message.content.lower().startswith("hello"):
        msg = f"Hello {message.author.mention}"
        await client.send_message(message.channel, msg)

@client.command()
#Command for "?ping" that responds with "Pong"
async def ping():
    await client.say("Pong")

@client.command()
#Command for "?square x" where x is a number that responds with the square of x.
async def square(number: int):
    squared_value = number ** 2
    await client.say(f"{number} squared is {squared_value}")

client.run(load(open("./token.json", r))["token"])