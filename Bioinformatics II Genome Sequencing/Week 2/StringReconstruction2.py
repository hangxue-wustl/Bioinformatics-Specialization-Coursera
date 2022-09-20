import sys
import itertools

def PathToGenome(patterns):
	n = len(patterns)
	genome=patterns[0]
	for i in range(1,n):
		genome+=patterns[i][-1]
		
	return genome

def DeBruijin(kmer):
	adjacent_list={}
	for i in kmer:
		if (i[0][:-1]+"|"+i[1][:-1]) in adjacent_list:
			adjacent_list[i[0][:-1]+"|"+i[1][:-1]].append(i[0][1:]+"|"+i[1][1:])
		else:
			adjacent_list[i[0][:-1]+"|"+i[1][:-1]]=[]
			adjacent_list[i[0][:-1]+"|"+i[1][:-1]].append(i[0][1:]+"|"+i[1][1:])
	return adjacent_list

def startNode(nodes):
	start=-1
	for key in nodes:
		out=len(nodes[key])
		ini=0
		for values in nodes.values():
			for i in range (len(values)):
				if values[i]==key:
					ini =ini+1			
		if out>ini:
			start=key
			break
	return start
			
def EulerianPath(nodes):
	# current=location
	current=startNode(nodes)
	#print ("current",current)
	# temp= stack in the above link
	temp=[]
	# circut=path
	circut=[]
	while len(nodes)!=0 or len(temp)!=0: 
		if current in nodes:
			temp.append(current)
			passed=current
	# deal with key that has many values
			if len(nodes[passed])>1:
				current=(nodes[current][0])
				del nodes[passed][0]
			else:
				current=(nodes[current][0])
				del nodes[passed]
			#print ("nodes",nodes)
	# if no more neighbors, then add temp into circut, until another one  has neighbors
		else:
			circut.append (current)
			current=temp.pop()
	# Do not miss the last one, or the original one to form a circle
	circut.append(current)
	# reverse() not working here
	circut=circut[::-1]
	return circut

def StringReconstruction2(Patterns,k,d):
	dB=DeBruijin(Patterns)
	path=EulerianPath(dB)
	Genome=StringSpelledByPatterns(path,k,d)
	return (Genome)

#check if read pairs are compatible
def StringSpelledByPatterns(paired,k,d):
	paired = list((line.strip().split('|') for line in paired))
	keyprefix=[]
	valuesuffix=[]
	for i in range (len(paired)):
		keyprefix.append(paired[i][0])
		valuesuffix.append (paired[i][1])
	#print (keyprefix)
	#print (valuesuffix)
	prefix=PathToGenome(keyprefix)
	#print (prefix)
	suffix=PathToGenome(valuesuffix)
	#print (suffix)
	l=k+d+1
	for i in range (l,len(prefix)):
		if prefix[i]!=suffix[i-k-d]:
			return "there is no string spelled by the gapped patterns"
	prefix=prefix+suffix[-k-d::]
	return prefix
		
if __name__ == "__main__":
	with open('dataset_204_16.txt', 'r') as file:
		paired = list((line.strip().split('|') for line in file))
	print (StringReconstruction2(paired,50,200))
