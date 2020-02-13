#!/usr/bin/python

import json

with open('KSCSPH073-dump.json') as f:
  data = json.load(f)
#print(data)
#print(data['KeyEvents'])
for event in data['KeyEvents']:
	#print(data['KeyEvents'][event]['slope'])
	try:
		for fff in data['KeyEvents'][event]['slope']:
			print(fff)
	except:
		print("\n")
