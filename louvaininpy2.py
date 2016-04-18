import louvaininpy as l
import json
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
roots = range(0,len(partition))

la = []
lb = []
jd = {"nodes":la,"edges":lb}
buf = len(partition)
print "Buf",buf
for i in roots:
	print "Creating Root",i ," With nodes", partition[i]
	k = {}
	k['id'] = str(i)
	k['root'] = True
	k['type'] = str(i)
	k['title'] = str(i)
	jd['nodes'].append(deepcopy(k))
	for j in partition[i]:
		k = {}
		k['id'] = str(j+buf)
		k['cluster'] = str(i)
		k['title'] = str(j+buf)
		k['relatedness'] = "0.5"
		jd['nodes'].append(deepcopy(k))

for i in range(0,g.length):
	print "Creating Edge :", g.start[i], "--",g.wgt[i], "-->", g.dest[i]
	m = {}
	m["source"] = str(g.start[i]+buf)
	m["target"] =  str(g.dest[i]+buf)
	m["relatedness"] = str(g.wgt[i])
	jd['edges'].append(m)





prin = json.dumps(jd,indent = 4)
print prin

f = open("testjsons.json","w")
f.write(prin)
f.close()
