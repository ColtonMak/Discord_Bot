# Python Discord Bot Guide
Download and install [Python](https://www.python.org/downloads/). Make sure to install Python 3.6.x as Python3.7+ is not supported by discord.py.

Once Python is installed, install the python package discord.py. Documentation can be found [here](https://github.com/Rapptz/discord.py)

    # Linus/OS X
    python3 -m pip install discord.py
    
    # Windows
    python -m pip install discord.py

## Create a Discord app, bot and server.
Create a new app at <https://discordapp.com/developers/applications/me>. After creating an app, create a bot user. Keep note of your app's **Client ID** and your bot's **token**.

Create a server at <https://discordapp.com> and add your bot to the server using the following link <https://discordapp.com/oauth2/authorize?client_ID=XXXXXXXXXXXXXXXXXXX&scope=bot> where XXXX is replaced with your app's **Client ID**. Select the corresponding server and authorize it.

## Sample Code
```python
from discord.ext.commands import Bot

BOT_PREFIX = "?"
TOKEN = "XXXXXXXXXXXXX"

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

client.run(TOKEN)

```
