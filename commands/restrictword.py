from database import add_restricted_word
from discord.ext import commands
print("restrictword.py loaded")

class RestrictWord(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restricword(self, ctx, *, word: str):
        word = word.lower()

        success = add_restricted_word(ctx.guild.id, word, ctx.author.id)

        if success:
            await ctx.send(f"The word '{word}' has been added to the restricted list.")
        else:
            await ctx.send(f"The word '{word}' is already restricted.")
async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(RestrictWord(bot))