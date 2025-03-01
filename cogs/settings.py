import discord
import funcs
from dotenv import set_key, load_dotenv
from discord.ext import commands

class settings(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    ###Set BT Role Command###
    @discord.slash_command(name="setbtrole", description="Change the Name/ID of the Bundestag Member Role")
    async def setbtrole(self, ctx, role):
        usesID = funcs.updateuseid()
        roles = funcs.updateroles()
        required_role = roles["chairRole"]
        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            set_key(".env", "btRole", role)
            await ctx.respond(f"The Bundestag Role has been set to **{role}**", ephemeral=True)
            await funcs.sendWebhook(f"✅ **setbtrole** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Nope, can't do that!")
            await funcs.sendWebhook(f"❌ **setbtrole** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")

    ###Set Whip Role Command###
    @discord.slash_command(name="setwhiprole", description="Change the Name/ID of the Whip Role")
    async def setwhiprole(self, ctx, role):
        usesID = funcs.updateuseid()
        roles = funcs.updateroles()
        required_role = roles["chairRole"]
        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            set_key(".env", "whipRole", role)
            await ctx.respond(f"The Whip Role has been set to **{role}**", ephemeral=True)
            await funcs.sendWebhook(f"✅ **setwhiprole** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Nope, can't do that!")
            await funcs.sendWebhook(f"❌ **setwhiprole** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")

    @discord.slash_command(name="useid", description="Set whether the bot should use role IDs or names")
    async def useid(self, ctx, status: bool):
        usesID = funcs.updateuseid()
        roles = funcs.updateroles()
        required_role = roles["chairRole"]

        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            if status.lower() == "true":
                set_key(".env", "usesid", status.lower())
                await ctx.respond("UsesID has been set to **True**.")
            elif status.lower() == "false":
                set_key(".env", "usesid", "")
                await ctx.respond("UsesID has been set to **False**.")
            else:
                await ctx.send("Please use either '**True**' or '**False**'.")
            await funcs.sendWebhook(f"✅ **useid** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**\nusesID set to:\n**{status.lower()}**")
        else:
            await ctx.send("Nope")
            await funcs.sendWebhook(f"❌ **useid** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(settings(bot)) # add the cog to the bot