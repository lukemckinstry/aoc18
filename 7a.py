
import numpy as np
import re
file_name = "7a.txt"

#stepre = re.compile(r'tep \w')

stepre = re.compile(r'(?<=tep )\w')


def traverse(d):
	available = [i for i in d if len(d[i]) == 0]
	path = []
	
	while available:

		available = sorted(available, reverse=True)

		n = available.pop()
		path.append(n)

		for i in d:
			if n in d[i]:
				d[i].remove(n)
				if len(d[i]) == 0:
					print( "now available ", i )
					available.append(i)

		print(path, available)

	print( ''.join(path) )
	return 


def process(x):	

	rows = []
	for r in x:
		step = stepre.findall( r )
		rows.append(step)

	allnodes = [i[0] for i in rows] + [i[1] for i in rows]
	allnodesset = list(set([i for i in allnodes])) 

	d = {}
	for r in allnodesset:
		d[r] = []

	for r in rows:
		step = r[1]
		gate = r[0]
		if step not in d:
			d[step] = [gate]
		else:
			d[step].append(gate)

	traverse(d)

	
	return
		


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()
