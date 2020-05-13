import discord, gspread
from discord.ext import commands
from discord.utils import get
from oauth2client.service_account import ServiceAccountCredentials


#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#sheets_client = gspread.authorize(creds)


class KickingCog(commands.Cog, name="Kicking Cog"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kickJZ')
    @commands.cooldown(5,3600)
    async def kickJZ(self, ctx):
#        kick_perms = [202278109708419072,201806047478939649,281586814471634945,372553093331812352,206833217678868480]
        kick_perms = [198821468317024256]
        if ctx.author.id in kick_perms:
            self.bot.sheets_client.login()
            kicked = ctx.guild.get_member(254774534274547713)
            invite_chan = ctx.guild.get_channel(513162681558106156)
            invite = await invite_chan.create_invite(max_age = 86400, max_uses = 1)
            if kicked.dm_channel:
                pass
            else:
                await kicked.create_dm()
            dm_chan = kicked.dm_channel
            try:
                nickname = kicked.nick
            except:
                nickname = kicked.name
            user_roles = [kicked.name,nickname,str(254774534274547713)] ###
            for r in kicked.roles:
                if r.name != '@everyone':
                    user_roles.append(str(r.id))
            sheet = self.bot.sheets_client.open_by_key("1jhslwpjOhqU_M-kJd3WuAXb7-AhNzPtCyxe8UBiKcN8")
            rt_sheet = sheet.get_worksheet(1)
            rt_sheet.append_row(user_roles,value_input_option='USER_ENTERED')
            kc_sheet = sheet.get_worksheet(0)
            jz_cell = kc_sheet.cell(2,8)
            new_count = int(jz_cell.value)+1
            kc_sheet.update_cell(2,8,new_count)
            await dm_chan.send(invite)
            await ctx.send(f"""{ctx.author} can kick. Times kicked: {new_count}""")
            await ctx.guild.kick(kicked)
        else:
            await ctx.send(f"""Silly {ctx.author}, kicks are for Dom""")

    @commands.command(name='kickDom')
    @commands.cooldown(5,3600)
    async def kickDom(self, ctx):
#        kick_perms = [202278109708419072,201806047478939649,281586814471634945,372553093331812352,206833217678868480]
        kick_perms = [254774534274547713,201806047478939649]
        if ctx.author.id in kick_perms:
            self.bot.sheets_client.login()
            kicked = ctx.guild.get_member(198821468317024256)
            invite_chan = ctx.guild.get_channel(513162681558106156)
            invite = await invite_chan.create_invite(max_age = 86400, max_uses = 1)
            if kicked.dm_channel:
                pass
            else:
                await kicked.create_dm()
            dm_chan = kicked.dm_channel
            try:
                nickname = kicked.nick
            except:
                nickname = kicked.name
            user_roles = [kicked.name,nickname,str(198821468317024256)] ###
            for r in kicked.roles:
                if r.name != '@everyone':
                    user_roles.append(str(r.id))
            sheet = self.bot.sheets_client.open_by_key("1jhslwpjOhqU_M-kJd3WuAXb7-AhNzPtCyxe8UBiKcN8")
            rt_sheet = sheet.get_worksheet(1)
            rt_sheet.append_row(user_roles,value_input_option='USER_ENTERED')
            kc_sheet = sheet.get_worksheet(0)
            dom_cell = kc_sheet.cell(2,9)
            new_count = int(dom_cell.value)+1
            kc_sheet.update_cell(2,9,new_count)
            await dm_chan.send(invite)
            await ctx.send(f"""{ctx.author} can kick. Times kicked: {new_count}""")
            await ctx.guild.kick(kicked)
        else:
            await ctx.send(f"""Silly {ctx.author}, kicks are for JZ""")

    @commands.command(name='sudoku')
    async def sudoku(self, ctx):
        try:
            self.bot.sheets_client.login()
            invite_chan = ctx.guild.get_channel(513162681558106156)
            invite = await invite_chan.create_invite(max_age = 86400, max_uses = 1)
            if ctx.author.dm_channel:
                pass
            else:
                await ctx.author.create_dm()
            dm_chan = ctx.author.dm_channel
            sheet = self.bot.sheets_client.open_by_key("1jhslwpjOhqU_M-kJd3WuAXb7-AhNzPtCyxe8UBiKcN8")
            kc_sheet = sheet.get_worksheet(0)
            rt_sheet = sheet.get_worksheet(1)
            auth_id = str(ctx.author.id)
            try:
                snowflake_cell = kc_sheet.find(auth_id)
            except:
                kc_sheet.append_row([ctx.author.name,auth_id,0],value_input_option='USER_ENTERED')
                snowflake_cell = kc_sheet.find(auth_id)
            count_cell = kc_sheet.cell(snowflake_cell.row,snowflake_cell.col+1)
            new_count = int(count_cell.value)+1
            user_roles = [ctx.author.name,ctx.author.nick,auth_id] ###
            role_names = []
            for r in ctx.author.roles:
                role_names.append(r.name)
                if r.name != '@everyone':
                    user_roles.append(str(r.id))
            if 'General Manager' in role_names or 'Captain' in role_names:
                    await ctx.channel.send(f"""bruh I can't kick you""")
            else:
                kc_sheet.update_cell(count_cell.row,count_cell.col,new_count)
                rt_sheet.append_row(user_roles,value_input_option='USER_ENTERED')
                await dm_chan.send(invite)
                await ctx.channel.send(f"""{ctx.author} took the honorable way out. Times sudoku'd: {new_count}""")
                await ctx.guild.kick(ctx.author)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
#        else:
#            await ctx.send('**`SUCCESS`**')

    @commands.command(name='sudoku_leaders')
    async def sudoku_leaders(self,ctx):
        try:
            self.bot.sheets_client.login()
            sheet = self.bot.sheets_client.open_by_key("1jhslwpjOhqU_M-kJd3WuAXb7-AhNzPtCyxe8UBiKcN8")
            kc_sheet = sheet.get_worksheet(0)
            leaderboard = kc_sheet.get_all_values()
            lines = ['+----------------------+-------+',
                     '|         NAME         | KICKS |',
                     '+----------------------+-------+']
            for leader in leaderboard[1:]:
                name = (20-len(leader[0]))*" "+leader[0]
                kicks = (5-len(leader[2]))*" "+leader[2]
                score_line = ("| " + name + " | " + kicks + " |")
                lines.append(score_line)
#                for i in range(len(score_line)):
#                    str_len = len(score_line[i])
#                    score_line[i] = (30-str_len)*" "+score_line[i]
#                    newline = ("| "+i[0]+" | "+i[1]+" | "+i[2]+" | "+i[3]+" |")
#                    lines.append(newline)
            msg = '```'
            for i in lines:
                msg = msg + i + "\n"
            msg = msg + "```"
            await ctx.send(f'Sudoku leaderboard:')
            await ctx.send(msg)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event
        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        Check above for a list of events.
        """
        self.bot.sheets_client.login()
        sheet = self.bot.sheets_client.open_by_key("1jhslwpjOhqU_M-kJd3WuAXb7-AhNzPtCyxe8UBiKcN8")
#        kc_sheet = sheet.get_worksheet(0)
        rt_sheet = sheet.get_worksheet(1)
        try:
            snowflake_cell = rt_sheet.find(str(member.id))
            nickname_cell = rt_sheet.cell(snowflake_cell.row,2).value ###
            role_cells = rt_sheet.row_values(snowflake_cell.row)[3:] ###
            role_list = []
            for i in role_cells:
                role_list.append(get(member.guild.roles,id=int(i)))
            await member.add_roles(*role_list)
            await member.edit(nick=nickname_cell) ###
            rt_sheet.delete_row(snowflake_cell.row)
            if ('688787927701913696' in role_cells or '688787624412053656' in role_cells): ### If members have Hitter or Pitcher role, remove the auto-added Guest role
                await member.remove_roles(get(member.guild.roles,id=513867033390219266)) ###
        except Exception as e:
            print(f'**`ERROR:`** {type(e).__name__} - {e}')



def setup(bot):
    bot.add_cog(KickingCog(bot))