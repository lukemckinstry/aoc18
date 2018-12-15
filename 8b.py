
file_name = "8a.txt"

import pprint
pp = pprint.PrettyPrinter(indent=4)


def dddwee(s):
	inst = {'s':[],'pc':[]}
	rootqty = s[1]
	inst['root'] = s[len(s)-rootqty:]
	sib = {} 
	for i in range(7):
		sib[i] = {'sibs':[],'seek':[]}

	t = []
	mqueue = []
	cqueue = []
	depth = 0
	while s:
		#print('depth->',depth)
		c=s.pop(0)
		m=s.pop(0)
		if cqueue: cqueue[-1] -= 1
		#print('if exists subtract from depth->',depth,'sib->', sib)
		#if sib[depth]['c']: sib[depth]['c'][-1] -= 1
		
		#print(c,m)
		if c==0:
			mid = [s.pop(0) for i in range(m)]
			#print('mid->',mid)
			t.append(mid)
			while cqueue and cqueue[-1] == 0:
				prevmid = mid
				if cqueue[-1] == 0: cqueue.pop() 
				#print( 'sib depth seek ->', sib[depth]['seek'][-1] )
				if sib[depth]['seek'][-1] == 1:
					#print("here1")
					sib[depth]['seek'].pop()
					if len(sib[depth]['sibs']) > 0:
						#print('there is a sibling(s) waiting', sib[depth]['sibs'])
						sib[depth]['sibs'].append(mid)

						inst['s'].append( {'d':depth-1, 's':sib[depth]['sibs']} )
						#print('here are sibling(s) ****', sib[depth]['sibs'])
						sib[depth]['sibs'] = [] 

				#print('peek at seek d: ', depth, sib)
				depth-=1
				qtym = mqueue.pop()
				mid = [s.pop(0) for i in range(qtym)]
				t.append(mid)
				#print(mid, ' is in parent of ', prevmid )
				inst['pc'].append( {'d':depth, 'pc':[mid,prevmid]} )
				#print('mid->',mid)

			if sib[depth]['seek']:
				if sib[depth]['seek'][-1] > 1:
					#print('here22')
					sib[depth]['seek'][-1]-=1
					sib[depth]['sibs'].append(mid)
			continue
		if c>0:
			depth += 1
			sib[depth]['seek'].append(c)
			mqueue.append(m)
			cqueue.append(c)
			continue

 
	#are the meta ids unique
	#tchecker = [ (','.join(str(x) for x in i)) for i in t ]	
	#print( 'len checker ->', len(tchecker))
	#print( 'set checker ->', len(set(tchecker)))
	#print( 'depth->', depth )
	#print( 'maxdepth->', maxdepth )
	print('rootqty', rootqty)
	print(inst['root'])

	#print('s->',len(inst['s']))
	#print('pc->',len(inst['pc']))


	schecker = [  str(i['d']) +'d'+ (','.join(str(x) for x in i['s'])) for i in inst['s'] ]
	print('s->',len(schecker))
	print('s->',len(set(schecker)))
	#print(pcchecker)

	# pcchecker = [  str(i['d']) +'d'+ (','.join(str(x) for x in i['pc'])) for i in inst['pc'] ]
	# print('s->',len(pcchecker))
	# print('s->',len(set(pcchecker)))
	# print(pcchecker)
	print(inst['s'])

	return inst

def makeid(i):
	return ','.join(str(x) for x in i)

def chomp(inst, root,depth ):
	print('chomp', depth )
	linkchild = [pc['pc'][1] for pc in inst['pc'] if pc['pc'][0] == root and pc['d'] ==depth ]
	print(linkchild)
	if len(linkchild) == 0:
		#print('OPTION 1')
		return { makeid(root) : [] } 
	else:

		sib = [s['s'] for s in inst['s'] if s['s'][-1] == linkchild[0] and s['d']==depth]
		print('sib', sib)
		if len(sib)>0:
			#print('OPTION 2')
			children = sib[0]
			return { makeid(root) : [  chomp(inst,c,depth+1) for c in children ] } 
		else:
			#print('OPTION 3')
			return { makeid(root) : [  chomp(inst,linkchild[0],depth+1) ] } 

		 



def maketree(inst):
	root = inst['root']
	startdepth = 0
	tree = chomp(inst, root, startdepth)
	print('depr')
	pp.pprint( tree )
	t = count(tree)
	print(t)
	return

def count(root):
	#print('################run->',root)
	total = 0
	meta = next([int(x) for x in k.split(',')] for k in root )
	children = next(root[k] for k in root ) 
	if len(children) == 0:
		total += sum(meta)
	else:
		active = [i for i in meta if 0 < i < len(children)+1 ]
		if len(active) > 0:
			for a in active:
				total += count(children[a-1])
	return total


def process(x):	
	s = []
	for r in x.split(' '):
		s.append( int(r) )
	inst = dddwee(s)
	maketree(inst)
	#print( out )
	#print( s )
	return

def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x[0]))
	    #process(x[0])

	    process("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") ## important
	    #process("2 1 4 3 1 1 1 1 0 1 99 44 2 0 3 10 11 12 0 3 110 111 112 0 3 210 211 212 71 71 72 4 3 1 1 1 1 0 1 499 444 42 0 3 510 511 512 0 3 4110 4111 4112 0 3 3210 3211 3212 1 1 2 0000") ## important
	    

	    #process("2 3 1 1 1 1 2 3 1 1 1 1 0 1 99 44 88 1 1 1 1 0 1 99 44 88 1 1 2 44 8 1 1 1 1 2 3 1 1 1 1 0 1 99 44 899 1 1 1 1 0 1 99 44 899 1 1 2 44 8 1 1 2") ## important
	    
	    #process("2 3 1 1 1 1 0 1 99 44 8 1 1 1 1 0 1 199 144 18 1 1 2") ## important
	    
	    #process("2 3 1 1 0 1 99 2 0 3 10 11 12 1 1 2") ## important

	    #process("3 3 0 3 10 11 12 1 1 0 1 99 0 3 10 11 12 2 1 1 2")
	    #process("2 3 0 3 10 11 12 1 1 2 3 0 3 10 11 12 1 1 0 1 0 2 1 1 2 2 1 1 2")
	    #process("0 1 99 0 1 88")
	    #process("1 1 1 1 0 1 88 87 1")

	    #process("1 1 1 1 0 1 88 87 2")
	    #process("1 1 0 1 99 1 1 0 1 88 2 2") #
	    #process("0 1 99")

main()