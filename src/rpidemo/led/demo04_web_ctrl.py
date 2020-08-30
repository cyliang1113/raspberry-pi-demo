from bottle import route, run, static_file

@route('/')
def page():
    return static_file("home.html", root='./demo04_web_ctrl_html/')

run(host='0.0.0.0', port=8080)