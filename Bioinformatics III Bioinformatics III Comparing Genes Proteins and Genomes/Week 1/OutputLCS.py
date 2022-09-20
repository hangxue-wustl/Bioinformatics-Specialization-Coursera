#passed
import numpy as np
import sys

def LCSBackTrack(v,w):
	n= len(v)
	m= len(w)
	s=[]
	backtrack=[]
	for i in range (n+1):
		s.append([0]*(m+1))
		backtrack.append([0]*(m+1))
	for i in range (len(v)+1):
		s[i][0]=0
	for j in range (len(w)+1):
		s[0][j]=0
	for i in range (1,n+1):
		for j in range (1, m+1):
			match=0
			if  v[i-1]==w[j-1]:
				match=1
			s[i][j]=max([s[i-1][j], s[i][j-1], s[i-1][j-1] + match])
			if s[i][j]==s[i-1][j]:
				backtrack[i][j]=4 #down
			elif s[i][j] == s[i][j-1]:
				backtrack[i][j]=5 #right
			elif s[i][j] == s[i-1][j-1] + 1 and v[i-1] == w[j-1]:
				backtrack[i][j]=6 #match
	return backtrack
				
def OutputLCS(backtrack, v, i,j):
	sys.setrecursionlimit(1500)
	if i==0 or j==0:
		return ""
	if backtrack[i][j]==4:
		return OutputLCS(backtrack, v, i - 1,j)
	elif backtrack[i][j]==5:
		return OutputLCS(backtrack, v, i,j - 1)
	else:
		return OutputLCS(backtrack, v, i - 1, j - 1) + v[i-1]

if __name__ == "__main__":
	v="AACACCGCGGGACGCCTCGCGAACGACGTCGCAGCTAAGAGTATCACAGATTCACATCTATACCATGGATCGATCCACAAGCAGAGCAGTATTTAAAGGAAAGTACCATGTCGATTATATATCATGCAATACCCAACACCAAGTGGATGGGGTGAGCATGGTGTCCTGTCACTAATCTAATGTTGCCTAACTCTGGGATGATCGATCCCTTTAGCTTGGGTACCTGCGTGCTGTTCCGAGGGGAACTTTTACCCATCGTTTGCATCGCTTGGCTTTACTCTTAGATCTTAATTACTGCAGGGAGGCCACGCTCCGATTCAGGTGTCACGAATTCCCTCTGACGAGTCCTCCGTGTCTGTGACTGTTCTGGCCGTGAGTTACCATATGTAACTGTGCGAGCGAAAGATGAGCGGAATGTACGACTCCAGCTAGACGGGGCCGTCGGAATGCGACTCGTCTATCGTTCATACCCGCGATCGCCCAGTTCCATGCGCAAGGGGCTTGGGAACCATTTGCGAAGCAGAATTTAAAGATCGCTTCTCGCCGCACTCACCTGGAGAGCATCCTTCAAATGGCGTGTATCAGTGGATTGGACAATGCAACGGCACTAATAACGGATAGAGTTAACGCTTAGCGCTGACCGGATATCCCATCCCCGCATGCGGGTGAACCGTTACTAGTTTCTATTGGCACCTTGTTATCAGACCTCTGACCGAACATAGGGCCAAGTAAAGGATGGACTATATTGCAGGTCGTGATTCAATTTCGCGTCATGTTCTCGAGAAACCGGTCATAGTAAAATTGCACATCGCGACACCTGAGTATGTATGAGCCTAACGTCAGTTCCCCGAACTCGGTGGAAAACCCGTTATTGCAAGGGAGGGGTGGTCA"
	w="AACTTGAAAGCACCGTGGGAAGGAATCTATTTACTCCTAAATACCGAGGATTGTGTTTGGGGGCATGCGTCTGGGTCGGCTTGGACATTTAACGCCAGTTCGTTATCCCTATCAGCATGACCAAGTATCTGGCTTTGCCCTATGCATGGATTTATCCGATTGCGCAATGTGCCCGAACCCGAAGTTTAGACGTATCGCCGTTGTCCGGGGCTTTGCGAACGTGGAATATAGAATCTAGTCCCGTTAGAGGAGGGGGAAGAATACCGCGGATTGAGTTCGCACGAACCAATACAGGCCTAGCGTGGCATTGTATTTCGAAGGCACTGCCGCCGAAGGCTAGAGCGCTTACCCTGTCTAGGTTAACGAAAAAAGATCATTCAATTAGCTTACAATCGCGGAGAGGGTCGCTATTGCTGGGGGCGAGATCCGCATCGGGACCAGCTCGCGTGCCACTGTGGTAACAGATGTTAGTGCCTTCGCTGGAATACCGTGTGCTCTCTGACTTGCCATTCGAAGGACGAGTAGTAATTTCGTTTTCACTCCAAAGCAAAGGGGTTTAATAGTGCGCAAGAAACCACCATTGGCTATTGTCAAGACGCTGGCACTCGGATGTAGGAACGGTTATTGGAGTTGGAGAATTTATGCGTTCTCATAGCCACCCGCTCCAGGAGGCCTGGACTCTGAGTACCGTAGTGACCAACTAGCTGTGCTGAGCTGTGTCTGCCCGCTGCTACTCGTCCACTAGGGTTCGTAATTATTATGTGAGAGCCGATCAGGATCCCGGTATTGCAAGTTGAATCCTGCGTAGATAGTTGCGTATCAATCGAAGTGAAGAACGGTAGCTGTACCCTCCGTCACTTGCCAGGGCGTGTACCCTCCGTTTTTGAATACTGCCTAGGATTGCTGGGGTCGGATTAGCCGTCACTTCATGCCTGTGGGTACACCGCG"
	backtrack=LCSBackTrack(v,w)
	print (OutputLCS(backtrack, v, len(v),len(w)))
	