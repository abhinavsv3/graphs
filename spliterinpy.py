import louvaininpy as l
import json
import jsoninpy
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
print roots
