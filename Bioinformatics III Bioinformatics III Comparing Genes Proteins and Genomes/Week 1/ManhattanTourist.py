# passed
import numpy as np
import sys
def ManhattanTourist(n, m, down, right):
	#s = np.matrix(np.arange((n+1)*(m+1)).reshape((n+1, m+1)))
	s=[]
	for i in range (n+1):
		s.append([0]*(m+1))
	s[0][0]=0
	for i in range (1, n+1):
		s[i][0]=s[i-1][0]+down[i-1][0]
	for j in range (1,m+1):
		s[0][j]=s[0][j-1]+right[0][j-1]
	for i in range (1,n+1):
		for j in range (1,m+1):
			s[i][j]=max([s[i-1][j]+down[i-1][j],s[i][j-1]+right[i][j-1]])
	return s[n][m]
	
if __name__ == "__main__":
	# this reads the file as lists of lists. How to read as a matrix??
	file=open("dataset_261_10.txt").readlines()
	lines=[line.rstrip() for line in file]
	[n,m]=[int(e) for e in lines[0].split()]
	b=lines.index('-')
	down,right=lines[1:b],lines[b+1:]
	down =[[int(e) for e in E.split()] for E in down]
	right=[[int(e) for e in E.split()] for E in right]
	print (down)
	print(ManhattanTourist(n, m, down, right))