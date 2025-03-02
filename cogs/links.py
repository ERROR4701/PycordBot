import discord
import funcs
from discord.ext import commands

class Links(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="party", description="Get a link to our party page")
    async def party(self, ctx):
        await ctx.respond("Placeholder for our Party's link")
        await funcs.sendWebhook(f"✅ **Party** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")

    @discord.slash_command(name="house", description="Get a link to the house")
    async def house(self, ctx):
        roles = funcs.updateroles()
        usesID = funcs.updateuseid()
        required_role = roles["btRole"]
        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            await ctx.respond("Placeholder for the link to parliament once McPolitics is back")
            await funcs.sendWebhook(f"✅ **House** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Fuck off! I don't know you!")
            await funcs.sendWebhook(f"❌ **House** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Links(bot)) # add the cog to the bot