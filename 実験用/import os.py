import os
from PIL import Image
from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('in.html', \
        title="Index with Jinja", \
        message="これはJinjaテンプレートの利用例です。!",
        img = img())


def img():
    image_list = [
        f for f in os.listdir()
        if f.endswith((".jpg"))
    ]
    return os.path.abspath(image_list[0])
    # 画像ファイル名を削除する



if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
