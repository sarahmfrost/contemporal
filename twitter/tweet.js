import tweepy;

consumer_key = "y2U2miVxbe7GUuAIf7ZEUajj";
consumer_secret = "Q6tjkjYICh9ykAeDYtVrYKl58thvrBHPeJ52Jmt95ByazWltMl";
access_token = "1279133094897872896-rhdMQfqYdUOiBc58rYxlxYDefI3x6l";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(access_token, access_token_secret);
api = tweepy.API(auth, wait_on_rate_limit=True);
