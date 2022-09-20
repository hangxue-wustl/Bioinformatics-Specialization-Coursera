def compute_probability(kmer,profile_matrix):
	prob=1
	for i in range(0,len(kmer)):
		for N, P in profile_matrix.items(): 
			if N==kmer[i]:
				item_prob=P[i]
		prob=prob*item_prob
	return prob


def profile(dna_seq,k,profile_matrix):
	maxP=0
	for i in range(len(dna_seq)-k+1):
		kmer=dna_seq[i:i+k]
		prob=compute_probability(kmer,profile_matrix)
		if prob>maxP:
			maxP=prob
			answer=kmer
	return answer

if __name__ == "__main__":
	profile_matrix = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],'C': [0.4, 0.3, 0.1, 0.5, 0.1],'G': [0.3, 0.3, 0.5, 0.2, 0.4],'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
	dna_seq="ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
	k=5
	answer=profile(dna_seq,k, profile_matrix)
	print (answer)
    