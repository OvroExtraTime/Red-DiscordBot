import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
import os
from .utils.chat_formatting import *

class Account:
    """The Account Cog"""

    def __init__(self, bot):
        self.bot = bot
        self.profile = "data/account/accounts.json"
        self.nerdie = dataIO.load_json(self.profile)
    
    @commands.command(name="signup", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _reg(self, ctx):
        """Sign up to get your own account today!"""

        server = ctx.message.server
        user = ctx.message.author
        
        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            self.nerdie[server.id][user.id] = {}
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:", value="You have officaly created your account for **{}**, {}.".format(server, user.mention))
            await self.bot.say(embed=data)
        else: 
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Oops, it seems like you already have an account, {}.".format(user.mention))
            await self.bot.say(embed=data)
        
    
    @commands.command(name="account", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _acc(self, ctx, user : discord.Member=None):
        """Your/Others Account"""
                    
        server = ctx.message.server
        
        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if not user:
            user = ctx.message.author
            if user.id in self.nerdie[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Favourite Team" in self.nerdie[server.id][user.id]:
                    Favourite Team = self.nerdie[server.id][user.id]["Favourite Team"]
                    data.add_field(name="Favourite Team:", value=Favourite Team)
                else:
                    pass
                if "Favourite Player" in self.nerdie[server.id][user.id]:
                    Favourite Player = self.nerdie[server.id][user.id]["Favourite Player"]
                    data.add_field(name="Favourite Player:", value=Favourite Player)
                else:
                    pass
                if "Favourite Manager" in self.nerdie[server.id][user.id]:
                    Favourite Manager = self.nerdie[server.id][user.id]["Favourite Manager"]
                    data.add_field(name="Favourite Manager:", value=Favourite Manager)
                else:
                    pass
                if "Favourite Video Game" in self.nerdie[server.id][user.id]:
                    Favourite Video Game = self.nerdie[server.id][user.id]["Favourite Video Game"]
                    data.add_field(name="Favourite Video Game:", value=Favourite Video Game)
                else:
                    pass 
                if "Job" in self.nerdie[server.id][user.id]:
                    job = self.nerdie[server.id][user.id]["Job"]
                    data.add_field(name="FIFA or PES:", value=job)
                else:
                    pass
                if "Favourite Stadium" in self.nerdie[server.id][user.id]:
                    Favourite Stadium = self.nerdie[server.id][user.id]["Favourite Stadium"]
                    data.add_field(name="Favourite Stadium:", value=Favourite Stadium)
                else:
                    pass
                if "Other" in self.nerdie[server.id][user.id]:
                    other = self.nerdie[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                prefix = ctx.prefix
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
                await self.bot.say(embed=data)
        else:
            server = ctx.messFavourite Team.server
            if user.id in self.nerdie[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Favourite Team" in self.nerdie[server.id][user.id]:
                    town = self.nerdie[server.id][user.id]["Favourite Team"]
                    data.add_field(name="Favourite Team", value=town)
                else:
                    pass
                if "Favourite Player" in self.nerdie[server.id][user.id]:
                    Favourite Player = self.nerdie[server.id][user.id]["Favourite Player"]
                    data.add_field(name="Favourite Player:", value=Favourite Player)
                else:
                    pass
                if "Favourite Manager" in self.nerdie[server.id][user.id]:
                    Favourite Manager = self.nerdie[server.id][user.id]["Favourite Manager"]
                    data.add_field(name="Favourite Manager:", value=Favourite Manager)
                else:
                    pass
                if "Favourite Video Game" in self.nerdie[server.id][user.id]:
                    Favourite Video Game = self.nerdie[server.id][user.id]["Favourite Video Game"]
                    data.add_field(name="Favourite Video Game:", value=Favourite Video Game)
                else:
                    pass 
                if "Job" in self.nerdie[server.id][user.id]:
                    job = self.nerdie[server.id][user.id]["Job"]
                    data.add_field(name="FIFA or PES:", value=job)
                else:
                    pass
                if "Favourite Stadium" in self.nerdie[server.id][user.id]:
                    Favourite Stadium = self.nerdie[server.id][user.id]["Favourite Stadium"]
                    data.add_field(name="Favourite Stadium:", value=Favourite Stadium)
                else:
                    pass
                if "Other" in self.nerdie[server.id][user.id]:
                    other = self.nerdie[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="{} doesn't have an account at the moment, sorry.".format(user.mention))
                await self.bot.say(embed=data)

    @commands.group(name="update", pass_context=True, invoke_without_command=True, no_pm=True)
    async def update(self, ctx):
        """Update your TPC"""
        await send_cmd_help(ctx)

    @update.command(pass_context=True, no_pm=True)
    async def Favourite Manager(self, ctx, *, Favourite Manager):
        """Tell us Favourite Manager yourself"""
        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix

        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass
        
        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Favourite Manager" : Favourite Manager})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have updated your Favourite Manager Me to{}".format(Favourite Manager))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def Favourite Player(self, ctx, *, Favourite Player):
        """Do you have a Favourite Player?"""
        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix
        
        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Favourite Player" : Favourite Player})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Favourite Player to {}".format(Favourite Player))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def Favourite Team(self, ctx, *, Favourite Team):
        """How old are you?"""
        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix

        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Favourite Team" : Favourite Team})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Favourite Team to {}".format(Favourite Team))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def job(self, ctx, *, job):
        """Do you have a job?"""
        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix

        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Job" : job})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Job to {}".format(job))
            await self.bot.say(embed=data)
    
    @update.command(pass_context=True, no_pm=True)
    async def Favourite Video Game(self, ctx, *, Favourite Video Game):
        """What's your Favourite Video Game?"""

        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix
                
        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Favourite Video Game" : Favourite Video Game})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Favourite Video Game to {}".format(Favourite Video Game))
            await self.bot.say(embed=data)
 
    @update.command(pass_context=True, no_pm=True)
    async def Favourite Stadium(self, ctx, *, Favourite Stadium):
        """What's your Favourite Stadium?"""

        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix

        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Favourite Stadium" : Favourite Stadium})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Favourite Stadium to {}".format(Favourite Stadium))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def other(self, ctx, *, other):
        """Incase you want to add anything else..."""
        
        server = ctx.messFavourite Team.server
        user = ctx.messFavourite Team.author
        prefix = ctx.prefix

        if server.id not in self.nerdie:
            self.nerdie[server.id] = {}
        else:
            pass

        if user.id not in self.nerdie[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.nerdie[server.id][user.id].update({"Other" : other})
            dataIO.save_json(self.profile, self.nerdie)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Other to {}".format(other))
            await self.bot.say(embed=data)

def check_folder():
    if not os.path.exists("data/account"):
        print("Creating data/account folder...")
        os.makedirs("data/account")

def check_file():
    data = {}
    f = "data/account/accounts.json"
    if not dataIO.is_valid_json(f):
        print("I'm creating the file, so relax bruh.")
        dataIO.save_json(f, data)

def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(Account(bot))
