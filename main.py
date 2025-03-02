import discord
import os
import funcs
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = discord.Bot(intents=intents, owner_ids=[funcs.ownerID])

if os.getenv("isTest"):
    TOKEN = os.getenv("testTOKEN")
else:
    TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    activity = discord.Activity(type=discord.ActivityType.listening, name="the Order of the Great Diess")
    await bot.change_presence(activity=activity)
    await bot.sync_commands()

@bot.slash_command(name="help", description="View a list of all available commands and trigger words")
async def hello(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="Help",
        description="A list of all available commands and trigger words",
        color=discord.Color.blue(),
    )
    # Commands
    embed.add_field(name="Commands:", value="List of commands:", inline=False)
    embed.add_field(name="/party", value="Returns the link to the SPD's party page", inline=False)
    embed.add_field(name="/house", value="Returns a link to the parliament's page", inline=False)
    embed.add_field(name="/addwhip ['Bill'] [Vote]", value="Allows the whip to add a bill to the current list of whips", inline=False)
    embed.add_field(name="/rmwhip ['Bill']", value="Allows the whip to remove a bill from the current list of whips", inline=False)
    embed.add_field(name="/getwhip ['Bill']", value="Allows members of the Bundestag to get the official party position on a specific bill", inline=False)
    embed.add_field(name="/whips", value="Allows members of the Bundestag to get a full list of all current whips", inline=False)
    embed.add_field(name="/setbtrole ['Bundestag Role']", value="Allows the Party Chair to set the name/ID of the Bundestag Role", inline=False)
    embed.add_field(name="/setwhiprole ['Whip Role']", value="Allows the Party Chair to set the name/ID of the Whip Role", inline=False)
    embed.add_field(name="/useid [True/False]", value="Allows the Party Chair to configure the bot to use Role IDs or names", inline=False)
    
    embed.add_field(name="", value="", inline=False)

    #Trigger Words
    embed.add_field(name="Trigger Words:", value="List of trigger words:", inline=False)
    embed.add_field(name="Ping", value="Pong", inline=False)
    embed.add_field(name="Far Right", value="Bot dabs on the Far Right", inline=False)
    embed.add_field(name="Far Left", value="Bot dabs on the Far Left", inline=False)
    embed.add_field(name="Baden", value="🤮", inline=False)
    embed.add_field(name="Schwaben/Württemberg", value="Oma Rosa", inline=False)
    await ctx.respond(embed=embed, ephemeral=True)

    await funcs.sendWebhook(f"✅ **Help** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")

cogs_list = [
    'whips',
    'triggers',
    'settings',
    'owner',
    'links'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run(TOKEN) # run the bot with the token