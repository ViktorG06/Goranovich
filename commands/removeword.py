from database import remove_restricted_word
from discord.ext import commands
print("removetword.py loaded")

class RemoveWord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeword(self, ctx, *, word: str):
        word = word.lower()

        success = remove_restricted_word(ctx.guild.id, word)

        if success:
            await ctx.send(f"The word '{word}' has been removed from the restricted list.")
        else:
            await ctx.send(f"The word '{word}' was not found in the restricted list.")

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(RemoveWord(bot))