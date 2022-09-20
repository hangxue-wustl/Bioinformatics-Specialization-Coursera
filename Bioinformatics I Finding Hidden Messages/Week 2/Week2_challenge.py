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
	
if __name__ == "__main__":
	d=open("Salmonella_enterica.txt").readlines()
	d=d[1:-1]
	s=""
	for i in range (0,len(d)):
		s=s+d[i].strip('\n')
	# [3764856, 3764858]
	Genome=s[(3764856-425):(3764856+425)]
	k=int(input("what is your k?"))
	d= int(input("what is your d?"))
	print(*FrequentWordsWithMismatchesWithComplement(Genome, k, d))
	# TTATCCACA TGTGGATAA
