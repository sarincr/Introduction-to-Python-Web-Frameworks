from bottle import route, run, static_file

@route('/')
def serve_homepage():
    return static_file('home.html', root='static/')

run(host='localhost', port=8080)
