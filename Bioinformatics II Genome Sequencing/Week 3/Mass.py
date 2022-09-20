#passed not did not understand why. Visualization can help http://www.pythontutor.com/visualize.html#mode=display
def CountingMass(Mass, masslist):
	Alphabet = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113:'I/L',114: 'N', 115: 'D', 128: 'K/Q', 129: 'E',131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}
	if Mass == 0: return 1,masslist
	if Mass<57: return 0,masslist
	if Mass in masslist: return masslist[Mass],masslist
	n=0
	for i in Alphabet:
		print ("i ",i, "Mass-i",Mass-i)
		k, masslist=CountingMass(Mass-i,masslist)
		n+=k
		print ("i ", i, k,"and", masslist)
	masslist[Mass]=n
	return n, masslist

if __name__ == "__main__":
	print(CountingMass(128,{}))