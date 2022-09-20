# https://www.mrgraeme.com/greedy-motif-search/
# The motif is added one by one to create the profile matrix, which then is used to compute the best score. 
def compute_probability(kmer,profile_matrix):
	prob=1
	for i in range(0,len(kmer)):
		for N, P in profile_matrix.items(): 
			if N==kmer[i]:
				item_prob=P[i]
		prob=prob*item_prob
	return prob

import numpy as np

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
	
def GreedyMotifSearch(Dna, k, t):
	BestMotifs=[]
	#create a list of first k-mer in each string
	for i in Dna:
		firstKmer=i[0:k]
		BestMotifs.append(firstKmer)
	# for every kmer in the first string, find the best match in every other string, add to the MotifListforProfile
	for i in range (len(Dna[0])-k+1):
		Motif1=Dna[0][i:i+k]
		MotifListforProfile=[]
		MotifListforProfile.append(Motif1)
		for l in range (1,t):
			#form profile
			seq='ACGT'
			Numberonly=Count(MotifListforProfile)
			profile_matrix={seq[i]:Numberonly[i] for i in range (4)}
			MotifListforProfile.append(profile(Dna[l],k,profile_matrix))
		if Score(MotifListforProfile)<Score(BestMotifs):
			BestMotifs=MotifListforProfile
	return BestMotifs
		
	
	
	
	
	
if __name__ == "__main__":
	profile_matrix = {'A': [0.5, 0.5, 0.0], 'C': [0.0, 0.0, 0.5], 'G': [0.5, 0.5, 0.5], 'T': [0.0, 0.0, 0.0]}
	#dna="AAGAATCAGTCA"
	d=open("dataset_159_5.txt").readlines()
	d=d[1:]
	s=[]
	for i in range (0,len(d)):
		s.append(d[i].strip('\n'))
	dna=["GGCGTTCAGGCA", "AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
	k=3
	t=5
	print (GreedyMotifSearch(dna,k,t))
	#print (profile(dna,k,profile_matrix))
	
    