import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.environ.get("TOKEN")
channel_id = int(os.environ.get("CHANNEL_ID"))

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user} !")

intents = discord.Intents.default()
# intents.message_content = True
intents.members = True

# client = Client(intents=intents)
# client.run(token=token)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title=f"Chào mừng {member.name} đã tham gia vào lớp học của Teacher Minh",
            description=f"Nhớ đọc rule của nhóm {member.mention}",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Thành viên số {len(member.guild.members)}")

        await channel.send(embed=embed)

bot.run(token=token)
