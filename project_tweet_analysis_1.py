#importing libraries
import tweepy
from tweepy import OAuthHandler
import pandas as pd
from textblob import TextBlob
from monkeylearn import MonkeyLearn

#Entering access key
api_key = 'DXoiLJMYL1hAA9muIuWRTHnP5'
api_key_secret = '3uGNg6yIVQda0BKfn2LZM2jrq9VqMClbbP3rX3VtukhoQJXh8U'
access_token = '1319866763283148805-zQlGdW2u8OG1uScITBn9HYeBzI4urE'
access_token_secret = "nQW0hxqK4HStv0M0V94YHZRxQbz3rv1NCYtOnIvUJzTp2"
ml = MonkeyLearn('b8703f11e18877421899419bf79eca85af5fece6')
model_id = 'cl_aMQ5BQZA'

#+ve, -ve, +-
pos = 0
neg = 0
neu = 0
x = []

#Granting Access
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

#Assigning API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweets = []
nega = []

#Searching tweets
searched_tweets = tweepy.Cursor(api.search, q = '@KTRTRS',lang = 'en', tweet_mode = 'extended', result_type = 'recent').items(10)
for tweet in searched_tweets:
  classifier = [tweet.full_text]
  list_1 = [tweet.id_str, tweet.user._json['screen_name']]
  neg_data = [tweet.full_text, 'https://www.twitter.com/'+tweet.user._json['screen_name']+'/status/'+tweet.id_str+'/']
  
  analysis = TextBlob(tweet.full_text)
  if analysis.sentiment[0]>0:
    pos += 1
  elif analysis.sentiment[0]<0:
    neg +=1
    nega.append(neg_data)
  else:
    neu = neu + 1
  
  

print("Total +ve: ", pos)
print("Total -ve: ", neg)
print("Total neu: ", neu)



ng = pd.DataFrame(nega, columns= ['tweet_text', 'urls'])
ng.to_excel('result1.xlsx', index=False)