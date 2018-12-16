
file_name = "8a.txt"

import json
import pprint
pp = pprint.PrettyPrinter(indent=4)


def cut(s):
	scop = s.copy()
	index=0
	scop.insert(index,'[')
	index += 1
	mqueue = []
	cqueue = []
	while s:
		c=s.pop(0)
		index += 1
		m=s.pop(0)
		index +=1
		if cqueue:
			cqueue[-1] -= 1	
		
		if c==0:
			for i in range(m):
				s.pop(0)
				index+=1
			scop.insert(index,']')
			index += 1
			if cqueue[-1] > 0:
				scop.insert(index,'[')
				index += 1
			
			while cqueue and cqueue[-1] == 0:
				if cqueue[-1] == 0: cqueue.pop() 
				qtym = mqueue.pop()
				for i in range(qtym):
					s.pop(0)
					index+=1
				scop.insert(index,']')
				index += 1
				if cqueue:
					if cqueue[-1] > 0:
						scop.insert(index,'[')
						index += 1
			continue
		
		if c>0:
			scop.insert(index, '[')
			index+=1
			mqueue.append(m)
			cqueue.append(c)
			continue
	
	strscop = ','.join([str(i) for i in scop])
	ss = strscop.replace(',]',']').replace('[,','[')
	ps = json.loads(ss)
	return ps


def count(r):
	total = 0
	children = [c for c in r if isinstance(c, (list,)) ]
	meta = r[len(r)-r[1]:]

	if len(children) == 0:
		total += sum(meta)

	else:
		active = [i for i in meta if 0 < i <= len(children) ]
		if len(active) > 0:
			for a in active:
				total += count(children[a-1])

	return total

def process(x):	
	s = []
	for r in x.split(' '):
		s.append( int(r) )
	scop = cut(s)
	t = count(scop)
	print( t )

	return

def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x[0]))
	    process(x[0])

	    #process("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") ## important


main()