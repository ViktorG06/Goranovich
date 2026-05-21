from discord.ext import commands
import discord
import config
import random
print("poke.py loaded")

poke_messages = [
    "poked you... I wonder why",
    "poked you. Pokey, pokey, pokey.",
    "told me you'd get poked. Strange guy.",
    "is thinking about you. Do something about it :)",
    "is poking you, wake up.",
    "pokes you. I hope you're not ticklish",
    "gave me instructions to poke you.",
]

msg = random.choice(poke_messages)

class Poke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poke(self, ctx, member: discord.Member):
        if member.bot:
            await ctx.send("You can't poke bots :)")
            return

        elif member == ctx.author:
            await ctx.send("Done.")
            await member.send("You poked yourself, haha!")
            return

        else:
            try:
                await member.send(msg)
                await ctx.send("Done.")     
                await member.send(f"{ctx.author.name} {msg}")

            except:
                await ctx.send(f"I couldn't poke {member.name}. They may have DMs off")        

async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(Poke(bot))