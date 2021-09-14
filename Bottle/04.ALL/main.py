
import bottle

@bottle.route('/') 
def index():
  return 'You can write html here'  

@bottle.route('/static_page')
def static_page():
  return bottle.static_file('page.html',root="static") 
  

@bottle.route('/input/<name>')
def input(name):
  return 'Hello '+name 
@bottle.post('/post_request_only')
def post_request_only():
  return 'Post request succesful'

@bottle.error(404)
def error404(error):
  return("oops! the page you were looked for isn't here. <a href='/'>Return Home?</a>")

bottle.run(host='0.0.0.0', port=1234) 