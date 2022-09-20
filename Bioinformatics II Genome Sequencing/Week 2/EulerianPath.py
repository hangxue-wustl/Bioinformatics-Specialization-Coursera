# passed
# for explanation of DFS, http://www.graph-magics.com/articles/euler.php
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
			
def EulerianCycle(nodes):
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
	
if __name__ == "__main__":
	with open('dataset_203_6.txt', 'r') as file:
		nodes = dict((line.strip().split(' -> ') for line in file))
		for key in nodes:
			nodes[key]=nodes[key].split(',')
	#nodes={0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]}
	path_list = EulerianCycle(nodes)
	path_display = "->".join(str(elements) for elements in path_list)
	print (path_display)