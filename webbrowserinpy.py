import webbrowser as wb

def createWebFile(fname):
  f = open(fname,"w")  

  message = """
  <html>
  <head>
    <link rel="stylesheet" href="http://abhinavsv3.github.io/javascriptsal/alchemy.min.css"/>
  </head>
  <body>
    <div class="alchemy" id="alchemy"></div>  

    <script src="http://abhinavsv3.github.io/javascriptsal/alchemy.min1.js"></script>
    <script type="text/javascript">
       var config = {
              dataSource: 'http://abhinavsv3.github.io/jstest/data/roots.json',
           cluster: true, 
          clusterColours: ["#DD79FF", "#00FF30", "#5168FF", "#f83f00", "#ff8d8f"],
          forceLocked: false,
          nodeCaption: "title", 
          nodeMouseOver: 'title',
          directedEdges: true,
          edgeCaption: "relatedness",
          nodeCaptionsOnByDefault: """+"""false,
           nodesToggle: true,
          nodeTypes: {"type":["root","edge","node"]},
          directedEdges:true,
          nodeStyle: {
              "root": { 

                "borderColor": "#000000",
                      "borderWidth": function(d) {
                          return 10
                      },
                      "color": function(d) { 
                          return "rgba(104, 185, 254, " + 
                          (d.getProperties().sizes/5) + " )" 
                      },  

                  "radius": function(d){ return d.getProperties().sizes *1}
              } 

          }, 
          initialScale: 1, 
          initialTranslate: [250,150]
        } 

          alchemy = new Alchemy(config)
      </script>
    </body>
  </html>ext
  """
  f.write(message)
  f.close()

def showFile(fname):
  wb.open_new_tab(fname)

createWebFile("file3.html")
showFile("file3.html")