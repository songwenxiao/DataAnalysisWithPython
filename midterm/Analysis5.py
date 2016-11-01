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

questions = []
heap = []

for i in range(len(users)):
	for user in users[i]:
		url = 'https://api.stackexchange.com/2.2/users/'+ str(user[1]['user_id']) +'/favorites?key=4IGfuFY8GypVylV4BUVCVQ((&order=desc&sort=activity&site=stackoverflow'
		result = requests.get(url).json()
		for res in result['items']:
			questions.append((res['score'],res['title']))

for item in questions:
	heappush(heap,item)

num = 10
while heap and (num>0):
	print("The No.%d favorite questions in the top 10 python poster is: %s "%(num,heappop(heap)[1]))
	num -= 1