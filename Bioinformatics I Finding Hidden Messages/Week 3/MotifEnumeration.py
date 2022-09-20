#Input: Integers k and d, followed by a collection of strings Dna.
#Output: All (k, d)-motifs in Dna.


# Generate neighbors with 1 mismatch to the pattern
def immediate_neighbor(pattern):
    neighborhood = set()
    for i in range (len(pattern)):
        symbol = pattern[i]
        for x in "ACGT":
            if symbol != x:
                neighbor = pattern[:i]+x+pattern[i+1:]
                neighborhood.add(neighbor)
    return neighborhood

# Generate d mismatches of a pattern using loop
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
	
def MotifEnumeration(Dna, k, d):
	# create a list of sets 
	kmer_list= []
	for i in Dna:
		Neighbors_set= set()
		for j in range (len(i)-k+1):
			Neighbors_set=Neighbors_set.union(Neighbors(i[j:j+k],d))
		kmer_list.append(Neighbors_set)
	Patterns=kmer_list[0]
	for q in range (1, len(kmer_list)):
		#print (kmer_list[q])
		Patterns=Patterns & kmer_list[q]
	return Patterns

if __name__ == "__main__":
	Dna=["GGGTAGCACAGACTGCATGGATACG","CAATGGTTAAACTGTAGGGTGGCTA","GGGTAACTTGGGTGGTTGGGGTTTA","GGGTATAAGAGGGCTGTAGATTTAC","TACATACCGGGGTTACGGCCTTACT", "GGATATGAATAGCTCAATACTATTG"]
	k=5
	d=1
	print (*MotifEnumeration(Dna, k, d))