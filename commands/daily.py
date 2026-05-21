from discord.ext import commands
import config
from database import claim_daily
print("daily.py loaded")

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        success = claim_daily(ctx.author.id, config.DAILY_XP)

        if success:
            await ctx.send("You claimed your daily XP!")
        else:    
            await ctx.send("You already claimed your daily xp today.")    

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(Daily(bot))