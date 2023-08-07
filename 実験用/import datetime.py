import re

def format_duration(duration):
    # 時間、分、秒の値を抽出する正規表現パターン
    pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'

    # 正規表現パターンに一致するグループを取得
    match = re.match(pattern, duration)

    # 時間、分、秒の値を取得
    hours = match.group(1)
    minutes = match.group(2)
    seconds = match.group(3)

    # 分に変換
    total_minutes = 0
    if hours:
        total_minutes += int(hours) * 60
    if minutes:
        total_minutes += int(minutes)
    if seconds:
        total_minutes += round(int(seconds) / 60)

    # フォーマットされた文字列を生成
    formatted_duration = str(total_minutes) + "分"

    return formatted_duration

# テスト用データ
data = [['PT37M25S'], ['PT1H47M58S'], ['PT59M45S'], ['PT1H30M40S'], ['PT43M36S'], ['PT38M14S'], ['PT34M34S'], ['PT1H9M14S'], ['PT41M46S'], ['PT43M25S'], ['PT54S'], ['PT48M38S'], ['PT1H23M30S'], ['PT40M42S'], ['PT1H30M31S'], ['PT25M48S'], ['PT34M5S'], ['PT1H9M16S'], ['PT36M42S'], ['PT1H30M52S'], ['PT58M23S'], ['PT57M15S'], ['PT52M22S'], ['PT34M33S'], ['PT49S'], ['PT47M31S'], ['PT1H20M35S'], ['PT27M39S'], ['PT27S'], ['PT50M28S'], ['PT52M17S'], ['PT1H28M43S'], ['PT33M46S'], ['PT15M29S'], ['PT34M13S'], ['PT46M17S'], ['PT49M1S']]
# フォーマットされたデータを格納するリスト
formatted_data = []

# 各データをフォーマット
for item in data:
    duration = item[0]
    formatted_duration = format_duration(duration)
    formatted_data.append(formatted_duration)

# 結果を出力
print(formatted_data)
