import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            Hello HTML
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self):
        return "hello Pages"

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
