#Driver Program
print "Please load the files in the directory for easy naming"
a = raw_input("Enter the file name : ")

g = louvaininpy()
fname = raw_input("Enter the file name :")
q = raw_input("Is it a weighted graph? y or n:")

if q == 'y':
	g.createWeightedGraph(fname)
else:
	g.createGraph(fname)