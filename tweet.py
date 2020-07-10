import time, tweepy

#definte the authentication keys
consumer_key = "y2U2miVxbe7GUuAIf7ZEUajj"
consumer_secret = "Q6tjkjYICh9ykAeDYtVrYKl58thvrBHPeJ52Jmt95ByazWltMl"
access_token = "1279133094897872896-rhdMQfqYdUOiBc58rYxlxYDefI3x6l"
access_token_secret = "sl0CudlP1KN8vCC6tvSiwKm5TVVDBdMWSG5jVAm65xnva"

#authorize ourselves
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []
username = 'MoCNASantaFe'
count = 20

try:
#Pull individual tweets from query
    for tweet in api.user_timeline(id=username, count = count):
        tweets.append((tweet.created_at, tweet.id,tweet.text))
except BaseException as e:
    print('failed on status', str(e))
    time.sleep(3)