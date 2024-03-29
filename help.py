import discord
from discord.ext import commands
import asyncio

...


# other imports you need

# make a class with your name as a commands.Cog class.
class helpcog(commands.Cog):
    # as this is not the main file you need to make a global variable called bot.
    def __init__(self, bot):
        self.bot = bot
        # define other variables

    # create a command using commands.command (not bot.command)
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="General commands", description="commands available for everyone to use")
        embed.add_field(name="ping", value="bot replies with 'pong', mostly used to test whether the bot is responsive")
        embed.add_field(name="echo [message]", value="bot replies with specified message")
        embed.add_field(name="invite", value="bot invite link")
        await ctx.author.send(content=None, embed=embed)
        if "mod" in [y.name.lower() for y in ctx.author.roles]:
            try:
                self.bot.unload_extension("cogss")
                self.bot.load_extension("cogss")
                embed = discord.Embed(title="Moderation commands", description="commands available for you as a mod to use")
                embed.add_field(name="purge [user] [amount: optional]", value="deletes all messages from specified user unless amount is specified")
                embed.add_field(name="nuke [amount: optional]", value="deletes all messages in the channel unless amount is specified")
                await ctx.author.send(content=None, embed=embed)
            except discord.ext.commands.ExtensionNotLoaded:
                embed = discord.Embed(title="Moderation commands", description="sorry this module is not loaded")
                await ctx.author.send(content=None, embed=embed)

    # add an event using commands.Cog.listener() (not bot.event)
    @commands.Cog.listener()
    # again pass in self then the objects that come with the event
    async def on_message(self, message):
        pass
        #await message.delete()
        # your event


# create a function called setup (this is run when you load the extention)
def setup(bot):
    # add the cog passing in bot (so that you can have self.bot)
    bot.add_cog(helpcog(bot))