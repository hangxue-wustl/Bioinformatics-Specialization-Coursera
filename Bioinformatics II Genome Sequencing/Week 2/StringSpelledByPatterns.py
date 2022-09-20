import sys
import itertools

def PathToGenome(patterns):
	n = len(patterns)
	genome=patterns[0]
	for i in range(1,n):
		genome+=patterns[i][-1]
	return genome
	
#check if assembled read pairs are compatible
def StringSpelledByPatterns(paired,k,d):
	keyprefix=[]
	valuesuffix=[]
	for i in range (len(paired)):
		keyprefix.append(paired[i][0])
		valuesuffix.append (paired[i][1])
	#print (keyprefix)
	prefix=PathToGenome(keyprefix)
	print (prefix)
	suffix=PathToGenome(valuesuffix)
	print (suffix)
	l=k+d+1
	for i in range (l,len(prefix)):
		if prefix[i]!=suffix[i-k-d]:
			return "there is no string spelled by the gapped patterns"
	prefix=prefix+suffix[-k-d::]
	return prefix
		
if __name__ == "__main__":
	#paired=[["GACC","GCGC"],["ACCG","CGCC"],["CCGA","GCCG"],["CGAG","CCGG"],["GAGC","CGGA"]]
	#keys=[]
	#values=[]
	with open('dataset_6206_4.txt', 'r') as file:
		paired = list((line.strip().split('|') for line in file))
	#for i in paired:
		#print (paired[i][0], "|", paried[i][1])
	
		#nums = file.readline().split(" ")
		#x = nums[0]
		#y = nums[1]
		#for line in file:
			#line = line.split("|")
			#keys.append(line[0])
			#values.append(line[1].strip("\n"))
	#paired=[]
	#paired[0]=keys
	#paired[1]=values
	print (StringSpelledByPatterns(paired,50,200))