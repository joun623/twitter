import twitter


def authentification():
    # 取得したキーとアクセストークンを設定する
    auth = twitter.OAuth(consumer_key="hoge",
                     consumer_secret="fuga",
                     token="piyo,
                     token_secret="poyo")
    t = twitter.Twitter(auth=auth)
    return t


def tweet(tweets):
    t = authentification()
    t.statuses.update(status=tweets)

def timeline():
    t = authentification()
    timelines = t.statuses.home_timeline()
    for timeline in timelines:
        tl = '({id}) [{username}]:{text}'.format(
                id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
        print (tl)

tweet("本日は水曜日なり from python3 #ハッシュタグのテスト")
# timeline()
