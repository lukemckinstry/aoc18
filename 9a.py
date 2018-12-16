

#425 players; last marble is worth 70848 points

def step():
	numplayers = 425
	playerscores = [0] * numplayers
	playercounter = 1
	l=[]
	m=1
	l.append(0)
	l.append(1)

	while m<=70848:
		
		if m % 23 == 0:
			cind = relocated

		else:
			cind = l.index(m)
		
		if (m + 1) % 23 == 0:
			n = n - 7
			if n < 0:
				n = len(l) - abs(n)
		else:
			n = (cind + 2)  ### new index insert
			if n > len(l):
				n = n-len(l)
		m+=1		
		if m % 23 == 0:
			currentplayer = playercounter % numplayers
			playerscores[currentplayer] += m
			value = l.pop(n)
			playerscores[currentplayer] += value
			relocated = n
				
		else:
			l.insert(n,m)

		playercounter+=1
		
	print('max->', max(playerscores))
	return


def main():
	step()
main()