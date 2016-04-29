import louvaininpy as l
import json
import jsoninpy as jj
from copy import deepcopy

g = l.louvaininpy()
fname = raw_input("Enter the file name :")
q = raw_input("Is it a weighted graph? y or n:")
print "Initizlizing"
if q == 'y':
	g.createWeightedGraph(fname)
else:
	g.createGraph(fname)
partition, q= g.louvain()
print partition
roots = zip([i for i in range(len(partition))],[len(i) for i in partition])
y = 0
d = {}
for i in partition:
	for j in i:
		d[j] = y
	y = y + 1
print d

print roots[0][0]

#Create the root json
newj = jj.jsoninpy()
for i in roots:
	newj.jsonRoot(i[0],i[1])
newj.jsonDump("roots.json")


print g.edges