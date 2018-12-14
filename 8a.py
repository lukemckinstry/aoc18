
file_name = "8a.txt"

def tree(s):
	total = 0
	mqueue = []
	cqueue = []
	while s:
		c=s.pop(0)
		m=s.pop(0)
		if cqueue: cqueue[-1] -= 1		
		if c==0:
			mid = [s.pop(0) for i in range(m)]
			total += sum(mid)
			while cqueue and cqueue[-1] == 0:
				if cqueue[-1] == 0: cqueue.pop() 
				qtym = mqueue.pop()
				mid = [s.pop(0) for i in range(qtym)]
				total += sum(mid)
			continue
		if c>0:
			depth += 1
			mqueue.append(m)
			cqueue.append(c)
			continue
	return total


def process(x):	
	s = []
	for r in x.split(' '):
		s.append( int(r) )
	out = tree(s)
	print( out )
	return

def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x[0]))
	    process(x[0])
	    #process("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")

main()