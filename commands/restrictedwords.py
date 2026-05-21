from database import get_restricted_words
from discord.ext import commands
print("restrictedwords.py loaded")

class RestrictedWords(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restrictedwords(self, ctx):
        words = get_restricted_words(ctx.guild.id)
        if words:
            msg = "**Restricted words:**\n"

            for word in words:
                msg += f"- {word}\n"

            await ctx.send(msg)
        else:
            await ctx.send("There are no restricted words for this server.")

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(RestrictedWords(bot))