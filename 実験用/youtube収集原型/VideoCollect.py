import csv
import pandas as pd
import datetime
from channelcollect import Format
from apiclient.discovery import build
from 実験用 import Dateedit
#from google.colab import drive
#drive.mount('/content/drive')

def vdcoll(dkey,channel_id):
    DEVELOPER_KEY = dkey
    CHANNEL_ID = channel_id
    search_info = []#動画のIDを入れる配列
    videos = []
    urls = []
    nextPagetoken = None
    nextpagetoken = None

    youtube =  build("youtube","v3",developerKey = DEVELOPER_KEY)

    while True:
      if nextPagetoken != None:
        nextpagetoken = nextPagetoken
      search_request =  youtube.search().list(
          part="snippet",
          channelId = CHANNEL_ID,
          maxResults = 50,
          order = "date",
          pageToken = nextpagetoken

      ).execute()

      for search_result in search_request.get("items", []):
          if search_result["id"]["kind"] == "youtube#video":
            search_info.append(search_result["id"]["videoId"])
            urls.append(f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}')


      for info in search_info:
        video_info = youtube.videos().list(
            part = "snippet,statistics",
            id = info
        ).execute()
        for video_search in video_info.get("items",[]):
          if video_search["kind"] == "youtube#video":
            try:
               videos.append([
                        video_search["snippet"]["thumbnails"]["medium"]["url"],
                        video_search["snippet"]["title"],#動画タイトル
                        video_search["statistics"]["viewCount"],#動画の再生数
                        video_search["statistics"]["likeCount"],#動画の高評価数
                        Dateedit.dateedit(video_search["snippet"]["publishedAt"])#投稿日時
                        ])
            except:
                videos.append([
                        video_search["snippet"]["thumbnails"]["medium"]["url"],
                        video_search["snippet"]["title"],#動画タイトル
                        video_search["statistics"]["viewCount"],#動画の再生数
                        0,#動画の高評価数
                        Dateedit.dateedit(video_search["snippet"]["publishedAt"])#投稿日時
                        ])
              
              
      try:
        nextPagetoken = search_request["nextPageToken"]
      except:
        break


    #print(videos)
    video = pd.DataFrame(videos,columns = ["サムネイル","タイトル","再生数","高評価数","投稿時間"])
    return video,urls
    #video.to_csv("videos.csv",index = False)
