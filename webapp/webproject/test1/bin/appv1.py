import web
import louvaininpy as l
import jsoninpy
import spliterinpy as spl

urls = (
  '/', 'index', '/upload','Upload','/jsons'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = ""
        print "In Here"
        return render.index()
    
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
    	print form.greet
    	fn = form.myfile
        x = web.input(myfile={})
        print x['myfile'],type(x['myfile'])
        print x['myfile'].value
        print x['myfile'].file
        print type(x['myfile'].file)
        print type(x['myfile'].file.read())
        g = l.louvaininpy()
        if form.weighted == "Yep":
            g.sCreateWeightedGraph(x['myfile'].value)
        else:
            g.sCreateGraph(x['myfile'].value)

        partition, q= g.louvain()
        print partition,q

        #roots

        r = spl.splitroot(g,partition)
        r.jsonDump("rjson.json")
        print "JSON Created"

        #if form.weighted == "Yep":

        """
        g = l.louvaininpy()
        
        q = raw_input("Is it a weighted graph? y or n:")
        print "Initizlizing"
        if q == 'y':
            g.createWeightedGraph(fname)
        else:
            g.createGraph(fname)
        partition, q= g.louvain()
        print partition
        lenp = len(partition)
        roots = zip([i for i in range(len(partition))],[len(i) for i in partition])
        y = 0
        d = {} 
        # d tells the group of the node
        for i in partition:
            for j in i:
                d[j] = y
            y = y + 1
        print d
        
        print roots[0][0]"""
        return render.tmp()
    	

if __name__ == "__main__":
    app.run()
