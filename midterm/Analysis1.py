import requests
import json
from heapq import heappush, heappop
import os

url = 'https://api.stackexchange.com/2.2/search/advanced?key=4IGfuFY8GypVylV4BUVCVQ((&page=999&pagesize=100&order=desc&sort=activity&tagged=python&site=stackoverflow'

results = requests.get(url).json()
questions = []
for stack in results['items']:
	if(stack['answer_count']!=0):
		questions.append(stack['question_id'])

user = []
heap = []

for id in questions:
	question_url = 'https://api.stackexchange.com/2.2/questions/'+ str(id) +'/answers?key=4IGfuFY8GypVylV4BUVCVQ((&order=desc&sort=activity&site=stackoverflow'
	answers = requests.get(question_url).json()
	for answer in answers['items']:
		user.append((answer['owner']['reputation'],answer['owner']));

for item in user:
	heappush(heap,item)
	
count = 0

while heap and (count<10):
	count += 1
	print("The No.%d popular user in the topic python is %s"%(count,heappop(heap)[1]['display_name']))

fn = os.path.join(os.path.dirname(__file__), "./python")
if not os.path.isdir(fn):
    os.makedirs(fn)

with open(fn+"/json_file.json", "w") as json_file:
    json_string = json.dumps(user)
    json_file.write(json_string)
	

