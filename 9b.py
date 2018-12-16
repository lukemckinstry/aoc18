
from collections import deque

#425 players; last marble is worth 70848 * 100 points

def prac():
	numplayers = 425
	lastmarble = 70848*100
	scores = [0] * numplayers
	l = deque([0])
	for m in range(1,lastmarble+1):
		if m%23==0:
			l.rotate(7)
			currentplayer = m%numplayers
			scores[currentplayer] += m + l.pop()
			l.rotate(-1)
		else:
			l.rotate(-1)
			l.append(m)
	print('max score->', max(scores))
	return


def main():
	prac()
	return
main()