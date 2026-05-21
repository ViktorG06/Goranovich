import discord
from discord.utils import get
from discord.ext import commands
print("rolecreate.py loaded")

class RoleCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rolecreate(self, ctx, *, role_name: str):
        duplicate_check = get(ctx.guild.roles, name = role_name)
       
        if duplicate_check is None:
            role = await ctx.guild.create_role(name = role_name, colour = discord.Colour.blue())
            await ctx.author.add_roles(role, reason = None, atomic = True)
            await ctx.send(f"Role '{role_name}' has been created and assigned to you.")
        else:
            await ctx.send("That role already exists!")
        
async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(RoleCreate(bot))