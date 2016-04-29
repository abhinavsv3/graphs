import louvaininpy as l
import json
from copy import deepcopy

class jsoninpy:

	def __init__(self):
		self.la = []
		self.lb = []
		self.jd = {"nodes":self.la,"edges":self.lb}
		print "Constrcutor"
# default node size is 20 but with the size 
#I increase the size of the node further to show bigger visual

	def jsonRoot(self, i,size): 
		print "Creating Root",i 
		k = {}
		k['id'] = str(i)
		k['root'] = True
		k['type'] = str(i)
		k['title'] = str(i)
		k['sizes'] = str((size*2) + 20)
		k['type'] = "root"
		self.jd['nodes'].append(deepcopy(k))
	
	def jsonNode(self,id,clusterid,size = 20 ): # default node size is set as 20 
		"""All three are integers"""
		k = {}
		k['id'] = str(id)
		k['cluster'] = str(clusterid)
		k['title'] = str(id)
		k['relatedness'] = "0.5"
		k['sizes'] = str(size)
		k['type'] = "node"
		self.jd['nodes'].append(deepcopy(k))
		
	def jsonEdge(self,src,dst,relat = 0.5):
		"""All three are integers"""
		m = {}
		m["source"] = str(src)
		m["target"] =  str(dst)
		m["relatedness"] =  str(relat)
		m["type"] = "edge"
		self.jd['edges'].append(m)

	def jsonDump(self,filename):
		"""filename is a string"""
		prin = json.dumps(self.jd,indent = 4)
		print prin
		f = open(filename,"w")
		f.write(prin)
		f.close()

"""
#Driver tests
jj = jsoninpy()

for i in range(5):
	jj.jsonNode(i,5)

for i in range(5):
	jj.jsonRoot(i,5)

for i in range(5):
	jj.jsonEdge(i,5-i)

jj.jsonDump("1.json")



print "here"
"""