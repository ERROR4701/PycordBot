import discord
import funcs
from discord.ext import commands

class Triggers(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg = message.content.lower()
        #Check message author is not webhook or this bot
        if not message.webhook_id and not message.author.bot:
            #Ping
            if "ping" in msg:
                await message.channel.send("Pong")
                await funcs.sendWebhook(f"✅ **Pong** executed in '**{message.guild.name}**' ID: **{message.guild.id}**")
            #Far Right
            if "far right" in msg:
                await message.channel.send("Dab on the Far Right")
                await funcs.sendWebhook(f"✅ **Dab on Far Right** executed in '**{message.guild.name}**' ID: **{message.guild.id}**")
            #Far Left
            if "far left" in msg:
                await message.channel.send("Dab on the Far Left")
                await funcs.sendWebhook(f"✅ **Dab on Far Left** executed in '**{message.guild.name}**' ID: **{message.guild.id}**")
            #Baden
            if "baden" in msg and not "württemberg" in msg:
                await message.channel.send("https://tenor.com/view/ulm-donau3fm-schwaben-schw%C3%A4bisch-stuttgart-gif-13299565")
                await message.add_reaction("🤮")
                await funcs.sendWebhook(f"✅ **Baden** executed in '**{message.guild.name}**' ID: **{message.guild.id}**")
            #Schwaben
            if "schwaben" in msg or "swabia" in msg or "württemberg" in msg:
                await message.channel.send("https://tenor.com/view/yes-awesome-rosa-stuttgart-granny-gif-13299086")
                await funcs.sendWebhook(f"✅ **Schwaben** executed in '**{message.guild.name}**' ID: **{message.guild.id}**")
                if "baden" in msg:
                    await message.channel.send("Minus Baden!")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Triggers(bot)) # add the cog to the bot