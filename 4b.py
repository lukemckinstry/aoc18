

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

	track = {}
	for g in gset:
		track[g] = dict.fromkeys([i for i in range(60)], 0)
	
	sleep = False
	currentguard = None
	starttime = sortr[0]['d']
	for r in sortr:
		currtime = r['d']
		timedelta = (currtime - starttime).total_seconds() / 60
		if sleep == True:
			for m in range( starttime.minute, currtime.minute):
				track[currentguard][m] += 1
		if "begins" in r["t"]:
			currentguard = shiftre.findall( r['t'] )[0]
			sleep = False
		if 'asleep' in r['t']:
			sleep = True
		if "wakes" in r['t']:
			sleep = False
		starttime = currtime

	maxguard = None
	maxminindex = None
	maxminqty = 0

	freq = {}
	for g in track:
		print( "guard", g )
		for m in track[g]:
			if track[g][m] > maxminqty:
				maxminind = m
				maxguard = g
				maxminqty = track[g][m]

	print( maxguard , maxminind, maxminqty)
	print(  "answer ", int(maxguard.replace("#","")) * maxminind)
	
	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()