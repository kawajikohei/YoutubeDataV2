
import os

# カレントディレクトリにある画像ファイル名を取得する
image_list = [
    f for f in os.listdir()
    if f.endswith((".jpg"))
]
image = image_list[0]
image2 = image_list[0]
# 画像ファイル名を表示する
image.show()
os.remove(image)


