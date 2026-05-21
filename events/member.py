from discord.ext import commands
print("member_join.py loaded") # for debugging

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        sys_channel = member.guild.system_channel
        if sys_channel:
            await sys_channel.send(f"{str(member)} has joined the server!")
            print(f"{str(member)} has joined the server!")
        # await message.channel.send(f"{str(member)} has joined the server!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        sys_channel = member.guild.system_channel
        if sys_channel:
            await sys_channel.send(f"{str(member)} has left the server.")
        print(f"{str(member)} has left the server.")
        # await message.channel.send(f"{str(member)} has left the server.")


async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(MemberEvents(bot))