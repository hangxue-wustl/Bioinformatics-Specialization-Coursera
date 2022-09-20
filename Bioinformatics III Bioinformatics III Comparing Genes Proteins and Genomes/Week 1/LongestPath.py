import math
def LongestPath (source, sink, matrix):
	# initiate the highest score of subpath ending at u as minus_infinity
	# here -inf +1 =-inf
	subpath={i:(-1000) for i in range (sink+1)}
	# track processed vertex u,v, source, sink
	vertexv=[]
	for v in matrix:
		vertexv.append(v)
	vertexv=set(vertexv)
	unprocessed=[i for i in vertexv]
	# T the highest score of subpath ending at u and starting at v
	T=[]
	L=[-1]*(sink+1)
	for n in range (sink+1):
		T.append([-1000]*(sink+1))
	# does not work if there are duplicate length of edges? or could not reach the start
	while unprocessed !=[]:
		#everything starts at 0,1,2,3
		v=unprocessed[0]
		for u in matrix[v] :
			T[v][u]=subpath[v]+matrix[v][u]
			if T[v][u]>subpath[u]:
				subpath[u]=T[v][u]
				# best path to u is start from v
				L[u]=v
		unprocessed.remove(v)
	
	BestPath=[]
	u=sink
	BestPath.append(u)
	route=0
	while u !=source :
		BestPath.append(L[u])
		route=route+matrix[L[u]][u]
		u=L[u]
	BestPath.reverse()
	return BestPath, route

if __name__ == "__main__":
	#matrix={0:{1:7,2:4},2:{3:2},1:{4:1},3:{4:3}}
	with open ('dataset_245_7.txt','r') as file:
		matrixlist=[line.strip().split('->') for line in file]
		matrix={}
		for i in matrixlist:
			a,b=i[1].split(':')
			a=int(a)
			b=int (b)
			d={int(i[0]):{a:b}}
			if int(i[0]) in matrix:
				matrix[int(i[0])].update({a:b})
			else:
				matrix.update(d)
	print (matrix)
			#b=int(matrix[start].split(':')[1])
	print(LongestPath(0, 49, matrix))
