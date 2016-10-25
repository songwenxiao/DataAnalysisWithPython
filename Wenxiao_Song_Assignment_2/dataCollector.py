import requests
import json
from requests_oauthlib import OAuth1
import argparse
import os
from datetime import datetime
import pytz
import time

consumer_key = 'tMtgCOq6QSCugqdD4oEuwHjo8'
consumer_secret = 'Eqg4w6zTIEZo7aHTu1HIhUEnklbY65RPz8PJg8VufXeLuv4C97'
access_token = '745798776456085504-jbcozPkLbElFOF6T2WTV9RGYw5ZbsgA'
access_token_secret = 'u4nEROdSfLnDjbyNxTzOhaXcEcvy9AGSqpFBtLYCkL7yS'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('st', metavar='N', type=str, help='an integer for the accumulator')
args = parser.parse_args()

url = 'https://api.twitter.com/1.1/search/tweets.json?q='+args.st+'&count=100'

results = requests.get(url, auth=auth)
better_results = results.json()
tweets = {}
count = 1
for tweet in better_results['statuses']:
	tweets.update({count:tweet})
	count += 1




fn = os.path.join(os.path.dirname(__file__), "./tweets/"+args.st)
print(os.path.isdir(fn))
if not os.path.isdir(fn):
    os.makedirs(fn)

with open(fn+"/json_file.json", "w") as json_file:
    json_string = json.dumps(tweets)
    json_file.write(json_string)

