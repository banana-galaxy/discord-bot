import discord
from discord.ext import commands

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
    async def purge(self, ctx, *, content:str):
        await delete(int(content))
        await ctx.send(str(content))

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