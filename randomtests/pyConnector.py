import louvaininpy as l
g = l.louvaininpy()
fname = raw_input("Enter the file name :")
q = raw_input("Is it a weighted graph? y or n:")
print "Initizlizing"
if q == 'y':
	g.createWeightedGraph(fname)
else:
	g.createGraph(fname)
partition, q= g.louvain()
print partition,q

print type(partition)

print g.nodes
print g.edges
print len(partition)
roots = range(0,len(partition))
print roots
print "This", [[i] for i in g.edges]
