import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# サンプルデータの作成
data = {'カテゴリ': ['A', 'B', 'A', 'B', 'A'],
        '値': [10, 15, 20, 12, 18],
        '種類': ['X', 'X', 'Y', 'Y', 'Y']}
df = pd.DataFrame(data)

# hue別に横に並べつつ縦に積上げる棒グラフを作成
sns.barplot(data=df, x='カテゴリ', y='値', hue='種類', dodge=False) # dodge=False で積み上げ
