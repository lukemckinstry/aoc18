file_name = "12a.txt"
#file_name = "12ex.txt"

import numpy as np
from collections import deque
from itertools import islice
import re

def bitwise(i):
	if i == '#': return '1'
	else: return '0'

start = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'
#start = '#..#.#..##......###...###'

start_bit = ''.join([bitwise(i) for i in start])

def preprocess(x):
	records = {}
	for r in x:
		row = r.replace('\n','').split('=>') 
		pattern = ''.join([bitwise(i) for i in row[0].strip()])
		res = bitwise(row[1].strip())
		records[int(pattern,2)] = res
	return records

def iter(s, r):
	s = '00' + s + '00000'
	totalmodifier = 2
	
	tempS = deque([i for i in s])
	S1 =deque()
	size = 5
	cycle = 0
	while cycle < 20:
		S1.append('0')
		S1.append('0')

		for i in tempS:
			S1.append(i)
		if cycle % 2 == 0:
			S1.append('0')
		if cycle % 16 == 0:
			S1.appendleft('0')
			totalmodifier += 1
		tempS.clear()
		while len(S1) >= size:
			tempS.append( r[int(''.join(islice(S1, 0, size)),2 )])
			S1.popleft()
		tempS.append('0')
		tempS.append('0')

		S1.clear()
		cycle += 1	
		calc(tempS, totalmodifier)
	return
	
def calc(tempS, totalmodifier):

	total = 0
	for i in range(0,len(tempS)):
		if tempS[i] == '1':
			total += (i- totalmodifier )
	print('t->', total)
	return




def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    records = preprocess(x)
	    print(sorted(records))
	    iter(start_bit,records )
	    #print(x)
	    

main()