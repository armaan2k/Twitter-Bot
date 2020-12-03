import tweepy
import time
import os

api_key = os.environ.get('TWITTER_API_KEY')
api_secret_key = os.environ.get('TWITTER_API_SECRET_KEY')
api_token = os.environ.get('TWITTER_API_TOKEN')
api_token_secret = os.environ.get('TWITTER_API_TOKEN_SECRET')

auth = tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(api_token,api_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user.screen_name)

#iterates through all the people I follow as the variable friend
for friend in tweepy.Cursor(api.friends, screen_name="NaamraTnahcrem").items():
    print('friend: ' + friend.screen_name)
    #status represents the users tweets. the loop goes through their 2 most recent tweets/retweets
    for status in tweepy.Cursor(api.user_timeline, screen_name=('@'+friend.screen_name), tweet_mode="extended").items(2):
        try:
            print(status.full_text)
            status.favorite()
            #api.update_status('this is going to be my bot reply', status.id_str)  #use this to reply to a tweet
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# api.update_status('I love OTV, haha :)')
for status in tweepy.Cursor(api.user_timeline, screen_name=('@Disguised Toast'), tweet_mode="extended").items(1):
    api.update_status('I love this', status.id_str)
    print(status.full_text)
    print(status.user.screen_name)



#api.update_status("my update", in_reply_to_status_id = tweetid)








