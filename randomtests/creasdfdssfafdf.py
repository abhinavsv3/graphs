def createGraph(self, file):
        m=[] # original graph
        with open(file) as f:
            for line in f:
                m.append(map(int, line.split()))
        mt = [[row[i] for row in m] for i in range(2)]
        x = list(set(mt[0]).union(mt[1])) 
        #non repeating list of nodes
        #renumbering
        y = range(0,len(x))
        d = dict(zip(x,y))
        st = mt[0] = [d[i] for i in mt[0]]
        ds = mt[1] = [d[i] for i in mt[1]]
        wt = [1 for i in range(0,len(m[1]))]
        self.edges = zip(zip(st,ds),wt)
        self.nodes = y
        self.initialg()
 