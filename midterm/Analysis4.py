import requests
import numpy as np

url = 'https://api.stackexchange.com/2.2/questions?key=4IGfuFY8GypVylV4BUVCVQ((&pagesize=10&fromdate=1477094400&todate=1477699600&order=desc&sort=activity&site=stackoverflow'

results = requests.get(url).json()
questions_ids = []
answers = []
tags = []
for stack in results['items']:
	answers.append(stack['answer_count'])
	for tag in stack['tags']:
		if tag not in tags:
			tags.append(tag)

mean = np.mean(answers)
print('The average answers count for questions asked on 10/29/2016 is %f'%(mean))


tags_count = []
for tag_name in tags:
	tags_url = 'https://api.stackexchange.com/2.2/tags?key=4IGfuFY8GypVylV4BUVCVQ((&order=desc&sort=popular&inname='+ tag_name +'&site=stackoverflow'
	tag_res = requests.get(tags_url).json()
	if 'items' in tag_res:
		for st in tag_res['items']:
			if tag_name == st['name']:
				tags_count.append(st['count'])

for i in range(len(tags_count)):
	print('The tag \'%s\' has %d questions'%(tags[i],tags_count[i]))

