from bottle import route, run, static_file
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
pin = 18  # 18号引脚
GPIO.setup(pin, GPIO.OUT)  # 18号引脚设置为输出
pwm = GPIO.PWM(pin, 500)  # 创建pwm 频率为500Hz 树莓派的pwm超过500Hz稳定性差
dutyValue = 50
d = 10
pwm.start(dutyValue)  # 开始脉冲, 占空比为0

def add():
    global dutyValue
    dutyValue = dutyValue + d
    if(dutyValue > 100):
        dutyValue = 100
    pwm.ChangeDutyCycle(dutyValue)

def minus():
    global dutyValue
    dutyValue = dutyValue - d
    if(dutyValue < 0):
        dutyValue = 0
    pwm.ChangeDutyCycle(dutyValue)

@route('/')
def page():
    return static_file("home.html", root='./demo04_web_ctrl_html/')

@route('/add')
def page():
    add()
    return static_file("home.html", root='./demo04_web_ctrl_html/')

@route('/minus')
def page():
    minus()
    return static_file("home.html", root='./demo04_web_ctrl_html/')

run(host='0.0.0.0', port=8080)