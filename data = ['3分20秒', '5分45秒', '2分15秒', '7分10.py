import matplotlib.pyplot as plt
from datetime import timedelta
from collections import Counter

data = ['6分10秒', '4分40秒', '5分5秒','4分5秒','5分5秒']

# データを秒単位に変換する関数
def convert_to_seconds(time):
    time_components = time.split('分')
    minutes = int(time_components[0])
    seconds = int(time_components[1].replace('秒', ''))
    return minutes * 60 + seconds

# データを秒単位に変換してリストに格納
seconds_data = [convert_to_seconds(time) for time in data]

# 5分間隔でデータをグループ化
grouped_data = Counter([(sec // 300) * 300 for sec in seconds_data])

# グラフの設定
labels = [f"{i}分-{i+5}分" for i in range(0, max(grouped_data) + 1, 300)]
plt.bar(range(len(grouped_data)), grouped_data.values())
plt.xlabel('長さ（5分間隔）')
plt.ylabel('動画数')
plt.title('最近の投稿された動画の長さ')

# X軸の目盛りとラベルの設定
plt.xticks(range(len(grouped_data)), labels, rotation='vertical')

# グラフを表示
plt.show()
