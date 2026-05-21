from discord.ext import commands
print("help.py loaded")

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        info_text = ("[Placeholder. To be updated]")
        
        await ctx.send(info_text)

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(Help(bot))