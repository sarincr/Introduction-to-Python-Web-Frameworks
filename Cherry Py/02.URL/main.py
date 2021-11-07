
import cherrypy

class HelloWorld():
    def index(self):
        return "Hello World!"
    index.exposed = True

    @cherrypy.expose
    def test(self):
        return "Test Controller"
cherrypy.quickstart(HelloWorld())
