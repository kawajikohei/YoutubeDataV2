
from flask import Flask,render_template,url_for,request,session,redirect
from flask.views import MethodView
import random
import itertools
from channelcollect import ChannelProfile,VideoCollect,GetChannelid,GetYoutube

#print(channel.iloc[:,0])
#print(type(channel.columns[0]))#チャンネルのデータフレームDL用
#print(video)#チャンネルの中身だけ

app = Flask(__name__)#チャンネルのプロフィール情報を取得
app.jinja_env.globals.update(zip=zip)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_word = request.form['search_word']
        select_candidate = GetChannelid.idlist(search_word)
        return render_template('home.html', \
            title = 'Analyze Youtube Neighbors',
            message = "気になるyoutuberの名前やキーワードを入力してください",
            select_candidate = select_candidate

        )
    else:
        return render_template('home.html',\
            title = 'Analyze Youtube Neighbors',
            message = "気になるyoutuberの名前やキーワードを入力してください"
            )






@app.route('/test', methods=['GET'])
def index():
    channel_id = request.args.get('channel_id')
    channel = GetYoutube.procoll("AIzaSyBetlY9qwgHZM1hDS_zPng0FHb42unlw4Y",channel_id)
    video,urls = GetYoutube.vdcoll("AIzaSyBetlY9qwgHZM1hDS_zPng0FHb42unlw4Y",channel_id)
    return render_template('test.html', \
        title='Analyze Youtube Neighbors', \
        message = "気になるyoutuberの名前やキーワードを入力してください",
        channelcolumns = channel.columns.values.tolist(),
        channeldata = channel.loc[0],
        videocolumns = video.columns,
        videodata = video.values.tolist(),
        urls = urls
    )


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')

#if __name__ == '__main__':
    #app.debug = True
   # app.run(host='localhost')

