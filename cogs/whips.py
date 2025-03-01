import discord
import funcs
from discord.ext import commands


class Whips(commands.Cog):

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    ###Add Whip Command###
    @discord.slash_command(name="addwhip", description="Add a bill to the list of whips")
    async def addwhip(self, ctx, bill: str, vote: str):
        roles = funcs.updateroles()
        usesID = funcs.updateuseid()
        required_role = roles["whipRole"]
        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]
            
        if not hasRole:
            await ctx.respond("Fuck off! Who the hell do you think you are?!")
            await funcs.sendWebhook(f"❌ **addWhip** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")
            return  
        else:

            # Load current whip data
            data = funcs.load_data()

            # Add bill and vote to whip data
            data[bill] = vote.upper()

            # Save updated data
            funcs.save_data(data)

            await ctx.respond(f"The vote for bill '{bill}' has been recorded as '{vote.upper()}'.")
            await funcs.sendWebhook(f"✅ **addWhip** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")

    ###Remove Whip Command###
    @discord.slash_command(name="rmwhip", description="Remove a bill from the list of whips")
    async def rmwhip(self, ctx, bill: str):
        roles = funcs.updateroles()
        usesID = funcs.updateuseid()
        required_role=roles["whipRole"]

        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            # Load current data
            data = funcs.load_data()

            # Check if bill exists in data
            if bill in data:
            
                # Remove bill from data
                del data[bill]
            
                # Save updated data
                funcs.save_data(data)
                await ctx.respond(f"The vote for bill '{bill}' has been successfully removed.", ephemeral=True)
            else:
                await ctx.respond(f"No vote was found for the bill '{bill}'.", ephemeral=True)
            await funcs.sendWebhook(f"✅ **rmwhip** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Piss off! You can't do that!")
            await funcs.sendWebhook(f"❌ **rmwhip** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")

    ###Whips Command###
    @discord.slash_command(name="whips", description="View a list of all current whips")
    async def whips(self, ctx):
        roles = funcs.updateroles()
        usesID = funcs.updateuseid()
        required_role = roles["btRole"]
        if usesID == True:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            data = funcs.load_data()
            if data:
                embed = discord.Embed(
                title="Whips",
                description="A list of all current whips",
                color=discord.Color.blue(),
                )

                embed.add_field(name="", value="\n".join([f"**{bill}**: *{vote}*" for bill, vote in data.items()]), inline=False)

                await ctx.respond(embed=embed, ephemeral=True)
            else:
                await ctx.respond("No whips have been recorded yet.", ephemeral=True)
                await funcs.sendWebhook(f"✅ **Whips** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Can't do that, you loser!")
            await funcs.sendWebhook(f"❌ **Whips** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")

    @discord.slash_command(name="getwhip", description="Get the whip for a certain bill")
    async def getwhip(self, ctx, bill: str):
        roles = funcs.updateroles()
        usesID = funcs.updateuseid()
        required_role = roles["btRole"]
        if usesID:
            hasRole = required_role in [role.id for role in ctx.author.roles]
        else:
            hasRole = required_role in [role.name for role in ctx.author.roles]

        if hasRole:
            # Load whip data
            data = funcs.load_data()
            bill_lower = bill.lower()
            matching_key = next((key for key in data.keys() if key.lower() == bill_lower), None)

            if matching_key:
                await ctx.respond(f"The recorded vote for bill '**{bill}**' is '**{data[matching_key]}**'.", ephemeral=True)
            else:
                await ctx.respond(f"No vote has been recorded for bill '{bill}'.", ephemeral=True)
            await funcs.sendWebhook(f"✅ **getWhip** Command executed in '**{ctx.guild.name}**' ID: **{ctx.guild.id}**")
        else:
            await ctx.respond("Nuhuh. That's only for the cool kids!")
            await funcs.sendWebhook(f"❌ **getWhip** Command refused in '**{ctx.guild.name}**' ID: **{ctx.guild.id}** from **{ctx.author}** ID: **{ctx.author.id}**")


#Set up bot
def setup(bot):
    bot.add_cog(Whips(bot)) # add the cog to the bot