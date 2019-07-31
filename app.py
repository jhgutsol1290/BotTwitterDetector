from twitter_client import TwitterAuthenticator
import tweepy
from datetime import date, datetime, timedelta

consumer_key = 'wtFRuCKCv8uB4zchxPpj0IxF7'
consumer_secret = 'SUPHCNtK7QWe8fKpYwPt11CKQ9vWdGwawrrMaItEFIuuSAe9d1'
access_token = '2205718165-0nE4pGg3XxLVDQztEGdKmmiXfOkFBRPF4D7SDTm'
access_token_secret = 'n9HnBZgoH1gXUWEo8KGYepYkNHi9lyJNe3hnfEvmxxy67'

twitter_authenticator = TwitterAuthenticator(consumer_key, consumer_secret, access_token, access_token_secret)
api = twitter_authenticator.twitterClient()

tweets = tweepy.Cursor(api.search, q='amlo', lang = 'es', tweet_mode='extended').items(10)
data = []
array_scores = []

for tweet in tweets:
    retweeted = 0
    info = tweet.user
    statuses = tweepy.Cursor(api.user_timeline, screen_name=info.screen_name, include_rts = True).items(100)
    for status in statuses:
        if 'RT' in status.text:
            retweeted += 1
        else:
            pass
    user_info = {
            "id": info.id,
            "sceen_name": info.screen_name,
            "followers": info.followers_count,
            "following": info.friends_count,
            "statuses": info.statuses_count,
            "retweeted_count": retweeted,
            "favorites": info.favourites_count,
            "created": info.created_at
        }
    data.append(user_info)

print(data)
# today = date(date.today().year, date.today().month, date.today().day)
# date_random = date(2018, 9, 11)
# print(today)
# dif = today - date_random
# print(dif.days)
# today = date(date.today().year, date.today().month, date.today().day)

for element in data:
    count_followers = 0
    count_following = 0
    count_retweets = 0
    count_total = 0
    
    if element['followers'] <= 20:
        count_followers += 5

    if element['following'] <= 20:
        count_following += 5
    
    if element['retweeted_count'] >= 20:
        count_retweets += 5

    if element['followers'] > 20 and element['followers'] <= 100:
        count_followers += 3

    if element['following'] > 20 and element['following'] <= 100:
        count_following += 3
    
    if element['retweeted_count'] >= 10 and element['retweeted_count'] < 20:
        count_retweets += 3

    if element['followers'] > 100:
        count_followers += 1

    if element['following'] > 100:
        count_following += 1

    if element['retweeted_count'] < 10:
        count_retweets += 1

    count_total = count_followers + count_following + count_retweets
    array_scores.append(count_total)

print(array_scores) 





#statuses = api.user_timeline(screen_name = '@lapinacb', count=10)
#statuses = tweepy.Cursor(api.user_timeline, screen_name='lapinacb', include_rts = True).items(10)
#user = api.get_user('lapinacb')
""" tweets = tweepy.Cursor(api.user_timeline, screen_name='lapinacb', include_rts = True).items(100)

retweets = 0
for tweet in tweets:
    if 'RT' in tweet.text:
        print('In reply')
        print(tweet.id)
        retweets += 1
    else:
        pass
print('-'*30)
print(retweets) """
        