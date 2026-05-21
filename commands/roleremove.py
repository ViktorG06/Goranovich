import discord
from discord.ext import commands
print("roleremove.py loaded")

class RoleRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roleremove(self, ctx, *, role_name: str):
        role = None

        if role_name.startswith("<@&") and role_name.endswith(">"):
            try:
                role_id = int(role_name[3:-1])
                role = ctx.guild.get_role(role_id)
            except ValueError:
                role = None

        if role is None:
            role = discord.utils.find(
                lambda r: r.name.lower() == role_name.lower(),
                ctx.guild.roles,
            )

        if role is None:
            await ctx.send("That role doesn't exist!")
            return
            
        if role not in ctx.author.roles:
            await ctx.send("You don't have that role!")
            return

        await ctx.author.remove_roles(role, reason=None, atomic=True)
        await ctx.send(f"Role '{role.name}' has been removed from you.")


async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(RoleRemove(bot))