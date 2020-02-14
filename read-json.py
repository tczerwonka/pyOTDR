#!/usr/bin/python
#{u'slope': u'0.000', u'distance': u'0.000', u'end of prev': u'87590.792', u'start of next': u'0.066', u'type': u'1F9999LS {auto} reflection', u'end of curr': u'0.036', u'comments': u' ', u'refl loss': u'-57.525', u'peak': u'0.013', u'start of curr': u'0.000', u'splice loss': u'0.064'}

import json

with open('KSCSPH073-dump.json') as f:
  data = json.load(f)

print("distance, refl_loss")
for event in data['KeyEvents']:
	try:
		print(data['KeyEvents'][event]['distance'] + "," + data['KeyEvents'][event]['refl loss'])
	except:
		print("")
