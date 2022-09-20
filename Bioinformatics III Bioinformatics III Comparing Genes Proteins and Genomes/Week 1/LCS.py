def LCS(seq1, seq2, m,n):
	if m==0 or n==0:
		return 0
	elif seq1[m-1]==seq2[n-1]:
		return 1 + LCS(seq1, seq2, m-1, n-1)
	else:
		return max(LCS(seq1, seq2, m-1, n),LCS(seq1, seq2, m, n-1))

if __name__ == "__main__":
	seq1="ACTGCA"
	seq2="CATCGC"
	a=LCS(seq1 , seq2, len(seq1), len(seq2))
	print (a)
	