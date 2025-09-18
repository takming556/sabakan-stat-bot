import discord
from discord import app_commands
import logging
import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

RANGE_YEAR = app_commands.Range[int, 2000, 2100]
RANGE_MONTH = app_commands.Range[int, 1, 12]


@client.event
async def on_ready():
    print(f"{client.user}としてログインしました")
    await tree.sync()


@tree.command(name="monthly", description="月次レポートを作成します。")
@app_commands.describe(year="対象年", month="対象月")
async def generate_monthly_report(interaction:discord.Interaction, year:RANGE_YEAR, month:RANGE_MONTH):
    guild = interaction.guild
    channels = guild.text_channels
    after = datetime.datetime(year, month, 1)
    before = datetime.datetime(year, month + 1, 1)
    embed = discord.Embed(title="あ！", description=f"{year}年 {month}月")
    await interaction.response.send_message(embed=embed)

    obj = list()
    # date = list()
    # member = list()
    # channel = list()
    # content = list()

    for chl in channels:
        async for message in chl.history(before=before, after=after):
            msg = dict()
            if not message.author.bot:
                msg["date"] = message.created_at.strftime("%Y/%m/%d %H:%M:%S")
                msg["author"] = message.author.name
                msg["channel"] = message.channel.name
                msg["content"] = message.content
                obj.append(msg)

            # date.append(message.created_at.strftime("%Y/%m/%d %H:%M:%S"))
            # member.append(message.author.name)
            # channel.append(message.channel.name)
            # content.append(message.content)
    
    # obj["date"] = date
    # obj["member"] = member
    
    dump(obj)
    # sns.lineplot(data=obj)
    # plt.savefig(get_now_datetime_txt() + ".png")
    # plt.show()


def dump(obj):
    filename = get_now_datetime_txt()
    with open(f'./output/{filename}.json', 'w') as f:
        json.dump(obj, f, indent=2)


def get_now_datetime_txt():
    now = datetime.datetime.now()
    year = str(now.year).zfill(4)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    datetime_txt = year + '-' + month + '-' + day + ' ' + hour + '-' + minute + '-' + second
    return datetime_txt



handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
client.run("bot token here", log_handler=handler)


# msg.clear()
# msg.append(message.created_at.strftime("%Y/%m/%d %H:%M:%S"))
# msg.append(message.author.name)
# msg.append(message.channel.name)
# msg.append(message.content)
# obj.append(msg)