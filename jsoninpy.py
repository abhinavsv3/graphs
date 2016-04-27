import louvaininpy as l
import json
from copy import deepcopy

class jsoninpy:

	def __init__(self):
		self.la = []
		self.lb = []
		self.jd = {"nodes":self.la,"edges":self.lb}
		print "Constrcutor"

	def jsonRoot(self, i):
		print "Creating Root",i 
		k = {}
		k['id'] = str(i)
		k['root'] = True
		k['type'] = str(i)
		k['title'] = str(i)
		self.jd['nodes'].append(deepcopy(k))
	
	def jsonNode(self,id,clusterid):
		"""All three are integers"""
		k = {}
		k['id'] = str(id)
		k['cluster'] = str(clusterid)
		k['title'] = str(id)
		k['relatedness'] = "0.5"
		self.jd['nodes'].append(deepcopy(k))
		
	def jsonEdge(self,src,dst):
		"""All three are integers"""
		m = {}
		m["source"] = str(src)
		m["target"] =  str(dst)
		m["relatedness"] = "0.5"
		self.jd['edges'].append(m)

	def jsonDump(self,filename):
		"""filename is a string"""
		prin = json.dumps(self.jd,indent = 4)
		print prin
		f = open(filename,"w")
		f.write(prin)
		f.close()

jj = jsoninpy()

for i in range(5):
	jj.jsonRoot(i)

for i in range(5,0):
	jj.jsonEdge(i,5-i)

print "here"