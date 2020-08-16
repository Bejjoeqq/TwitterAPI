import tweepy

key = ""
secretKey = ""
token = ""
tokenSecret = ""

auth = tweepy.OAuthHandler(key,secretKey)
auth.set_access_token(token,tokenSecret)
api = tweepy.API(auth)

user = "jokowi"
lastTweet = 200
results = api.user_timeline(id=user,count=lastTweet,tweet_mode='extended')
y=0
for x in results:
	print(x.full_text)
	if "covid" in x.full_text.lower():
		y+=1
print(f"Banyak tweet pak jokowi yang diambil : {lastTweet}")
print(f"Banyak tweet pak jokowi tentang covid : {y}")
print(api.rate_limit_status()['resources']['statuses']['/statuses/home_timeline'])
print(api.rate_limit_status()['resources'])