#passed
# for explanation of DFS, http://www.graph-magics.com/articles/euler.php
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
	# reverse() not working here
	circut=circut[::-1]
	return circut

def StringReconstruction(Patterns):
	dB=DeBruijin(Patterns)
	path=EulerianPath(dB)
	Genome=PathToGenome(path)
	return (Genome)

if __name__ == "__main__":
	d=open("dataset_203_7.txt").readlines()
	s=[]
	for i in range (0,len(d)):
		s.append(d[i].strip('\n'))
	print (StringReconstruction(s))
	#patterns=["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]\
