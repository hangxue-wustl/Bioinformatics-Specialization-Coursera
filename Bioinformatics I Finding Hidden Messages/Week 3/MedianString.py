def HammingDistance(p, q):
    count = 0
    if len(p) == len(q):
        for i in range(len(p)):
            if p[i] != q[i]:
                count += 1
    return count	
	
def MedianString(Dna,k):
	kmerList=[]
	kmerAll=set()
	# create all possible kmers
	# create all possible kmers in all  strings and store in a list of set
	for i in range (len(Dna)):
		kmerbyString=set()
		for j in range (len(Dna[i])-k+1):
			pattern=Dna[i][j:j+k]
			kmerbyString.add(pattern)
			kmerAll.add(pattern)
		kmerList.append(kmerbyString)
	# for all possible kmers
	# dict [kmer, distance]
	median=dict()
	for m in kmerAll:
		distance=0
		for n in kmerList:
			localDistance=1000000
			for item in n:
				if (localDistance > HammingDistance(m,item)):
					localDistance=HammingDistance(m,item)
			distance=distance+localDistance
		d={m:distance}
		median.update(d)
	m=min(median.values())
	return [t for t, v in median.items() if v==m]	
	

    
if __name__ == "__main__":
	Dna=["AATAATGAGCCATATAATTTGCCTTGTAACTAAGGGCGATCA","TGTGACGTGATGTAAGGATACGTTACCGGGATACTAGGGGTC","GAGCGATGCTCTCCAGAACTCAATTTCCGCATTCTATAAGGT","CATAAACTCACCAATCGAGTCACGAAATTCTAAGGATTCGGG","ATAACAATCCGTAAGACTCAGTCTTAAGGTGCCAGAAGCAGC","TGGCCCGGAGGGGCACTTATCCTACGAACCTAAGGGGATCCC","ACTCTAGGATACTAAGGAGTGTGGCAGATTTAGGATACAATT","CTTAGTCGAACGGGTAAGGCGCGGAAATCTTAAGGCTATGCT","TGAGTTTCTTTTCAGATGGAGCACCATGTCTAAGGCGTAACC","GATCCAGAGTTGTTATGCGCCCACGGAATATAAGGCACTGTC"]
	k=6
	print (*MedianString(Dna, k))