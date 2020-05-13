import discord, random
from discord.ext import commands
from discord.utils import get

class ArtistCog(commands.Cog, name="Artists Cog"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gaga')
    async def gaga(self, ctx):
        songs = ['https://www.youtube.com/watch?v=bESGLojNYSo', #Poker Face
                 'https://www.youtube.com/watch?v=qrO4YZeyl0I', #Bad Romance
                 'https://www.youtube.com/watch?v=niqrrmev4mA', #Alejandro
                 'https://www.youtube.com/watch?v=wagn8Wrmzuc', #Judas
                 'https://www.youtube.com/watch?v=Xn599R0ZBwg', #Perfect Illusion
                 'https://www.youtube.com/watch?v=en2D_5TzXCA', #Million Reasons
                 'https://www.youtube.com/watch?v=pco91kroVgQ'] #Applause
        song = random.choice(songs)
        await ctx.send(song)

    @commands.command(name='crj')
    async def crj(self, ctx):
        songs = ['https://youtu.be/L4YbNztrCIA', 
                 'https://youtu.be/6_zD5-ij7So', 
                 'https://youtu.be/J0w4c0o0rHw', 
                 'https://youtu.be/ofZzC9mEj-4'] 
        song = random.choice(songs)
        await ctx.send(song)

    @commands.command(name='kawaiimetal')
    async def babymetal(self, ctx):
        songs = ['https://www.youtube.com/watch?v=WIKqgE4BwAY',
                 'https://www.youtube.com/watch?v=GvD3CHA48pA',
                 'https://www.youtube.com/watch?v=cK3NMZAUKGw',
                 'https://www.youtube.com/watch?v=Uds7g3M-4lQ',
                 'https://www.youtube.com/watch?v=9TkHpvaO09c',
                 'https://www.youtube.com/watch?v=ZpAYnVJX9CY',
                 'https://www.youtube.com/watch?v=wKZbzcUdY1g']
        song = random.choice(songs)
        await ctx.send(song)

    @commands.command(name='kpop')
    async def kpop(self, ctx):
        songs = ['https://www.youtube.com/watch?v=uxmP4b2a0uY',
                 'https://www.youtube.com/watch?v=499YUeNoYVE',
                 'https://www.youtube.com/watch?v=HlN2BXNJzxA',
                 'https://www.youtube.com/watch?v=6yWPfUz0z94',
                 'https://www.youtube.com/watch?v=V2hlQkVJZhE',
                 'https://www.youtube.com/watch?v=kOHB85vDuow',
                 'https://www.youtube.com/watch?v=i0p1bmr0EmE',
                 'https://www.youtube.com/watch?v=mrAIqeULUL0']
        song = random.choice(songs)
        await ctx.send(song)

def setup(bot):
    bot.add_cog(ArtistCog(bot))