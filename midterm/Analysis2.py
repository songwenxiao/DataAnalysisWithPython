import os
import json
import requests
from heapq import heappush, heappop

users = []
for subdir, dirs, files in os.walk('python'):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".json"):
            myfile = open(filepath)
            data = json.load(myfile)
            users.append(data)


counts = []
heap = []
for i in range(len(users)):
	for user in users[i]:
		url = 'https://api.stackexchange.com/2.2/users/'+str(user[1]['user_id'])+'/badges?key=4IGfuFY8GypVylV4BUVCVQ((&pagesize=100&order=desc&sort=rank&site=stackoverflow'
		posts = requests.get(url).json()
		count = 0
		for post in posts['items']:
			if post['rank']=='bronze':
				count += 1
			elif post['rank']=='silver':
				count += 3
			else:
				count += 5
		counts.append((count,user[1]['display_name']))

num = 10

for item in counts:
	heappush(heap,item)

while heap and (num>0):
	print("The No.%d badges weightage poster in the top 10 python poster is %s"%(num,heappop(heap)[1]))
	num -= 1