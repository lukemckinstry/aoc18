
file_name = "1a.txt"

def find_double(x):
	seek = True
	mod = len(x)
	f = {}
	count = 0
	neg = 0
	pos = 0

	while seek:
		index = count % mod
		r = x[index]
		row = int(r[0:])
		if r[0] == "+":
			pos += row
		else:
			neg -= row
		this_num = (pos - neg)

		bucket = this_num // 10000
		if bucket not in f:
			f[bucket] = []
			f[bucket].append(this_num)
		else:
			f[bucket].append(this_num)

		print( f.keys() )
		if len(f[bucket]) != len(set(f[bucket])):
			print("double f --> ", this_num)
			seek = False
		count += 1
	return


def main():
	with open(file_name, 'r') as f:
	    x = f.readlines()
	    find_double(x)
	return

main()

