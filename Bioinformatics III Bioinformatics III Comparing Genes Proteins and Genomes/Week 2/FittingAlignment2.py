# score should be right but alignment has gaps (-) off 
import sys
import numpy as np

def FittingAlignment (string1, string2,sigma=1):
	n=len(string2)
	m=len(string1)
	s=np.matrix(np.zeros((n+1)*(m+1),dtype = np.int).reshape((n+1),(m+1)))
	backtrack=np.matrix(np.zeros((n+1)*(m+1),dtype = np.int).reshape((n+1),(m+1)))
	s[0,0]=0
	backtrack[0,0]=0
	#  initiate values of vertical border as 0
	for j in range (1,m+1):
		s[0,j]=0
		backtrack[0,j]=0 #freeride
	#  initiate values of vertical border as -sigma
	for i in range (1,n+1):
		s[i,0]=s[i-1,0]-sigma
		backtrack[i,0]=2 
		
	for i in range (1,n+1):
		for j in range (1,m+1):
			down=s[i-1,j]-sigma
			right=s[i,j-1]-sigma
			if string2[i-1]==string1[j-1]:
				match=s[i-1,j-1]+1
			else:
				match=s[i-1,j-1]-sigma
			s[i,j]=max([down,right,match])
			if s[i,j]==down:
				backtrack[i,j]=1
			if s[i,j]==right:
				backtrack[i,j]=2
			if s[i,j]==match:
				backtrack[i,j]=3
	# find the max value in the matrix, then the location of it
	i=n
	j=np.argmax(s[n,:])
	return s[i,j], backtrack,i,j

def OutputLCS(backtrack, string1, string2,n,m):
	#n=len(string2)
	#m=len(string1)
	s1=''
	s2=''
	while n>0 or m>0:
		if backtrack[n,m]==1:
			n=n-1
			s2=string2[n]+s2
			s1='-'+s1
		elif backtrack[n,m]==2:
			m=m-1
			s2='-'+s2
			s1=string1[m]+s1
		elif backtrack[n,m]==3:
			n=n-1
			m=m-1
			s2=string2[n]+s2
			s1=string1[m]+s1
		else:
			n=0
			m=0
	return s1,s2
	
if __name__ == "__main__":
	string1='GTAGGCTTAAGGTTA'
	string2='TAGATA'
	'''file=open("dataset_247_10.txt").readlines()
	lines=[line.rstrip() for line in file]
	string1=lines[0]
	string2=lines[1]
	maxscore,backtrack,n,m=LocalAlignment(string1,string2,sigma=1)
	s1, s2 =OutputLCS(backtrack, string1, string2,n,m)
	sourcefile = open("Best_Local_Alignments.txt" , "w")
	print(maxscore , s1 , s2 , sep="\n" , file=sourcefile)
	'''
	maxscore,backtrack,n,m=FittingAlignment(string1,string2,sigma=1)
	s1, s2 =OutputLCS(backtrack, string1, string2,n,m)
	print ('maxscore ',maxscore,'s1 ',s1,'s2 ', s2)