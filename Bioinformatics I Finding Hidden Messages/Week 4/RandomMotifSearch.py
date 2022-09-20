import numpy as np
import random

# A helper method of profile
def compute_probability(kmer,profile_matrix):
	prob=1
	for i in range(0,len(kmer)):
		for N, P in profile_matrix.items(): 
			if N==kmer[i]:
				item_prob=P[i]
		prob=prob*item_prob
	return prob


# This function choose the best match of kmer in the string according to the profile matrix
def profile(dna_seq,k,profile_matrix):
	maxP=0
	answer=dna_seq[0:k]
	for i in range(len(dna_seq)-k+1):
		kmer=dna_seq[i:i+k]
		prob=compute_probability(kmer,profile_matrix)
		if prob>maxP:
			maxP=prob
			answer=kmer	
	return answer

# This is a helper method of creating profile_matrix
def Count(motifs):
	A=[0]*len(motifs[0]);
	C=[0]*len(motifs[0]);
	G=[0]*len(motifs[0]);
	T=[0]*len(motifs[0]);
	for i in range (len(motifs[0])):
		for l in motifs:
			if l[i]=='A':
				A[i]=A[i]+1
			if l[i]=='C':
				C[i]=C[i]+1
			if l[i]=='G':
				G[i]=G[i]+1
			if l[i]=='T':
				T[i]=T[i]+1
	# i+1 is for pseudocount so that the prob will not be equal to zero but will be a small number
	ProfileA=[(i+1)/len(motifs) for i in A]
	ProfileC=[(i+1)/len(motifs) for i in C]
	ProfileG=[(i+1)/len(motifs) for i in G]
	ProfileT=[(i+1)/len(motifs) for i in T]
	countMotifs=[]
	countMotifs.append(ProfileA)
	countMotifs.append(ProfileC)
	countMotifs.append(ProfileG)
	countMotifs.append(ProfileT)
	return countMotifs

				
def Score(motifs):
	score=0
	freq=zip(*Count(motifs))
	for i in freq:
		score=score+(1-np.max(i))
	return score
	
def OneRandomizedMotifSearch(Dna, k, t):
	
	#randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
	#generate t random r
	r = [random.randint(0, len(Dna[0])-k) for _ in range(t)]
	Motifs = [Dna[i][r[i]:r[i]+k] for i in range(t)]
	BestMotifs=Motifs[:]
	while True:
		#form profile matrix 
		seq='ACGT'
		Numberonly=Count(BestMotifs)
		profile_matrix={seq[i]:Numberonly[i] for i in range (4)}
		# find the best match in each string and store in TempMotifs
		TempMotifs=[]
		for i in Dna:	
			TempMotifs.append(profile(i,k,profile_matrix))
		# compare best and temp and update
		if Score(TempMotifs)<Score(BestMotifs):
			BestMotifs=TempMotifs[:]
		else:
			return BestMotifs

def RandomizedMotifSearch(Dna, k, t, iter=1000):
	BestScore=float('inf')
	random.seed()
	# iterate multiple times and find the bestMotifs among all iterations
	for i in range (iter):
		currentBest=OneRandomizedMotifSearch(Dna, k,t)
		if Score(currentBest)<BestScore:
			BestScore=Score(currentBest)
			BestMotifs=currentBest
	return BestMotifs
	
	
	
if __name__ == "__main__":
	# this code pass the Code-graded
	k,t=[int(a) for a in input().strip().split(" ")]
	Dna=[]
	for _ in range (t):
		Dna.append(input())
	ans=RandomizedMotifSearch(Dna,k,t,iter=1000)
	for a in ans:
		print(a)

	#dna=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
	#d=open("dataset_161_5.txt").readlines()
	#d=d[1:]
	#s=[]
	#for i in range (0,len(d)):
		#s.append(d[i].strip('\n'))
	#print (s)
	#k=15
	#t=20
	#print (*RandomizedMotifSearch(s, k, t, iter=100))
	#print (OneRandomizedMotifSearch(dna,k,t))
	#print (profile(dna,k,profile_matrix))
	#Random
	
