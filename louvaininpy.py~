class louvaininpy:
    '''
    Creating graph from a file
    '''
    def createWeightedGraph(self, file):
        print "Loading the graph"
        m=[] # original graph
        with open(file) as f:
            for line in f:
                m.append(map(int, line.split()))
        mt = [[row[i] for row in m] for i in range(3)]
        x = list(set(mt[0]).union(mt[2])) 
        #non repeating list of nodes
        #renumbering 
	#Formatof number representation in the matrix:
	#"start weight destination"
        y = range(0,len(x))
        d = dict(zip(x,y))
        print "Loading Complete, Rearraging"
        st = mt[0] = [d[i] for i in mt[0]]
        ds = mt[2] = [d[i] for i in mt[2]]
        wt = mt[1]
        self.start = st
        self.dest = ds
        self.wgt = wt
        self.length = len(st)
        self.edges = zip(zip(st,ds),wt)
        self.nodes = y
        self.initialg()
    '''
    Initializing the graph into the object
    '''
    def initialg(self):
    	print "Setting Initials"
        nodes = self.nodes
        edges = self.edges
        self.m = 0
        self.e_sum = [0 for n in nodes]
        self.edges_of_node = {}
        self.w = [0 for n in nodes]
        for e in edges:
            self.m += e[1]
            self.e_sum[e[0][0]] += e[1]
            self.e_sum[e[0][1]] += e[1] # there's no self-loop initially
            # save edges by node
            if e[0][0] not in self.edges_of_node:
                self.edges_of_node[e[0][0]] = [e]
            else:
                self.edges_of_node[e[0][0]].append(e)
            if e[0][1] not in self.edges_of_node:
                self.edges_of_node[e[0][1]] = [e]
            elif e[0][0] != e[0][1]:
                self.edges_of_node[e[0][1]].append(e)
        # access community of a node in O(1) time
        self.communities = [n for n in nodes] #copying list
        self.actual_partition = []

    def louvain(self):
    	print "In louvain"
        network = (self.nodes, self.edges)
        best_partition = [[node] for node in network[0]]
        best_q = -1
        i = 1
        while 1:
            ###print("pass #%d" % i)
            i += 1
            partition = self.first_phase(network)
            q = self.modularity_calc(partition)
            partition = [c for c in partition if c]
            ###print("%s (%.8f)" % (partition, q))
            # clustering initial nodes with partition
            if self.actual_partition:
                actual = []
                for p in partition:
                    part = []
                    for n in p:
                        part.extend(self.actual_partition[n])
                    actual.append(part)
                self.actual_partition = actual
            else:
                self.actual_partition = partition
            if q == best_q:
                break
            network = self.second_phase(network, partition)
            best_partition = partition
            best_q = q
        return (self.actual_partition, best_q)

    '''
    Modularity function
    '''
    def modularity_calc(self, partition):
        q = 0
        m2 = self.m * 2
        for i in range(len(partition)):
            q += self.s_in[i] / m2 - (self.s_tot[i] / m2) ** 2
        return q

    '''
        Modularity Gain
        _node: an int
        _c: an int
        _e_sum_in: the sum of the weights of the links from _node to nodes in _c
    '''
    def modularity_calc_gain(self, node, c, e_sum_in):
        return 2 * e_sum_in - self.s_tot[c] * self.e_sum[node] / self.m

    '''
       Phase 1
        _network: a (nodes, edges) pair
    '''
    def first_phase(self, network):
        # make initial partition
        print "Phase 1"
        best_partition = self.make_initial_partition(network)
        while 1:
            improvement = 0
            for node in network[0]:
                node_community = self.communities[node]
                # default best community is its own
                best_community = node_community
                best_gain = 0
                # remove _node from its community
                best_partition[node_community].remove(node)
                best_shared_links = 0
                for e in self.edges_of_node[node]:
                    if e[0][0] == e[0][1]:
                        continue
                    if e[0][0] == node and self.communities[e[0][1]] == node_community or e[0][1] == node and self.communities[e[0][0]] == node_community:
                        best_shared_links += e[1]
                self.s_in[node_community] -= 2 * (best_shared_links + self.w[node])
                self.s_tot[node_community] -= self.e_sum[node]
                self.communities[node] = -1
                communities = {} # only consider neighbors of different communities
                for neighbor in self.get_neighbors(node):
                    community = self.communities[neighbor]
                    if community in communities:
                        continue
                    communities[community] = 1
                    shared_links = 0
                    for e in self.edges_of_node[node]:
                        if e[0][0] == e[0][1]:
                            continue
                        if e[0][0] == node and self.communities[e[0][1]] == community or e[0][1] == node and self.communities[e[0][0]] == community:
                            shared_links += e[1]
                    # compute modularity gain obtained by moving _node to the community of _neighbor
                    gain = self.modularity_calc_gain(node, community, shared_links)
                    if gain > best_gain:
                        best_community = community
                        best_gain = gain
                        best_shared_links = shared_links
                # insert _node into the community maximizing the modularity gain
                best_partition[best_community].append(node)
                self.communities[node] = best_community
                self.s_in[best_community] += 2 * (best_shared_links + self.w[node])
                self.s_tot[best_community] += self.e_sum[node]
                if node_community != best_community:
                    improvement = 1
            if not improvement:
                break
        return best_partition

    '''
        Next node
        _node: an int
    '''
    def get_neighbors(self, node):
        for e in self.edges_of_node[node]:
            if e[0][0] == e[0][1]:
                continue
            if e[0][0] == node:
                yield e[0][1]
            if e[0][1] == node:
                yield e[0][0]

    '''
        Initial Partition
        _network: a (nodes, edges) pair
    '''
    def make_initial_partition(self, network):
    	print "Initial Partition"
        partition = [[node] for node in network[0]]
        self.s_in = [0 for node in network[0]]
        self.s_tot = [self.e_sum[node] for node in network[0]]
        print "Loading the network.. this will take some time"
        for e in network[1]:
            if e[0][0] == e[0][1]: # only self-loops
                self.s_in[e[0][0]] += e[1]
                self.s_in[e[0][1]] += e[1]
             #   print "If statement"
            print  "Loading .. ", e
        return partition
        print "Initial Partition done"

    '''
        Phase 2
        _network: a (nodes, edges) pair
        _partition: a list of lists of nodes
    '''
    def second_phase(self, network, partition):
    	print "Phase 2"
        nodes_ = [i for i in range(len(partition))]
        # relabelling communities
        communities_ = []
        d = {}
        i = 0
        for community in self.communities:
            if community in d:
                communities_.append(d[community])
            else:
                d[community] = i
                communities_.append(i)
                i += 1
        self.communities = communities_
        # building relabelled edges
        edges_ = {}
        for e in network[1]:
            ci = self.communities[e[0][0]]
            cj = self.communities[e[0][1]]
            try:
                edges_[(ci, cj)] += e[1]
            except KeyError:
                edges_[(ci, cj)] = e[1]
        edges_ = [(k, v) for k, v in edges_.items()]
        # recomputing e_sum vector and storing edges by node
        self.e_sum = [0 for n in nodes_]
        self.edges_of_node = {}
        self.w = [0 for n in nodes_]
        for e in edges_:
            self.e_sum[e[0][0]] += e[1]
            self.e_sum[e[0][1]] += e[1]
            if e[0][0] == e[0][1]:
                self.w[e[0][0]] += e[1]
            if e[0][0] not in self.edges_of_node:
                self.edges_of_node[e[0][0]] = [e]
            else:
                self.edges_of_node[e[0][0]].append(e)
            if e[0][1] not in self.edges_of_node:
                self.edges_of_node[e[0][1]] = [e]
            elif e[0][0] != e[0][1]:
                self.edges_of_node[e[0][1]].append(e)
        # resetting communities
        self.communities = [n for n in nodes_]
        return (nodes_, edges_)

    def createGraph(self,file):
        m = []
        print "Loading the graph"
        with open(file) as f:
            for line in f:
                m.append(map(int, line.split()))
        #print m
        mt = [[row[i] for row in m] for i in range(2)]
        x = list(set(mt[0]).union(mt[1]))
        print "Loading Complete, Rearraging"
        y = range(0,len(x))
        d = dict(zip(x,y))
        st = mt[0] = [d[i] for i in mt[0]]
        ds = mt[1] = [d[i] for i in mt[1]]
        #print "MT ", mt[1], len(mt[1])
        wt = [1 for i in range(0,len(mt[1]))]
        #print "Wt", wt
        self.start = st
        self.dest = ds
        self.wgt = wt
        self.length = len(st)
        self.edges = zip(zip(st,ds),wt)
        self.nodes = y
        self.initialg()
 

"""
g = louvaininpy()
fname = raw_input("Enter the file name :")
q = raw_input("Is it a weighted graph? y or n:")
print "Initizlizing"
if q == 'y':
	g.createWeightedGraph(fname)
else:
	g.createGraph(fname)
partition, q= g.louvain()
print partition,q
"""
