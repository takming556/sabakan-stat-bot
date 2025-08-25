import discord
import logging
import datetime
import json

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

obj = list()
msg = list()

@client.event
async def on_ready():
    print(f'{client.user}としてログインしました')
    
    now = datetime.datetime.now()
    year = str(now.year).zfill(4)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    filename = year + '-' + month + '-' + day + ' ' + hour + '-' + minute + '-' + second
    
    guild = client.get_guild('guild id here')
    channels = guild.text_channels
    before = datetime.datetime(2025, 8, 1)
    after = datetime.datetime(2025, 7, 1)

    for channel in channels:
        async for message in channel.history(before=before, after=after):
            msg.clear()
            msg.append(message.guild.name)
            msg.append(message.channel.name)
            msg.append(message.author.name)
            msg.append(message.created_at.strftime('%Y/%m/%d %H:%M:%S'))
            msg.append(message.content)
            print(msg)
        obj.append(msg)
    
    with open(f'./output/{filename}.json', 'w') as f:
        json.dump(obj, f, indent=2)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run('bot token here', log_handler=handler)