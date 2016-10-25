import os
import json
import numpy as np
import argparse
from heapq import heappush, heappop

def main():
	data = []
	for subdir, dirs, files in os.walk('tweets/trump'):
	    for file in files:
	        filepath = subdir + os.sep + file
	        if filepath.endswith(".json"):
	            myfile = open(filepath)
	            data1 = json.load(myfile)
	            data.append(data1)
	for subdir, dirs, files in os.walk('tweets/hillary'):
	    for file in files:
	        filepath = subdir + os.sep + file
	        if filepath.endswith(".json"):
	            myfile = open(filepath)
	            data2 = json.load(myfile)
	            data.append(data2)

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('st', metavar='N', type=str, help='an integer for the accumulator')
	args = parser.parse_args()
	if(args.st=='friend'):
		avg_friend(data)
	elif(args.st=='location'):
		location(data)
	elif(args.st=='retweet'):
		retweeted(data)
	elif(args.st=='influential'):
		influential(data)
	elif(args.st=='time'):
		time(data)
	


def avg_friend(data):
	tFriends = []
	hFriends = []
	for tweet in data[0]:
	    tFriends.append(data[0][tweet]['user']['friends_count'])

	for tweet in data[1]:
	    hFriends.append(data[1][tweet]['user']['friends_count'])

	tMean = np.mean(tFriends)
	print("The averge friend that Trump poster has is %f" %(tMean))
	hMean = np.mean(hFriends)
	print("The averge friend that Hillary poster has is %f" %(hMean))

def location(data):
	tState = []
	hState = []
	tLocations = []
	hLocations = []
	for tweet in data[0]:
	    tLocations.append(data[0][tweet]['user']['location'])

	for loc in tLocations:
		if(loc!=''):
			locs = loc.split(', ')
			if(len(locs)==2):
				if(len(locs[1])==2):
					tState.append(locs[1])

	for tweet in data[1]:
	    hLocations.append(data[1][tweet]['user']['location'])

	for loc in hLocations:
		if(loc!=''):
			locs = loc.split(', ')
			if(len(locs)==2):
				if(len(locs[1])==2):
					hState.append(locs[1])
	
	npTState = most_common (tState)
	npHState = most_common (hState)
	print("%s post Trump most."%(npTState))
	print("%s post Hillary most."%(npHState))

def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

def retweeted(data):
	heap = []
	tRetweet = []
	tTweet = []
	for tweet in data[0]:
	    tRetweet.append((data[0][tweet]['retweet_count'],data[0][tweet]['text']))
	for tweet in data[1]:
	    tRetweet.append((data[1][tweet]['retweet_count'],data[1][tweet]['text']))

	for item in tRetweet:
		heappush(heap,item)
	count = 0
	while heap and (count<10):
		print(heappop(heap)[1])
		count += 1

def influential(data):
	heap = []
	tRetweet = []
	tTweet = []
	for tweet in data[0]:
	    tRetweet.append((data[0][tweet]['retweet_count']*data[0][tweet]['user']['followers_count'],data[0][tweet]['text']))
	for tweet in data[1]:
	    tRetweet.append((data[1][tweet]['retweet_count']*data[0][tweet]['user']['followers_count'],data[1][tweet]['text']))

	for item in tRetweet:
		heappush(heap,item)
	count = 0
	while heap and (count<1):
		print("The most influential tweet among hillary and trump is %s"%(heappop(heap)[1]))
		count += 1

def time(data):
	days = []
	for tweet in data[0]:
	    days.append((data[0][tweet]['created_at']))
	m=0
	t=0
	w=0
	r=0
	f=0
	sat=0
	sun=0
	dic={}
	for i in range(len(days)):
		day = days[i][:3]
		if day in "Mon":
			m=m+1
		if day in "Tue":
			t=t+1
		if day in "Wed":
			w=w+1
		if day in "Thu":
			r=r+1
		if day in "Fri":
			f=f+1
		if day in "Sat":
			sat=sat+1
		if day in "Sun":
			sun=sun+1
	dic.update({"Mon":m})
	dic.update({"Tue":t})
	dic.update({"Wed":w})
	dic.update({"Thu":r})
	dic.update({"Fri":f})
	dic.update({"Sat":sat})
	dict = sorted(dic.items(), key = lambda d:d[1], reverse = True)
	a = dict[0]
	print ("Most people tweet on %s"%(dict[0][0]))



if __name__ == "__main__":
    main()
 