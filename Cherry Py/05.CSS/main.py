import cherrypy
import os


class application:
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            <p> Hello CSS.</p>
          </body>
        </html>"""


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.getcwd()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    cherrypy.quickstart(application(), '/', conf)
