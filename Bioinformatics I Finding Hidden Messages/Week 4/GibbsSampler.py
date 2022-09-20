# not tested
import numpy as np
import random
import sys

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
	
	
	# The difference between GibbsSampler and Randomized is that during each iteration, GibbsSampler will randomly delete one
	# of the sequences and build profile matrix without that sequence, find the best match in the deleted sequence and add the
	# new motif back. This way it limits local optimum. 
def GibbsSampler(dna, k, t, N):
	
	#randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
	#generate t random r
	r = [random.randint(0, len(Dna[0])-k) for _ in range(t)]
	motifs = [Dna[i][r[i]:r[i]+k] for i in range(t)]
	BestMotifs=motifs[:]
	for j in range (N):
		i=random.randint(0,t-1)
		#form profile matrix without Motifi
		profileWithoutI=(Dna[:i] + Dna[i+1:])
		seq='ACGT'
		Numberonly=Count(profileWithoutI)
		profile_matrix={seq[s]:Numberonly[s] for s in range (4)}
		# find the best match in Motifi
		Motifi=profile(Dna[i],k,profile_matrix)
		# Add the best Motif back
		NewMotifs=motifs[:i] + [Motifi] + motifs[i+1:]
		if Score(NewMotifs)<Score(BestMotifs):
			BestMotifs=NewMotifs
	return BestMotifs

def MultipleGibbsSampler(Dna, k, t, N, iter=20):
	BestScore=float('inf')
	random.seed()
	# iterate multiple times and find the bestMotifs among all iterations
	for i in range (iter):
		current=GibbsSampler(Dna, k,t,N)
		if Score(current)<BestScore:
			BestScore=Score(current)
			BestMotifs=current
	return BestMotifs
	
	
	
if __name__ == "__main__":
	# not tested
	data = list(sys.stdin.read().strip().split())
	k=int(data[0])
	t=int(data[1])
	N=int(data[2])
	Dna=data[3:]
	ans=MultipleGibbsSampler(Dna,k,t,N,iter=20)
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