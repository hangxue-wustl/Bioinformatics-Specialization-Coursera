#correct
import sys
import numpy as np
import copy

def GreedySorting (P):
	distance=0
	RevList=[]
	for i in range (len(P)):
		# if not matched
		if i+1 !=abs (P[i]):
			for j in range (i+1, len(P)):
				# find the matched number, then break and reverse
				if i+1==abs(P[j]):
					b=j
					break
			P=P[:i]+[-e for e in reversed (P[i:b+1])]+P[b+1:]
			RevList.append(copy.deepcopy(P))
			distance=distance+1
		# if negative of matched
		if i+1==-P[i]:
			P[i]=-P[i]
			RevList.append(copy.deepcopy(P))
			distance=distance+1
	return distance, RevList

def printList (RevList):
	for p in RevList:
		print('('+' '.join(['+'+str(e) if e>0 else str(e) for e in p])+')')

if __name__ == "__main__":
	P=[-3, +4, +1, +5, -2]
	distance, RevList=GreedySorting(P)
	printList(RevList)
	print (distance)