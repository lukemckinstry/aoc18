

file_name = "2a.txt"

def process(x):
	d = 0
	t = 0
	for r in x:
		r = r.replace('\n','')
		chars = [i for i in r]
		set_let = list(set(chars))
		doubles = any( [ i for i in set_let if chars.count(i) == 2  ]  )
		triples = any( [ i for i in set_let if chars.count(i) == 3  ]  )
		if doubles:
			d += 1
		if triples:
			t += 1
	checksum = d * t
	print( "checksum ", checksum  )

	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    #find_double(x)
	    print(len(x))
	    process(x)

main()