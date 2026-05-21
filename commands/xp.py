from discord.ext import commands
from database import get_user
print("xp.py loaded")

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="xp", aliases=["rank"])
    async def xp(self, ctx):
        user = get_user(ctx.author.id)

        if user:
            await ctx.send(f"User XP: {user[1]}")
        else:
            await ctx.send("No data yet.")

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(XP(bot))