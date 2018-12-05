

file_name = "5a.txt"



#ord Z is 90
def process(x):	
	
	pairs = []
	letters = list(set([ord(i) for i in x]))

	for i in letters:
		if i > 90:
			if (i - 32) in letters: 
				pairs.append( [chr(i), chr(i-32)])
	best = 100000
	
	for p in pairs:
		reducedstring = x.replace(p[0],'').replace(p[1],'')
		score = whit(reducedstring)
		if score < best:
			best = score
	print( "best --> ", best )
	return
		


	
def whit(x):
	b = x[0]
	x = x[1:]
	while x:

		if len(b) == 0:
			b = b + x[0]
			x = x[1:]
			continue

		if abs(ord(b[-1]) - ord(x[0])) == 32:
			b = b[:-1]
			x = x[1:]				
			continue

		if abs(ord(b[-1]) - ord(x[0])) != 32:
			b = b + x[0]
			x = x[1:]		
			continue

	return len(b) + len(x)


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x[0])

main()