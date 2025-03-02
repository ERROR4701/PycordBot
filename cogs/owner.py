import discord
import funcs
from dotenv import set_key
from discord.ext import commands

class Owner(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    ###Message Command###
    @discord.slash_command(name="message")
    @discord.command.is_owner()
    async def message(self, ctx, channel_id, message: str):
        isOwner = ctx.author.id == funcs.ownerID

        if isOwner:
            channel = await self.bot.fetch_channel(int(channel_id))
            if channel:  # Check if channel exists
                await channel.send(message)
                await ctx.respond("Message sent!", ephemeral=True)
            else:
                await ctx.respond("Channel not found.", ephemeral=True)
            set_key(".env", "last_msg_cmd", message)
            await funcs.sendWebhook(f"🚨 **Message** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** by **{ctx.author}** ID: **{ctx.author.id}**\nWith the Message:\n'{message}'")
        else:
            print("Message Command Permission denied")
            await ctx.respond("Denied", ephemeral=True, delete_after=0.0001)
            await funcs.sendWebhook(f"⚠️ **Message** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**\nWith the Message:\n'{message}'")
        
    ###Guilds Command###
    @discord.slash_command(name="guilds")
    @discord.command.is_owner()
    async def guilds(self, ctx):
        isOwner = ctx.author.id == funcs.ownerID

        if isOwner:
            guild_list = [f"- {guild.name} (ID: {guild.id})" for guild in self.bot.guilds]
            guilds_message = "\n".join(guild_list)
            print(guilds_message)
            
            if len(guilds_message) > 2000: #Discord Message Limit
                await ctx.respond("The List is too long", ephemeral=True)
            else:
                await ctx.respond(f"{guilds_message}", ephemeral=True)
            await funcs.sendWebhook(f"🚨 **Guilds** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** by **{ctx.author}** ID: **{ctx.author.id}**")
        else:
            print("Guilds command permission denied")
            await ctx.respond("Denied", ephemeral=True, delete_after=0.0001)
            await funcs.sendWebhook(f"⚠️ **Guilds** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")

    ###Leave Command###
    @discord.slash_command(name="leave")
    @discord.command.is_owner()
    async def leave(self, ctx, guild_id):
        isOwner = ctx.author.id == funcs.ownerID

        if isOwner:
            try:
                guildName=await self.bot.fetch_guild(int(guild_id)) #Get guild name from guild ID
            except:
                await ctx.respond("No guild found!", ephemeral=True)
                
            await funcs.sendWebhook(f"🚨 **Leave** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** by **{ctx.author}** ID: **{ctx.author.id}**\nServer left:\n**{guildName}** ID: **{guild_id}**")
            if guildName: #Check if guild name could be fetched. If it couldn't = guild doesn't exist
                await self.bot.get_guild(guild_id).leave() #Leave guild using ID
                await ctx.respond(f"I have left **{guildName}** ID: **{guild_id}**", ephemeral=True)
            else:
                await ctx.respond("No guild found!", ephemeral=True)
        else:
            print("Leave command permission denied")
            await ctx.respond("Denied", ephemeral=True, delete_after=0.0001)
            await funcs.sendWebhook(f"⚠️ **Leave** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Owner(bot)) # add the cog to the bot