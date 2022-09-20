# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches

# 2.1 find the string with d mismatches to the pattern
def ApproximatePatternMatching(text, pattern, d):
    positions = []  # initializing list of positions
    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(text[i:(i+len(pattern))], pattern) <= d:
            positions.append(i)
    return positions

# 2.2 count number of string with d mismatches to the pattern
def ApproximatePatternCount(text, pattern, d):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(text[i:(i+len(pattern))], pattern) <= d:
            count += 1
    return count

# 1. Find the distance/mismatches between two strings
def HammingDistance(p, q):
    count = 0
    if len(p) == len(q):
        for i in range(len(p)):
            if p[i] != q[i]:
                count += 1
    return count

# 3. Find neighbors with 1 mismatch to the pattern
def immediate_neighbor(pattern):
    neighborhood = set()
    for i in range (len(pattern)):
        symbol = pattern[i]
        for x in "ACGT":
            if symbol != x:
                neighbor = pattern[:i]+x+pattern[i+1:]
                neighborhood.add(neighbor)
    return neighborhood

# 4.1 Finding d mismatches of a pattern using loop
def Neighbors(pattern,d):
	if d==0:
		return pattern
	neighbor=set()
	neighbor.add(pattern)
	# number of loops=number of nucleotide change
	for i in range (1, d+1):
		for p in neighbor:
			neighbor=neighbor.union(immediate_neighbor(p))
	return neighbor
	
# 4.2 Finding d mismatches of a pattern using recursion
def NeighborsRecursive(pattern, d):
	if d==0:
		return pattern
	if len(pattern)==1:
		return {'A', 'C', 'G', 'T'}
	Neighborhood=set ()
	# remove the first nucleotide in pattern until only 1 nucleotide left, then build on it
	SuffixNeighbors=NeighborsRecursive(pattern[1:], d)
	for i in SuffixNeighbors:
		if HammingDistance(pattern[1:], i)<d:
			for x in "ACGT":
				Neighborhood.add(x+i)
		else:
			Neighborhood.add(pattern[0]+i)
	return Neighborhood
	
# 5.1 Find the most frequent k-mers with d mismatches in a string.	
def FrequentWordsWithMismatches(Genome, k, d):
	counts=dict()
	for i in range (len(Genome)-k+1):
		neighbor=Neighbors(Genome[i:i+k],d)
		for n in neighbor:
			counts[n]=counts.get(n,0)+1
	m=max(counts.values())
	return [t for t, v in counts.items() if v==m]
	
# 5.2 Find the most frequent k-mers with mismatches in a string and its compliment.	
def FrequentWordsWithMismatchesWithComplement(Genome, k, d):
	counts=dict()
	for i in range (len(Genome)-k+1):
		neighbor=Neighbors(Genome[i:i+k],d)
		for n in neighbor:
			ncomplement=ReverseComplement(n)
			counts[n]=counts.get(n,0)+1
			counts[ncomplement]=counts.get(ncomplement,0)+1
	m=max(counts.values())
	return [t for t, v in counts.items() if v==m]	

def ReverseComplement(text):
	Complement=""
	for i in range (len(text)):
		if text[len(text)-i-1]=="A":
			Complement += "T"
		if text[len(text)-i-1]=="T":
			Complement += "A"
		if text[len(text)-i-1]=="G":
 			Complement += "C"
		if text[len(text)-i-1]=="C":
 			Complement += "G"
	return Complement
	
	
if __name__ == "__main__":
	Genome=input("what is your genome?")
	k=int(input("what is your k?"))
	d= int(input("what is your d?"))
	print(*FrequentWordsWithMismatchesWithComplement(Genome, k, d))