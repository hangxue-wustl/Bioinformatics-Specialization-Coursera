def ChromosomeToCycle(chromosome):
# slightly modified index for ChromosomeToCycle, so the [0] element now ended up in the -1 position
# [2, 4, 3, 6, 5, 1]
	n=len(chromosome)
	nodes=[0]*2*n
	for j in range (0, n):
		i=chromosome[j]
		if i>0:
			nodes[2*j-1]=2*i-1
			nodes[2*j]=2*i
		else:
			nodes[2*j-1]=-2*i
			nodes[2*j]=-2*i-1
	return nodes

def CycleToChromosomeT(cycle):
# modified index so the -1 element is in the beginning [1, 2, 4, 3, 6, 5]
	nodes=[]
	for i in range (0,len(cycle)):
		nodes.append(cycle[i-1])
	m=len(nodes)
	k=int(m/2)
	chromosome=[0]*k
	for j in range (1, k+1):
		if nodes[2*j-2]<nodes[2*j-1]:
			chromosome[j-1]=int(nodes[2*j-1]/2)
		else:
			chromosome[j-1]=-int(nodes[2*j-2]/2)
	return chromosome
	
def ColoredEdges(P):
	Edges=[]
	for chromosome in P:
		nodes=ChromosomeToCycle(chromosome)
		for j in range (0, len(chromosome)):
			newEdge=[]
			newEdge.append(nodes[2*j])
			newEdge.append(nodes[2*j+1])
			Edges.append(newEdge)
	return Edges
	
def GraphToGenome(GenomeGraph):
	P=[]
	cycleblock={}
	group=0
	cycleblock.update({group:[]})
	for i in range (0, len(GenomeGraph)):
		# if different =1, add into a group
		if GenomeGraph[i][0]-GenomeGraph[i-1][1]==1 or GenomeGraph[i][0]-GenomeGraph[i-1][1]==-1 :
			# cycle break block
			cycleblock[group].append(GenomeGraph[i-1][0])
			cycleblock[group].append(GenomeGraph[i-1][1])
		else:
			cycleblock[group].append(GenomeGraph[i-1][0])
			cycleblock[group].append(GenomeGraph[i-1][1])
			group=group+1
			cycleblock.update({group:[]})
	# union the end and the beginning
	for e in cycleblock[0]:
		cycleblock[group].append(e)
	# delete the beginning
	cycleblock.pop(0)
	for cycle in cycleblock:
		chromosome=CycleToChromosomeT(cycleblock[cycle])
		P.append(chromosome)
	return P
		
def BreakDistance(P,Q):
	# breakdistance=blocks-cycles
	# check if P is nested or not
	if any(isinstance(sub, list) for sub in P) is True:
		blocks=sum([len(a) for a in P])
	else:
		blocks=len(P)
	edges=ColoredEdges(P)+ColoredEdges(Q)
	print (edges)
	# check if any cycles in the edges
	group=0
	visited=[]
	for i in edges:
		if i not in visited:
			visited.append(i)
			visited=Neighbor(visited,edges)
			# if no more neighbors, cycle+1
			group=group+1
	distance=blocks-group
	return distance

def Neighbor(visited,edges):
	for j in edges:
		if j not in visited:
			k=set().union(*visited)
			# check if any neighbors present
			if len(k.intersection(set(j)))!=0:
				visited.append (j)
				# if new neighbor is added, need to start scan j from the beginning of the list
				visited=Neighbor(visited,edges)
	return visited

if __name__ == "__main__":
	#P=[[1, -2, -3], [4, 5,-6]]
	#chromosome=[1,-2,-3,4]
	#Q=[1,2,4,3,6,5,7,8]
	#print (ChromosomeToCycle(chromosome))
	#print (CycleToChromosomeT(Q))
	P=[[1,2,3,4,5,6]]
	Q=[[1,2,3,-6,-5,-4]]
	#cycle=[[2, 4], [3, 6], [5, 1], [7, 9], [10, 12], [11, 8]]
	print (BreakDistance(P,Q))
