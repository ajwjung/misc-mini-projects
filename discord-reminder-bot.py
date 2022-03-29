import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks

"""
A simple script that uses Discord.py to send a fun embedded message
to the designated Discord channel every 10 minutes to remind users
about their posture. The bot only stays live while the program is run.
"""


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# An object of client
client = discord.Client()


# Establish connection to Discord
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


# Create a task that loops and sends embed every 10 minutes
@tasks.loop(minutes=10)
async def posture_check():
    # Get channel ID
    channel = client.get_channel(int(CHANNEL_ID))

    # Create embedded message with image
    embed = discord.Embed(title="POSTURE CHECK! STOP SLOUCHING!",
                          description="How many times do I have to tell ya?",
                          color=discord.Colour.random())

    embed.set_image(url="https://imgur.com/RgnZQqf.png")

    # Send embed to channel
    await channel.send(embed=embed)


# Wait until bot is ready before loop starts
@posture_check.before_loop
async def posture_check_before_loop():
    await client.wait_until_ready()


posture_check.start()  # Start bot
client.run(TOKEN)  # Run client
