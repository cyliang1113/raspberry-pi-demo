#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../")
from rpidemo.motor_car.motor_car_fwd import FWD
from bottle import route, run, static_file
import RPi.GPIO as GPIO

pin_left_motor_en = 13
pin_left_motor_in1 = 19
pin_left_motor_in2 = 26

pin_right_motor_en = 16
pin_right_motor_in1 = 20
pin_right_motor_in2 = 21

fwd = FWD(pin_left_motor_en, pin_left_motor_in1, pin_left_motor_in2,
          pin_right_motor_en, pin_right_motor_in1, pin_right_motor_in2)
fwd.launch()


@route('/')
def page():
    return static_file("home.html", root='./test04_web_ctrl_html/')


@route('/forward')
def page():
    global fwd
    fwd.forward()
    return "ok"


@route('/back')
def page():
    global fwd
    fwd.back()
    return "ok"


@route('/left')
def page():
    global fwd
    fwd.left()
    return "ok"


@route('/right')
def page():
    global fwd
    fwd.right()
    return "ok"


@route('/brake')
def page():
    global fwd
    fwd.brake()
    return "ok"

try:
    run(host='0.0.0.0', port=8080)
finally:
    GPIO.cleanup()
    print("GPIO.cleanup()")
