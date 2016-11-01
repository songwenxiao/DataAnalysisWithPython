import requests
from heapq import heappush, heappop

url = 'https://api.stackexchange.com/2.2/search?key=4IGfuFY8GypVylV4BUVCVQ((&pagesize=100&fromdate=1477699200&order=desc&sort=activity&tagged=python&site=stackoverflow'
results = requests.get(url).json()
owner_ids = []
for stack in results['items']:
	owner_ids.append(stack['owner']['user_id'])

badges_id = []

count = 0
for owner_id in owner_ids:
	owner_url = 'https://api.stackexchange.com/2.2/users/'+ str(owner_id) +'/badges?key=4IGfuFY8GypVylV4BUVCVQ((&pagesize=100&order=desc&sort=rank&site=stackoverflow'
	badges = requests.get(owner_url).json()
	if(len(badges['items'])):
		count += 1
	for stack in badges['items']:
		if stack['badge_id'] not in badges_id:
			badges_id.append(stack['badge_id'])

badges_res = []
heap = []

for badge_id in badges_id:
	badge_url = 'https://api.stackexchange.com/2.2/badges/'+ str(badge_id) +'?key=4IGfuFY8GypVylV4BUVCVQ((&fromdate=1477353600&order=desc&sort=rank&site=stackoverflow'
	badges = requests.get(badge_url).json()
	for bad in badges['items']:
		badges_res.append((bad['award_count'],bad['name']))

for item in badges_res:
	heappush(heap,item)

num = 11

print('Among 100 user in the stackoverflow who posts questions about python, %d users have badges' %(count))

while heap and (num>1):
	num -= 1
	pop = heappop(heap)
	print("The No.%d popular badge among users in topic python is %s, the total award count for this badge is %d"%(num,pop[1],pop[0]))

