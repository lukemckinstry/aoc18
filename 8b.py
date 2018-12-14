
file_name = "8a.txt"


def dddwee(s):
	depthqueue = {}
	t = []
	mqueue = []
	cqueue = []
	depth = 0
	maxdepth = 0
	print(s)
	while s:
		print('depth->',depth)
		c=s.pop(0)
		m=s.pop(0)
		print('##before cqueue ## ', cqueue )
		if cqueue: cqueue[-1] -= 1
		print('##after cqueue ## ', cqueue )
		#print('mqueue->', mqueue)
		#print('cqueue->', cqueue)
		print(c,m)
		if c==0:
			mid = [s.pop(0) for i in range(m)]
			#total += sum(mid)
			t.append(mid)
			print('mid (zero-child-node)->',mid)
			#print('mqueue c==0 ->', mqueue)
			#depth-=1
			#print('loosing depth now ->',depth)
			print('before loop cqueue after zero-child-node ->', cqueue)
			#if depth > maxdepth: maxdepth = depth
			while cqueue and cqueue[-1] == 0:
				print('in loop cqueue after zero-child-node ->', cqueue)
				prevmid = mid
				#print( '###cqueue -> ', cqueue  )
				if cqueue[-1] == 0: cqueue.pop() 
				qtym = mqueue.pop()
				mid = [s.pop(0) for i in range(qtym)]
				depth-=1
				print('loosing depth now ->',depth)
				print(mid, ' is in parent of ', prevmid )
				#total += sum(mid)
				t.append(mid)
				print('mid->',mid)
			continue
		if c>0:
			depth += 1
			#if depth > maxdepth: maxdepth = depth
			mqueue.append(m)
			cqueue.append(c)
			continue

 
	#are the meta ids unique
	checker = [ (','.join(str(x) for x in i)) for i in t ]	
	print( 'len checker ->', len(checker))
	print( 'set checker ->', len(set(checker)))
	print( 'depth->', depth )
	print( 'maxdepth->', maxdepth )

	return


def process(x):	
	s = []
	for r in x.split(' '):
		s.append( int(r) )
	out = dddwee(s)
	print( out )
	#print( s )
	return

def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x[0]))
	    #process(x[0])

	    process("2 3 1 1 1 1 0 1 99 44 2 0 3 10 11 12 1 1 2") ## important
	    
	    #process("2 3 1 1 0 1 99 2 0 3 10 11 12 1 1 2") ## important

	    #process("3 3 0 3 10 11 12 1 1 0 1 99 0 3 10 11 12 2 1 1 2")
	    #process("2 3 0 3 10 11 12 1 1 2 3 0 3 10 11 12 1 1 0 1 0 2 1 1 2 2 1 1 2")
	    #process("0 1 99 0 1 88")
	    #process("1 1 0 1 88 2")
	    #process("1 1 0 1 99 1 1 0 1 88 2 2") #
	    #process("0 1 99")

main()