from bottle import route, run, template, static_file

@route('/')
def hello():
    return "Hello World!"

@route('/html/<path>')
def page(path):
    return static_file(path, root='./html/')

run(host='0.0.0.0', port=8080)
