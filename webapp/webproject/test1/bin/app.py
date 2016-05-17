import web

urls = (
  '/', 'index', '/upload','Upload'
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
        filepath=x.myfile.filename.replace('\\','/')
        print filepath
        print x['myfile'].value
        print type(x['myfile'].value)
        print "I am here",x.myfile.filename
        
        return render.tmp()
    	

if __name__ == "__main__":
    app.run()
