import asyncio, discord, os, sys, traceback
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
load_dotenv()

#Discord config
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# All cogs are in a 'cogs' folder in the same directory as the overall file. You can do an "import all" thing, but I like having them specifically listed.
# Only "essential" cog is Owner, which has commands that let you load and unload cogs.
initial_extensions = [
                      'cogs.owner',
                      'cogs.dice'
                                   ]
# Initializing the bot itself. The command_prefix option lets every command in a cog have that prefix, coded only once here.
bot = commands.Bot(command_prefix='p!',description='The Pioneer Multipurpose Bot',owner_id=202278109708419072)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

bot.run(TOKEN, bot=True, reconnect=True)
