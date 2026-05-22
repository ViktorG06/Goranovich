from discord.ext import commands
print("message.py loaded") # for debugging
from database import add_xp 

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("MessageEvents INIT")
            
    @commands.Cog.listener()
    async def on_message(self, message):
        print("on_message triggerred")
        if message.author == self.bot.user:
            return

        responses= {
            "hello": "Hi!",
            "bye": "Goodbye!",
            "who": "Asked?",
            "tutrakan": "Top 2 cities, and it aint number 2",
            "zdr": "kp",
            "brat": "sestro"
        }

        content = message.content.lower()

        for word, reply in responses.items():            
            if word in content:
                await message.channel.send(reply)

        print("before XP")

        try:
            add_xp(message.author.id, 10)
        except Exception as e:
            print("XP error:", e)


async def setup(bot):
    # This must be awaited in discord.py 2.0+
    await bot.add_cog(MessageEvents(bot))
