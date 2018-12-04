

file_name = "4a.txt"

from datetime import datetime


import numpy as np
import re


def process(x):
	
	shiftre = re.compile(r'#\d+')

	records = []
	for r in x:
	 	r = r.split(']')
	 	d = datetime.strptime(r[0], '[%Y-%m-%d %H:%M')
	 	text = r[1].replace('\n', '')
	 	rd = {"d": d, "t": text}
	 	records.append( rd )
	sortr =  sorted(records, key=lambda student: student["d"])


	guards = []
	for r in sortr: 
		g = shiftre.findall( r['t'] )
		if len(g) == 1:
			guards.append( g[0] )
	gset = list(set(guards))
	totalsleep = {}
	for g in gset:
		totalsleep[g] = 0

	sleep = False
	currentguard = None
	starttime = sortr[0]['d']
	for r in sortr:
		currtime = r['d']
		timedelta = (currtime - starttime).total_seconds() /60
		if sleep == True:
			totalsleep[currentguard] += timedelta
		if "begins" in r["t"]:
			currentguard = shiftre.findall( r['t'] )[0]
			sleep = False
		if 'asleep' in r['t']:
			sleep = True
		if "wakes" in r['t']:
			sleep = False
		starttime = currtime
	print( totalsleep )

	maxs = max(totalsleep, key=totalsleep.get)

	print( "id of guard ", maxs )

	minutes = dict.fromkeys([i for i in range(60)], 0)

	sleep = False
	currentguard = None
	starttime = sortr[0]['d']
	for r in sortr:
		currtime = r['d']
		timedelta = (currtime - starttime).total_seconds() / 60
		if sleep == True and currentguard == maxs:
			for m in range( starttime.minute, currtime.minute):
				minutes[m] += 1
		if "begins" in r["t"]:
			currentguard = shiftre.findall( r['t'] )[0]
			sleep = False
		if 'asleep' in r['t']:
			sleep = True
		if "wakes" in r['t']:
			sleep = False
		starttime = currtime
	
	maxminute = max(minutes, key=minutes.get)
	print( "max minute ", maxminute )
	print(  "answer ", int(maxs.replace("#","")) * maxminute)

	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()