# passed
import random
# for explanation of DFS, http://www.graph-magics.com/articles/euler.php
def EulerianCycle(nodes):
	# current=location
	current=random.choice(list(nodes.keys()))
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
	with open('dataset_203_2.txt', 'r') as file:
		nodes = dict((line.strip().split(' -> ') for line in file))
		for key in nodes:
			nodes[key]=nodes[key].split(',')
	# nodes={2:[1,6],1:[0],0:[3],3:[2],8:[7],7:[9],9:[6],6:[5,8],5:[4],4:[2]}
	path_list = EulerianCycle(nodes)
	path_display = "->".join(str(elements) for elements in path_list)
	print (path_display)