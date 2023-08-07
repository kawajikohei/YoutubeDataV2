import datetime
#ISO8601フォーマット形式になっている文字型日付を年月日形式に変換する

#チャンネル情報用
def dateedit(date):
    try:
        s = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%fZ')
        d = s.strftime('%Y年%m月%d日%H時')
    except:
         s = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
         d = s.strftime('%Y年%m月%d日%H時')
    return d

