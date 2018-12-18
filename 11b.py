

file_name = "10a.txt"

import numpy as np
np.set_printoptions(threshold=np.nan)
import re


def calc(x,y):
	serial = 3628
	rackid = x + 10
	pl = rackid * y
	pl = (pl + serial) * rackid
	if len(str(pl)) < 3:
		return -5
	else:
		return int(str(pl)[len(str(pl))-3]) - 5

def box(base_arr, x,y,s):
	y = y-1
	x = x-1
	sli = base_arr[y:y+s, x:x+s]
	return sli.sum()


def preprocess():
	maxval = 0
	maxcoords = 0,0
	maxsize = 0

	base_arr = np.zeros(( 300, 300 ))

	for x in range(1,301):
		for y in range(1,301):
			base_arr.itemset((y-1,x-1), calc(x,y))
	
	for x in range(1,301):
		print(x)
		for y in range(1,301):
			xymax = max(x,y)
			for s in range(xymax,300):
				s = s - xymax
				val = box(base_arr,x,y,s)

				if val > maxval:
					maxval = val
					maxcoords = x,y
					maxsize = s
	print('maxcoords ', maxcoords)
	print('maxsize ', maxsize)
	print('maxval ', maxval)
	return
	 

def main():
	preprocess()

main()