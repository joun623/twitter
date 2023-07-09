import twitter


def lambda_handler():
    # 取得したキーとアクセストークンを設定する
    auth = twitter.OAuth(consumer_key="hoge",
                     consumer_secret="fuga",
                     token="piyo",
                     token_secret="poyo")
    t = twitter.Twitter(auth=auth)

    t.statuses.update(status="python3からtwitterへの投稿テストです。")

lambda_handler()
