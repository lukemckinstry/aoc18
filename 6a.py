
import numpy as np
file_name = "6a.txt"

def closecoord(r,c,coords  ):
	closest = []
	mindist = 10000
	for pair in coords:

		xdist = abs(pair[0] - c)
		ydist = abs(pair[1] - r)
		dist = xdist + ydist
		
		if dist == mindist:
			mindist = dist
			closest.append(pair)
		if dist < mindist:
			mindist = dist
			closest = [pair]
	#print( pair, " is closest to ", c,",", r, " and dist = ", mindist)
	#print( "index ", coords.index(pair) )
	if len(closest) > 1:
		return 99
	else:
		return coords.index(closest[0])

#ord Z is 90
def process(x):	

	coords = []
	for c in x:
		c = c.replace('\n','')
		c = c.split(',')
		x,y = int(c[0]), int(c[1].replace(' ',''))
		coords.append( [x,y] )
		print(x,y)
		pass
	minx = min([i[0] for i in coords])
	miny = min([i[1] for i in coords])
	maxx = max([i[0] for i in coords])
	maxy = max([i[1] for i in coords])
	print("x ", minx, maxx, "y ", miny, maxy)
	base_arr = np.zeros(( maxy-miny, maxx-minx ))
	
	for r in range(maxy-miny):
	#for r in range(2):
		for c in range(maxx-minx):
		#for c in range(2):
			closest = closecoord(r,c,coords)
			#print( c,",", r, " --> ", closest, " is closest ")
			base_arr.itemset((r,c), closest)
	

	top = list(base_arr[0])
	bot = list(base_arr[-1])
	left = list([r[0] for r in base_arr])
	right = list([r[-1] for r in base_arr])
	borders = top + bot + left + right
	#borders = top.append(bot).append(left).append(right) 
	#print( len(borders) )
	maxarea = 0
	for i in range(len(coords)):
		if i not in borders:
			count = np.count_nonzero(base_arr == i )
			if count > maxarea:
				maxarea = count
	print("max finite area ", maxarea)




	return
		


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()