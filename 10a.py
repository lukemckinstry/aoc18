

file_name = "10a.txt"

import numpy as np
np.set_printoptions(threshold=np.nan)
import re


def preprocess(x):
	pre = re.compile(r'(?<=position=<).*(?=> v)')
	vre = re.compile(r'(?<=velocity=<).*(?=>)')
	records = []
	for r in x:
		pm = pre.findall(r)
		vm = vre.findall(r)
		p = [ int(i.strip()) for i in pm[0].split(',')]
		v = [ int(i.strip()) for i in vm[0].split(',')]
		rd = {"p": p, "v": v}
		records.append( rd )
	return records


def render(x):
	px = [i['p'][0] for i in x]
	py = [i['p'][1] for i in x]
	print( 'x positions->', min(px), max(px), ' range ', max(px) - min(px)) 
	print( 'y positions->', min(py), max(py), ' range ', max(py) - min(py)) 
	xr = max(px) - min(px)
	yr = max(px) - min(px)	
	charar = np.chararray((yr+1, xr+1))
	for r in x:
		xx,yy = r['p']		
		charar.itemset((yy-179,xx-190), b'#')
	check = charar.count(b'#')
	print( check)


def stats(x):
	px = [i['p'][0] for i in x]
	py = [i['p'][1] for i in x]
	xmode = max(px, key=lambda l: px.count(l))
	ymode = max(py, key=lambda l: py.count(l))
	return px.count(xmode) * py.count(ymode)

def step(x):
	modemax = 0
	modemaxindex = 0
	count=0
	while count <= 10866:
		for r in x:
			r['p'][0] += r['v'][0]
			r['p'][1] += r['v'][1]
		# m = stats(x)
		# if m > modemax:
		# 	modemax = m
		# 	modemaxindex = count
		if count == 10866:
			render(x)
			break
		count += 1

	#print( 'modemax ', modemax )
	#print( 'modemaxindex ', modemaxindex )
	return


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    x = preprocess(x)
	    step(x)

main()