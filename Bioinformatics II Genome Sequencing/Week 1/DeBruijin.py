#tested correct
import sys


def DeBruijinText(k, Dna):
    adjacent_list ={}
    for i in range (len(Dna)-k+1):
        if Dna[i:i+k-1] in adjacent_list:
        	adjacent_list[Dna[i:i+k-1]].append(Dna[i+1:i+k])
        else:
            adjacent_list[Dna[i:i+k-1]]=[]
            adjacent_list[Dna[i:i+k-1]].append(Dna[i+1:i+k])
    return adjacent_list

def DeBruijin(kmer):
	adjacent_list={}
	for i in kmer:
		if i[:-1] in adjacent_list:
			adjacent_list[i[:-1]].append(i[1:])
		else:
			adjacent_list[i[:-1]]=[]
			adjacent_list[i[:-1]].append(i[1:])
	return adjacent_list
	
if __name__ == "__main__":
    data = list(sys.stdin.read().strip().split())
    adjacent_list = DeBruijin(data)
    for m, n in adjacent_list.items():
    	if len(n)>0:
    		print(m+' -> '+','.join(n))