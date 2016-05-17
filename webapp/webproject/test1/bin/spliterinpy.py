import jsoninpy as jj
from copy import deepcopy

def splitroot(g,partition):
	lenp = len(partition)
	roots = zip([i for i in range(len(partition))],[len(i) for i in partition])
	y = 0
	d = {} 
	# d tells the group of the node
	for i in partition:
		for j in i:
			d[j] = y
		y = y + 1
	print d	

	print roots[0][0]	

	#Create the root json
	newj = jj.jsoninpy()
	newnode = jj.jsoninpy()
	for i in roots:
		newj.jsonRoot(i[0],i[1])	

	#Creating the nodes
	l = 0
	for i in partition:
		for j in partition[l]:
			newnode.jsonNode(j,l)
		l = l+1	

	matrixa = [[0 for i in range(len(partition))] for j in range(len(partition))]
	print matrixa
	for i in range(0,g.length):
		print "Creating Edge :", g.start[i], "--",g.wgt[i], "-->", g.dest[i]
		newnode.jsonEdge(g.start[i],g.dest[i],g.wgt[i])
		if d[g.dest[i]] == d[g.start[i]]:
			matrixa[d[g.start[i]]][d[g.dest[i]]] += 1
		else:
			matrixa[d[g.start[i]]][d[g.dest[i]]] += 1
			matrixa[d[g.dest[i]]][d[g.start[i]]] += 1	

	newnode.jsonDump("allnodes.json")	

	print matrixa	

	for i in range(0,lenp):
		for j in range(i,lenp):
			newj.jsonEdge(i,j,matrixa[i][j])	

	rootsJsonObject = newj
	return newj
