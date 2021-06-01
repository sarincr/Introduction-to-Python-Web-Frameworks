import cherrypy

class demoExample:
    def index(self):
        return "Hello World!!!"
    index.exposed = True
cherrypy.quickstart(demoExample())
