# 必要なライブラリのインストール

# 必要なモジュールのインポート
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# APIキーの設定
API_KEY = 'AIzaSyBetlY9qwgHZM1hDS_zPng0FHb42unlw4Y'

# YouTube Data APIのビルド
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 動画IDの設定
video_id = 'oGu6gZtAME'
# 動画情報の取得
try:
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    # 動画情報の取得
    video_info = video_response.get("items")
    
    # 必要な情報の抽
    print(video_response)

except HttpError as error:
    print(f'An error occurred: {error}')


https://www.googleapis.com/youtube/v3/videos?id=oGu6gZtAME&key=AIzaSyBetlY9qwgHZM1hDS_zPng0FHb42unlw4Y&part=statistics