from google import google
import re
import time
import tweepy
import operator
import itertools

name_filename = '/Users/emz/Downloads/OpinRankDataset/hotels/all/hotel_names'

consumer_key='OSYEU1pjj5ZBAsW5TOuVu6cbT'
consumer_secret='Q7b3U9U6EZ815Gm7H4bXTtVgrEUuIgwJAVHvF2AhOpcEHZ1nFn'
access_token='31118185-1DJgoztOtd2r5sPMGNbEiO3QPpbx2Lq5anXnuHunX'
access_token_secret='YAjpD76tIt8NB8GjBkr9BbHuk8Y5qmYCpXSpplWUdMYmq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



f = open(name_filename, 'r')

i = 0

for hotel_filename in f:
    if not re.match("uk", hotel_filename):
        continue
    hotel_filename = hotel_filename.rstrip()
    # if i >= 10:
    #     break
    # i += 1
    words = hotel_filename.split('_')
    words.append("+site:twitter.com")
    r = api.search_users(words[1:],3)
    # print r
    ll = list(itertools.chain.from_iterable(map(lambda x: [str(x.id), x.screen_name], r)))
    print ','.join([hotel_filename] + ll)



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text