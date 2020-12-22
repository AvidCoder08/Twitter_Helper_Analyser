#importing libraries
import tweepy
from tweepy import OAuthHandler
import pandas as pd
from textblob import TextBlob

#Entering access key
consumer_key = 'DXoiLJMYL1hAA9muIuWRTHnP5'
consumer_key_secret = '3uGNg6yIVQda0BKfn2LZM2jrq9VqMClbbP3rX3VtukhoQJXh8U'
access_token = '1319866763283148805-zQlGdW2u8OG1uScITBn9HYeBzI4urE'
access_token_secret = "nQW0hxqK4HStv0M0V94YHZRxQbz3rv1NCYtOnIvUJzTp2"

#+ve, -ve, +-
pos = 0
neg = 0
neu = 0

#Granting Access
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

#Assigning API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweets = []
nega = []
#Searching tweets
searched_tweets = tweepy.Cursor(api.search, q = '@KTRTRS',lang = 'en', tweet_mode = 'extended').items(1000)
for tweet in searched_tweets:
	
  data = [tweet.created_at, tweet.id, tweet.full_text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
  
  neg_data = [tweet.full_text, tweet.entities['urls']]
  analysis = TextBlob(tweet.full_text)
  if analysis.sentiment[0]>0:
    pos += 1
  elif analysis.sentiment[0]<0:
    neg +=1
    data = tuple(data)
    nega.append(neg_data)

  else:
    neu = neu + 1
    data = tuple(data)
    tweets.append(data)
   

print("Total +ve: ", pos)
print("Total -ve: ", neg)
print("Total neu: ", neu)



ng = pd.DataFrame(nega, columns= ['tweet_text','urls'])
ng.to_csv(path_or_buf = 'tweet_result3.csv', index=False)