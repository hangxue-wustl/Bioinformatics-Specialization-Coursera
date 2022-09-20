#correct
import sys
import numpy as np
import copy

def breakpoint (P):
	breakpoints=0
	#Include 0 and n+1 at the ends of the permutation before counting breakpoints.
	P= copy.deepcopy([0] + P + [len(P)+1])
	for i in range (len(P)-1):
		# if not matched
		if P[i+1]!= P[i]+1:
			breakpoints=breakpoints+1
	return breakpoints

if __name__ == "__main__":
	P=[+3, +4, +5, -12, -8, -7, -6, +1, +2, +10, +9, -11, +13, +14]
	f=open('dataset_287_6.txt','r')
	data=[]
	for line in f:
		data.append(line.strip())
	data=data[0].split()
	P=[int(data[0][1:])] + [int(e) for e in data[1:-1]] + [int(data[-1])]
	print (breakpoint (P))
