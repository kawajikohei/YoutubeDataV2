from googleapiclient.discovery import build

# APIキーを設定
api_key = 'YOUR_API_KEY'

# YouTube Data APIのビルド
youtube = build('youtube', 'v3', developerKey="AIzaSyBet8fhqadIOwf-DCH9od7N6Mlt4X9M92w")

# 検索リクエストの送信
request = youtube.search().list(
    part='snippet',
    q='検索キーワード',
    order='date',  # 古い順にソート
    type='video',
    maxResults=50  # 取得する動画の最大数
)

# レスポンスの取得
response = request.execute()

# 動画の情報を抽出し、古い順に並び替え
videos = response['items']
sorted_videos = sorted(videos, key=lambda x: x['snippet']['publishedAt'])

# 動画の情報を表示
for video in sorted_videos:
    title = video['snippet']['title']
    published_at = video['snippet']['publishedAt']
    print(f'Title: {title}\nPublished at: {published_at}\n')
