#sudo nohup python3.8 tobreenoip.py > tobreenoip.txt &
#ps aux | grep -i python
import re, statistics, random, operator, csv, time, collections, io, string, asyncio, discord, os, gspread, sys, traceback
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
load_dotenv()
#Discord config
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#Sheets config
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
sheets_client = gspread.authorize(creds)

initial_extensions = [
                      'cogs.owner',
                      'cogs.sudoku',
                      'cogs.scouter',
                      'cogs.artists',
                      'cogs.mcoh',
                      'cogs.dice'
                                   ]

bot = commands.Bot(command_prefix='p!',description='The Pioneer Multipurpose Bot',owner_id=202278109708419072)
bot.sheets_client = sheets_client

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