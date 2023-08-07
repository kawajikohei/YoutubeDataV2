import csv
import pandas as pd
import itertools
from channelcollect import Format
from apiclient.discovery import build
from 実験用 import Dateedit

def procoll(dkey,channel_id):
    DEVELOPER_KEY = dkey
    CHANNEL_ID = channel_id
    channel_info = []#チャンネル情報を入れる配列

    youtube =  build("youtube","v3",developerKey = DEVELOPER_KEY)

    #取得したrequestはdict型である
    request = youtube.channels().list(
        part = 'snippet,statistics',
        id = CHANNEL_ID
        ).execute()



    #requestで入手した情報の中からほしいデータをinfoとして取り出して配列channel_infoに入れる
    for info in request.get("items",[]):
      if info["kind"] != "youtube#video":
        channel_info.append([info["snippet"]["title"],#チャンネルタイトル
                            Format.commaformat(info["statistics"]["videoCount"]),#チャンネルのアップロード数
                            Format.commaformat(info["statistics"]["subscriberCount"]),#チャンネルの登録者数'{:,}'.format(number)
                            Format.commaformat(info["statistics"]["viewCount"]),#チャンネルの総再生数
                            Dateedit.dateedit(info["snippet"]["publishedAt"])])#チャンネルの作成日時

    #配列channel_infoのデータをデータフレーム化してcsvファイルとして出力する
    channel = pd.DataFrame(channel_info,columns = ["チャンネル名","動画投稿数","チャンネル登録者数","総再生数","チャンネル創設日時"])
    #chanellist = list(itertools.chain.from_iterable(channel.values.tolist()))
    return channel
    #channel.to_csv("channel.csv",index = False)
    #print(channel)