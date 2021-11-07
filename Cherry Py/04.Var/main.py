import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)

cherrypy.quickstart(HelloWorld())
