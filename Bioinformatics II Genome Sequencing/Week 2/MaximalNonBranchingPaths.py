#passed
def DeBruijin(kmer):
	adjacent_list={}
	for i in kmer:
		if i[:-1] in adjacent_list:
			adjacent_list[i[:-1]].append(i[1:])
		else:
			adjacent_list[i[:-1]]=[]
			adjacent_list[i[:-1]].append(i[1:])
	return adjacent_list

def MaximalNonBranchingPaths(nodes):
	path=[]
	NonBranchingPath=[]
	nodes1in1out=set()
	explored=set()
	for key in nodes:
		#print ("key",key)
		if not is1in1out(nodes,key):
			if len(nodes[key])>0:
				for values in nodes[key]:
					NonBranchingPath=[key,values]
					while is1in1out(nodes,values):
						explored.add(values)
						NonBranchingPath.append(nodes[values][0])
						values=nodes[values][0]
					path.append(NonBranchingPath)
		else:
			nodes1in1out.add(key)
	for v in nodes1in1out:
		if v not in explored:
			w=v
			NonBranchingPath=[]
			while w in nodes1in1out:
				NonBranchingPath.append(w)
				if w==v and len(NonBranchingPath)>1:
					path.append(NonBranchingPath)
					for node in NonBranchingPath:
						explored.add(node)
					break
				w=nodes[w][0]
	return path

def is1in1out(nodes,v):
	start=-1
	out=0
	if v in nodes:
		out=len(nodes[v])
	ini=0
	for values in nodes.values():
		for i in range (len(values)):
			if values[i]==v:
				ini =ini+1			
	if out*ini!=1:
		return False
	else:
		return True

def printPath(path):
	for p in path:
		print(' -> '.join(p))

if __name__ == "__main__":
	with open('dataset_6207_2.txt', 'r') as file:
		nodes = dict(line.strip().split(' -> ') for line in file)
		for key in nodes:
			nodes[key]=nodes[key].split(',')
	#nodes={'a':['b'],'b':['c'],'c':['d','e'],'f':['g'],'g':['f'],'e':['i'],'i':['k'],'k':['l'],'l':['m'],'z':['o'],'q':['x']}
	path=MaximalNonBranchingPaths(nodes)
	printPath(path)	
