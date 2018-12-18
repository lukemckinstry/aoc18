

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


def box(x,y):
	total = 0
	for xi in range(0,3):
		for yi in range(0,3):
			total += calc(x+xi,y+yi)
	return total


def preprocess():
	maxval = 0
	maxbox = 0,0

	for x in range(1,299):
		print(x)
		for y in range(1,299):

			val = box(x,y)
			if val > maxval:
				maxval = val
				maxbox = x,y
	print('maxval ', maxval)
	print('maxbox ', maxbox)

def main():
	preprocess()

main()