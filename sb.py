import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar
import os
import tkinter as tk
import tkinter.filedialog
import pandas as pd
import json

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

sns.set_theme(font="IPAexGothic")

root = tk.Tk()
root.withdraw()

fileType = [("", "*")]
currDir = os.path.abspath(os.path.dirname(__file__))
filePath = tkinter.filedialog.askopenfilename(filetype=fileType, initialdir=currDir)

with open(filePath, "r", encoding="utf-8") as f:
    data = json.load(f)

# for msg in data:
#     datetxt = msg["date"]
#     date = pd.to_datetime(datetxt)
#     msg["date"] = date.strftime("%d")


df = pd.DataFrame(data=data)
# df = df.sort_values("date")
pd.to_datetime(df["date"])
# df = pd.read_json(filePath)
# tips = sns.load_dataset(filePath)
# sns.relplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     col="time",
#     hue="smoker",
#     style="smoker",
#     size="size",
# )
dayCount = calendar.monthrange(2025, 6)[1]
sns.displot(data=df, x="date", hue="author", bins=dayCount, kde=True)
plt.savefig(get_now_datetime_txt() + ".png")
plt.show()
sns.countplot(data=df, x="date", hue="author")
plt.savefig(get_now_datetime_txt() + ".png")
plt.show()
sns.lineplot(data=df, x="date", hue="author")
plt.savefig(get_now_datetime_txt() + ".png")
plt.show()
# sns.pairplot(data=df, hue="author")
# plt.savefig(get_now_datetime_txt() + ".png")
# plt.show()


