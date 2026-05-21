from discord.ext import commands
from database import get_leaderboard
print("leaderboard.py loaded")


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self,ctx):
        data = get_leaderboard()

        msg = "Leaderboard:\n"
        for i, (user_id, xp) in enumerate(data, start = 1):
            msg += f"{i}. <@{user_id}> - {xp} XP\n"

        await ctx.send(msg)

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(Leaderboard(bot))