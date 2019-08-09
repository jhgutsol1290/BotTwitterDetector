import tweepy
from datetime import date, datetime, timedelta
from twitter_client import TwitterAuthenticator

consumer_key = 'wtFRuCKCv8uB4zchxPpj0IxF7'
consumer_secret = 'SUPHCNtK7QWe8fKpYwPt11CKQ9vWdGwawrrMaItEFIuuSAe9d1'
access_token = '2205718165-0nE4pGg3XxLVDQztEGdKmmiXfOkFBRPF4D7SDTm'
access_token_secret = 'n9HnBZgoH1gXUWEo8KGYepYkNHi9lyJNe3hnfEvmxxy67'

twitter_authenticator = TwitterAuthenticator(consumer_key, consumer_secret, access_token, access_token_secret)
api = twitter_authenticator.twitterClient()

class TwitterBotDetector():
    def __init__(self, data=[], array_scores=[], countBot=0, countNotKnow=0, countReal=0):
        self.data = data
        self.array_scores = array_scores
        self.countBot = countBot
        self.countNotKnow = countNotKnow
        self.countReal = countReal
    
    def get_data_from_tweets(self, tweets):
        for tweet in tweets:
            today = date(date.today().year, date.today().month, date.today().day)
            retweeted = 0
            info = tweet.user
            statuses = tweepy.Cursor(api.user_timeline, screen_name=info.screen_name, include_rts = True).items(50)
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
            self.data.append(user_info)
        return self.data
    
    def get_results(self, data_from_user):
        for element in data_from_user:
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
                self.array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Bot'})
                self.countBot += 1
            
            if count_total >= 6 and count_total < 12:
                self.array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Not Know'})
                self.countNotKnow += 1
            
            if count_total < 6:
                self.array_scores.append({'score': count_total, 'account': element['screen_name'], 'status': 'Real Account'})
                self.countReal += 1
        
        return self.array_scores

    def get_final_count(self):
        return [self.countBot, self.countNotKnow, self.countReal]