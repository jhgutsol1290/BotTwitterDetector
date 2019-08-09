import tweepy
import pandas as pd
from matplotlib import pyplot as plt
from twitter_client import TwitterAuthenticator
from twitter_bot_detector import TwitterBotDetector

consumer_key = 'wtFRuCKCv8uB4zchxPpj0IxF7'
consumer_secret = 'SUPHCNtK7QWe8fKpYwPt11CKQ9vWdGwawrrMaItEFIuuSAe9d1'
access_token = '2205718165-0nE4pGg3XxLVDQztEGdKmmiXfOkFBRPF4D7SDTm'
access_token_secret = 'n9HnBZgoH1gXUWEo8KGYepYkNHi9lyJNe3hnfEvmxxy67'

twitter_authenticator = TwitterAuthenticator(consumer_key, consumer_secret, access_token, access_token_secret)
api = twitter_authenticator.twitterClient()


if __name__ == "__main__":
    tweets = tweepy.Cursor(api.search, q='#chorizogate', lang = 'es', tweet_mode='extended').items(10)
    bot_detector = TwitterBotDetector()
    data_from_user = bot_detector.get_data_from_tweets(tweets)
    final_results = bot_detector.get_results(data_from_user)
    final_count = bot_detector.get_final_count()
    print('-'*80)
    print(data_from_user)
    print('-'*80)
    print(final_results)
    print('-'*80)
    print('Bots:', final_count[0])
    print('-'*80)
    print('Not know:', final_count[1])
    print('-'*80)
    print('Real Accounts:', final_count[2])
    names = ['Bots', 'Not Know', 'Real Accounts']
    values = final_count
    plt.figure(figsize=(12,3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.suptitle('Botmeter')
    plt.show()





    """ 
    consumer_key = 'wtFRuCKCv8uB4zchxPpj0IxF7'
consumer_secret = 'SUPHCNtK7QWe8fKpYwPt11CKQ9vWdGwawrrMaItEFIuuSAe9d1'
access_token = '2205718165-0nE4pGg3XxLVDQztEGdKmmiXfOkFBRPF4D7SDTm'
access_token_secret = 'n9HnBZgoH1gXUWEo8KGYepYkNHi9lyJNe3hnfEvmxxy67'

twitter_authenticator = TwitterAuthenticator(consumer_key, consumer_secret, access_token, access_token_secret)
api = twitter_authenticator.twitterClient()

tweets = tweepy.Cursor(api.search, q='amlo', lang = 'es', tweet_mode='extended').items(10)
data = []
array_scores = []
bots_scores = []
countBot = 0
countNotKnow = 0
countReal = 0
    
    
    for tweet in tweets:
    today = date(date.today().year, date.today().month, date.today().day)
    retweeted = 0
    info = tweet.user
    statuses = tweepy.Cursor(api.user_timeline, screen_name=info.screen_name, include_rts = True).items(100)
    d0 = info.created_at.date()
    delta = today - d0
    delta_res = delta.days
    for status in statuses:
        if 'RT' in status.text:
            retweeted += 1
    user_info = {
            "id": info.id,
            "screen_name": info.screen_name,
            "followers": info.followers_count,
            "following": info.friends_count,
            "statuses": info.statuses_count,
            "retweeted_count": retweeted,
            "favorites": info.favourites_count,
            "created": info.created_at.date(),
            "created_days": delta_res
        }
    data.append(user_info) """

# date_random = date(2018, 9, 11)
# print(today)
# dif = today - date_random
# print(dif.days)
# today = date(date.today().year, date.today().month, date.today().day)

""" for element in data:
    count_followers = 0
    count_following = 0
    count_retweets = 0
    count_date = 0
    count_total = 0
    
    if element['followers'] <= 20:
        count_followers += 5

    if element['following'] <= 20:
        count_following += 5
    
    if element['retweeted_count'] >= 20:
        count_retweets += 5
    
    if element['created_days'] <= 365:
        count_date += 5

    if element['followers'] > 20 and element['followers'] <= 100:
        count_followers += 3

    if element['following'] > 20 and element['following'] <= 100:
        count_following += 3
    
    if element['retweeted_count'] >= 10 and element['retweeted_count'] < 20:
        count_retweets += 3

    if element['created_days'] > 365 and element['created_days'] <= 720:
        count_date += 3

    if element['followers'] > 100:
        count_followers += 1

    if element['following'] > 100:
        count_following += 1

    if element['retweeted_count'] < 10:
        count_retweets += 1
    
    if element['created_days'] > 720:
        count_date += 1

    count_total = count_followers + count_following + count_retweets + count_date
    
    if count_total >= 12:
        array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Bot'})
        countBot += 1
    
    if count_total >= 6 and count_total < 12:
        array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Not Know'})
        countNotKnow += 1
    
    if count_total < 6:
        array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Real Account'})
        countReal += 1 """

    #array_scores.append({'score': count_total, 'account': element['screen_name']})


""" for score in array_scores:
    if score['score'] >= 12:
        bots_scores.append('Bot')
        countBot += 1
    
    if score['score'] >=6 and score['score'] < 12:
        bots_scores.append('Not know')
        countNotKnow += 1

    if score['score'] < 6:
        bots_scores.append('Real Account')
        countReal += 1 """


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
        