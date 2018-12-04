

file_name = "3a.txt"

import numpy as np


def process(x):
	d = 0
	t = 0
	shapes = []
	for r in x:
		r = r.replace(':','').replace('\n','').split(' ')
		
		l = int(r[2].split(',')[0])
		t = int(r[2].split(',')[1])
		w = int(r[3].split('x')[0])
		h = int(r[3].split('x')[1])
		claimid = int(r[0].replace('#',''))
		area = w * h
		shapes.append( [l,t,w,h,area,claimid] )

	#print(shapes)
	totalw = max([i[0] + i[2] for i in shapes ])
	totalh = max([i[1] + i[3] for i in shapes ])
	print( totalw, totalh )
	base_arr = np.zeros(( totalh, totalw ))

	for s in shapes:
		l,t,w,h,area,claimid = s
		for r in range(t,t+h ):
			for c in range(l, l+w):

				if base_arr.item((r,c)) != 0:
					base_arr.itemset((r,c), -1)
				else: 
					base_arr.itemset((r,c), claimid)

	for s in shapes:
		l,t,w,h, area,claimid  = s


		if np.count_nonzero(base_arr == claimid ) == area:
			print( "found it!! ", claimid )
			return
	print( "count ", count )

	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()