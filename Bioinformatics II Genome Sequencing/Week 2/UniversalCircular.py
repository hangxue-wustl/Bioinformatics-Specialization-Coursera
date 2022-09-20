#not passed
#the answer I have is difference for k=4 but I think is correct
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
		if i[:-1] in adjacent_list:
			adjacent_list[i[:-1]].append(i[1:])
		else:
			adjacent_list[i[:-1]]=[]
			adjacent_list[i[:-1]].append(i[1:])
	return adjacent_list

def bkmers(a):
	bkmers=["".join(i) for i in itertools.product('01', repeat=k)]
	return bkmers
	
def EulerianPath(nodes):
	# current=location
	current=list(nodes.keys())[0]
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
	# if no more neighbors, then add temp into circut, until another one  has neighbors
		else:
			circut.append (current)
			current=temp.pop()
	# Do not miss the last one, or the original one to form a circle
	circut.append(current)
	circut=circut[::-1]
	# reverse() not working here
	return circut

def StringReconstruction(Patterns):
	dB=DeBruijin(Patterns)
	path=EulerianPath(dB)
	Genome=PathToGenome(path)
	return (Genome)
	
if __name__ == "__main__":
	k=3
	bkmers=bkmers(k)
	print (StringReconstruction(bkmers))
	