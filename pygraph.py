"""
File: pygraph.py
 -- simple graph handling source file
Author   : Abhinav S V
Email    : abhinavsv3@gmail.com
Location : Barcelona, Spain
Time	    : April 2016
"""
class Graph:
	"""gwt : graph's total weight
	m: graph matrix in start,weight, destination
	mt : Transpose of m 
			mt[0]:all starts m
			mt[1]:all weights
			mt[2]:a;;destinations
	nodes : Set of all the nodes
	lnodes: List of all nodes
	type: 0 for not weighted (Default)
	  	  1 for weighted
	"""
	def __init__(self):
		"""Creates an Empty, Unweighted Graph"""
		self.type=0
		self.tname = ["Unweighted","Weighted"]
		#"""Matrix"""
		self.m = []
		#"""Matrix Transpose"""
		self.mt = []
		#Set of all the nodes
		self.nodes = set()
		#List of all the nodes
		self.lnodes = []
		#Number of nodes
		self.nnodes = 0
		#Name
		self.name = "Unnamed"
		#Number of Edges
		self.nedges = 0


	def createWeightedGraph(self, file, name = "Unnamed"):
		"""Used to create a weighed graph given the file name of the stored graph
		and also the name of the graph as an optinal parameter
		"""
		self.type = 1 # """Weighted Graph"""
		with open(file) as f:
			for line in f:
				self.m.append(map(int, line.split()))
		self.mt = [[row[i] for row in self.m] for i in range(3)]#"""Matrix Transpose"""		
		self.gwt = sum(self.mt[1]) # graph weight sum
		self.nodes= set(self.mt[0]).union(self.mt[2])
		self.lnodes = list(self.nodes)
		self.nnodes = len(self.lnodes)
		self.name = name
		self.nedges = len(self.m)
#		print "Graph Created"

	def createGraph(self, file, name = "Unnamed"):
		"""Used to create a weighed graph given the file name of the stored graph
		and also the name of the graph as an optinal parameter
		"""
		self.type = 0 # """UnWeighted Graph"""
		with open(file) as f:
			for line in f:
				self.m.append(map(int, line.split()))
		self.mt = [[row[i] for row in self.m] for i in range(2)]#"""Matrix Transpose"""		
		self.gwt = 0
		self.nodes= set(self.mt[0]).union(self.mt[1])
		self.lnodes = list(self.nodes)
		self.nnodes = len(self.lnodes)
		self.name = name
		self.nedges = len(self.m)
#		print "Unweighted Graph Created"

	def __repr__(self):
		"""Displays the meta data of the graph"""
		print "<GraphObject>"
		print "Name of the Graph: ",self.name
		print "Type: ",self.tname[self.type]
		print "Number of Nodes:",self.nnodes
		print "Number of Edges:",self.nedges
		return "\b"

	def __str__(self):
		"""Display the meta data of the graph"""
		print "<GraphObject>"
		print "Name of the Graph: ",self.name
		print "Type: ",self.tname[self.type]
		print "Number of Nodes:",self.nnodes
		print "Number of Edges:",self.nedges
		return "\b"

	def __len__(self):
		"""Number of nodes will be returned"""
		return self.nnodes
	def clean(self): #Same as reinitiaziling
		"""Clean the graph and reinitialze a Null graph
		"""
		self.type=0
		self.tname = ["Unweighted","Weighted"]
		#"""Matrix"""
		self.m = []
		#"""Matrix Transpose"""
		self.mt = []
		#Set of all the nodes
		self.nodes = set()
		#List of all the nodes
		self.lnodes = []
		#Number of nodes
		self.nnodes = 0
		#Name
		self.name = "Unnamed"
		#Number of Edges
		self.nedges = 0


#Driver Tests
filename = raw_input("Enter the Name of the File : ")
g  =  Graph()
g.createGraph(filename,"Karate")
print g
help(g)
print len(g)
g.clean()
print g
print len(g)
