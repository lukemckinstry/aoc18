
import numpy as np
file_name = "6a.txt"

def within10000(r,c,coords  ):
	d = 0
	for pair in coords:
		xdist = abs(pair[0] - c)
		ydist = abs(pair[1] - r)
		d += xdist
		d += ydist
	print(r,c, " dist ", d)
	if d < 10000:
		return True
	else:
		return False

def process(x):	

	coords = []
	for c in x:
		c = c.replace('\n','')
		c = c.split(',')
		x,y = int(c[0]), int(c[1].replace(' ',''))
		coords.append( [x,y] )
		pass
	minx = min([i[0] for i in coords])
	miny = min([i[1] for i in coords])
	maxx = max([i[0] for i in coords])
	maxy = max([i[1] for i in coords])
	base_arr = np.zeros(( maxy, maxx ))
	
	for r in range(maxy):
		for c in range(maxx):
			within = within10000(r,c,coords)
			if within:
				base_arr.itemset((r,c), 1)
	
	area = np.count_nonzero(base_arr == 1 )
	print("max finite area ", area)

	return
		


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()