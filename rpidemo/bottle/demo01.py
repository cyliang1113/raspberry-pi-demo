from bottle import route, run, template, static_file


@route('/')
def hello():
    return "Hello World!"


@route('/html/<filepath:path>')
def page(filepath):
    return static_file(filepath, root='./html/')


run(host='0.0.0.0', port=8080)
