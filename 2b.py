

file_name = "2a.txt"

def xor1( a,b ):

	diff = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			diff += 1
	return diff == 1

def commonletters(a,b):
	output = ''
	for i in range(len(a)):
		if a[i] == b[i]:
			output = output + a[i]
	print( "commonletters --> ", output )
	print( "check len ", len(a), len(output) )
	return 


def process(x):

	bank = []
	for r in x:
		r = r.replace('\n','')
		chars = [i for i in r]
		for b in bank:
			if xor1(b,chars):
				print( "found it ", b, chars )

				commonletters( b,chars )
		bank.append(chars)
	return



def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    print(len(x))
	    process(x)

main()