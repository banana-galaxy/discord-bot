import discord
from discord.ext import commands
import asyncio

...


# other imports you need

# make a class with your name as a commands.Cog class.
class MyCog(commands.Cog):
    # as this is not the main file you need to make a global variable called bot.
    def __init__(self, bot):
        self.bot = bot
        # define other variables

    # create a command using commands.command (not bot.command)
    @commands.command()
    async def delete_hitler(self, ctx):
        async for message in ctx.channel.history(limit = 10000):
            if message.author.id == 628281248879607809:
                message.delete()

    @commands.command()
    async def purge(self, ctx, person: discord.User, delete_limit=1000000):
        if "mod" in [y.name.lower() for y in ctx.author.roles]:
            def is_person(m):
                return m.author == person
            if ctx.message.author == person:
                await ctx.channel.purge(limit=(delete_limit+1), check=is_person)
            else:
                await ctx.channel.purge(limit=delete_limit, check=is_person)
        '''async for message in ctx.channel.history(limit=int(delete_limit)):
            if message.author == person:
                await message.delete()'''
        #else:
        #    await ctx.send("Sorry, you do not have access to this command!", delete_after=2.0)

    '''@commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount= 1000, author: discord.User = None):  # Purge ANY message by default
        """Purge said amount of messages"""
        if author is None:
            await ctx.channel.purge(limit=amount)
            return
        else:
            if isinstance(author, discord.User):
                author_id = author.id
            else:
                author_id = author

        await ctx.channel.purge(limit=(amount+1), check=lambda m: m.author.id == author_id)'''

    @commands.command()
    async def nuke(self, ctx, delete_limit=1000000):
        if "mod" in [y.name.lower() for y in ctx.author.roles]:
            await ctx.channel.purge(limit=delete_limit)
            await ctx.send("Nuked :thumbsup: https://tenor.com/view/explosion-gif-5940694", delete_after=2.5)
        else:
            await ctx.send("Sorry, you do not have access to this command!", delete_after=2.0)
            await ctx.message.delete(delay=2.0)

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
    bot.add_cog(MyCog(bot))