

file_name = "12a.txt"
#file_name = "12ex.txt"

import numpy as np
import re

start = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'

#start = '#..#.#..##......###...###'


def preprocess(x):
	records = []
	for r in x:
		row = r.replace('\n','').split('=>')
		records.append([row[0].strip(),row[1].strip()])
	return records

def xor(s,rec):
	for r in rec:
		if all([ s[i] == r[0][i] for i in range(5) ]):
			print( 'xor ', s, r[1] )
			return r[1]
	else:
		print( 'xor ', s, '.' )
		return '.'



def iter(s, r):
	print(len(s))
	s = '..........' + s + '..............................'
	print(s)
	sl = [i for i in s]
	slx = sl.copy()
	cycle = 0
	while cycle < 20:
		sl = [slx[i] for i in range(len(sl))]
		for i in range(0,len(sl)-5):
			sli = sl[i:i+5]
			res = xor(sli,r)
			slx[i+2] = res
		cycle += 1	
		print( ''.join(slx) )
	total = 0
	for i in range(0,len(slx)):
		if slx[i] == '#':
			total += (i-10)
	print('t->', total)
	return




def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    records = preprocess(x)
	    iter(start,records )
	    #print(x)
	    

main()