import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar
import os
import tkinter as tk
import tkinter.filedialog
import pandas as pd
import json
import datetime
from datetime import timedelta

# 現在の日付時刻を表す文字列を返す
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


def daterange(start, end):
    for n in range((end - start).days + 1):
        yield start + timedelta(n)


def distribute_on_timeline(data):

    dates = list()
    for msg in data:
        dates.append(datetime.datetime.strptime(msg["date"], "%Y/%m/%d %H:%M:%S").date())
    minDate = min(dates)
    print(f"minDate = {minDate}")
    maxDate = max(dates)
    print(f"maxDate = {maxDate}")

    obj = dict()
    for date in daterange(minDate, maxDate):
        obj[date] = dict()

    print(obj)

    for msg in data:
        date = datetime.datetime.strptime(msg["date"], "%Y/%m/%d %H:%M:%S").date()
        author = msg["author"]
        if author in obj[date]:
            obj[date][author] += 1
        else:
            obj[date][author] = 1 
    
    # for msg in data:
    #     date = datetime.strptime(msg["date"]).date()
    #     member = msg["author"]
    #     if member in obj[date][member]:
    #         obj[date][member] += 1
    #     else:
    #         obj[date][member] = 1

    return obj

sns.set_theme(font="IPAexGothic")

root = tk.Tk()
root.withdraw()

fileType = [("", "*")]
currDir = os.path.abspath(os.path.dirname(__file__))
filePath = tkinter.filedialog.askopenfilename(filetype=fileType, initialdir=currDir)

with open(filePath, "r", encoding="utf-8") as f:
    data = json.load(f)

distributed_data = distribute_on_timeline(data)
df = pd.DataFrame.from_dict(data=distributed_data).T
print(df)

dayCount = calendar.monthrange(2025, 6)[1]
sns.displot(data=df, hue="author", bins=dayCount, kde=True)
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


