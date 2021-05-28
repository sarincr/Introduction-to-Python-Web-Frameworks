import os
from bottle import route, run, template

index_html = ''' Hello <strong>{{ author }}</strong>.'''


@route('/')
def index():
    return template(index_html, author='World')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='1.2.3.4', port=port, debug=True)
