import tweepy
import datetime
import csv

consumer_key="YOUR_CONSUMER_KEY"
consumer_secret="YOUR_CONSUMER_KEY_SECRET"

access_token="YOUR_ACCESS_TOKEN"
access_token_secret="YOUR_ACCESS_SECRET"

def search(hashtag):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)
  result = api.search(q=hashtag, rpp = 100)

  with open('tweets.csv', 'wb') as csvfile:
      spamwriter = csv.writer(csvfile)
      spamwriter.writerow(('Name','Time','Tweet'))
      for  tweet in result:
        content = tweet.text.encode('utf-8').strip()
        username = tweet.from_user
        time    = tweet.created_at
        spamwriter.writerow((username, time, content))

hashtag = input("what hash do you want to search?")

search(hashtag)
print 'success!'