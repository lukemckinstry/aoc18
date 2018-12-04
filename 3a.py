

file_name = "3a.txt"

import numpy as np


def process(x):
	d = 0
	t = 0
	shapes = []
	for r in x:
		r = r.replace(':','').replace('\n','').split(' ')
		claimid = r[0]
		l = int(r[2].split(',')[0])
		t = int(r[2].split(',')[1])
		w = int(r[3].split('x')[0])
		h = int(r[3].split('x')[1])
		shapes.append( [claimid, l,t,w,h] )

	totalw = max([i[0] + i[2] for i in shapes ])
	totalh = max([i[1] + i[3] for i in shapes ])
	print( totalw, totalh )
	base_arr = np.zeros(( totalh, totalw ))
	

	for s in shapes:
		claimid, l,t,w,h = s
		for r in range(t,t+h ):
			for c in range(l, l+w):
				item = base_arr.item((r,c))
				base_arr.itemset((r,c), item + 1)
	
	count = np.count_nonzero(base_arr > 1 )
	print( "count ", count )

	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    #find_double(x)
	    print(len(x))
	    process(x)

main()