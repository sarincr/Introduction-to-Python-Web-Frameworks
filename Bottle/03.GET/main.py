 
import os
from bottle import route, run, template

index_html = '''Hello {{ inX }}.'''



@route('/<name>')
def name(name):
    return template(index_html, inX=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
