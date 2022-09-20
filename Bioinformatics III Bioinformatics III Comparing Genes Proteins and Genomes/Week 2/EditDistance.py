#passed
import sys
import numpy as np

def GlobalAlignment (string1, string2,sigma=1):
	n=len(string1)
	m=len(string2)
	s=np.matrix(np.zeros((n+1)*(m+1),dtype = np.int).reshape((n+1),(m+1)))
	backtrack=np.matrix(np.zeros((n+1)*(m+1),dtype = np.int).reshape((n+1),(m+1)))
	s[0,0]=0
	backtrack[0,0]=0
	# mismatch and gap =-1, match=0, initiate values of border as decreasing of -1
	for i in range (1,n+1):
		s[i,0]=s[i-1,0]-sigma
		backtrack[i,0]=1 #down
	for j in range (1,m+1):
		s[0,j]=s[0,j-1]-sigma
		backtrack[0,j]=2 #right
	for i in range (1,n+1):
		for j in range (1,m+1):
			down=s[i-1,j]-sigma
			right=s[i,j-1]-sigma
			# modify the match score
			if string1[i-1]==string2[j-1]:
				match=s[i-1,j-1]+0
			else:
				match=s[i-1,j-1]-sigma
			s[i,j]=max([down,right,match])
			if s[i,j]==down:
				backtrack[i,j]=1
			if s[i,j]==right:
				backtrack[i,j]=2
			if s[i,j]==match:
				backtrack[i,j]=0
			#print (s[i,j], " and ", backtrack[i,j])
	return s[n,m], backtrack

def OutputLCS(backtrack, string1, string2):
	n=len(string1)
	m=len(string2)
	s1=''
	s2=''
	while n>0 or m>0:
		if backtrack[n,m]==1:
			n=n-1
			s1=string1[n]+s1
			s2='-'+s2
		elif backtrack[n,m]==2:
			m=m-1
			s1='-'+s1
			s2=string2[m]+s2
		else:
			n=n-1
			m=m-1
			s1=string1[n]+s1
			s2=string2[m]+s2
		#print ("backtrack", backtrack[n,m], s1, " and ", s2)
	return s1,s2

#def HammingtonDistance(s1,s2):
	
if __name__ == "__main__":
	#string1='PLEASANTLY'
	#string2='MEANLY'
	file=open("dataset_248_3.txt").readlines()
	lines=[line.rstrip() for line in file]
	string1=lines[0]
	string2=lines[1]
	maxscore,backtrack=GlobalAlignment(string1,string2,sigma=1)
	s1, s2 =OutputLCS(backtrack, string1, string2)
	print ('maxscore ',maxscore,'s1 ',s1,'s2 ', s2)