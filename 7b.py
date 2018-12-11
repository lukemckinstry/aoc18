
import numpy as np
import re
file_name = "7a.txt"

stepre = re.compile(r'(?<=tep )\w')


def traverse(d):
	worker = []
	available = [i for i in d if len(d[i]['g']) == 0]
	pathcomplete = []
	time = 0

	while available or worker: 
		time += 1
		
		available = sorted(available, reverse=True)
		while (len(available) > 0) and len(worker) <= 5 :
			n = available.pop()
			print("starting ", n, time)
			worker.append( n )

		completedworkers = [] 
		for w in worker:
			d[w]['to_complete'] = d[w]['to_complete'] - 1
			if d[w]['to_complete'] == 0:
				completedworkers.append(w)				
				pathcomplete.append(w)		
		
		for w in completedworkers:
			worker.remove(w)		
			for i in d:
				if w in d[i]['g']:
					d[i]['g'].remove(w)
					if len(d[i]['g']) == 0:
						available.append(i)
		
	print( "final time",  time )
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
		d[r] = {'g': [], 'to_complete': 60 + ord(r) - 64 }

	for r in rows:
		step = r[1]
		gate = r[0]
		if step not in d:
			d[step]['g'] = [gate]
		else:
			d[step]['g'].append(gate)

	traverse(d)
	
	return
		


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()
