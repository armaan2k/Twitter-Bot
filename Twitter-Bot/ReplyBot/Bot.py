import tweepy
import time
import os
from ReplyBot.chat import twitter_reply

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
    #status represents the users tweets. the loop goes through their most recent tweet/retweet
    for status in tweepy.Cursor(api.user_timeline, screen_name=('@'+friend.screen_name), tweet_mode="extended").items(1):
        try:
            print(friend.screen_name)
            print(status.full_text)
            status.favorite()
            sn = friend.screen_name
            m = twitter_reply(status.full_text)
            u = "@%s %s" % (sn,m)
            print(u)
            print()
            api.update_status(u, status.id_str)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# api.update_status("i just walked outside and saw a dog taking a poop")
#
# # api.update_status('I love OTV, haha :)')
# for status in tweepy.Cursor(api.user_timeline, screen_name=('@NaamraTnahcrem'), tweet_mode="extended").items(1):
#     api.update_status(twitter_reply(status.full_text), status.id_str)
#     print(status.full_text)
#     print(status.user.screen_name)



#api.update_status("my update", in_reply_to_status_id = tweetid)








