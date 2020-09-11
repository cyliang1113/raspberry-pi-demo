#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
电动车前轮驱动
左右轮各有一个电机
"""
import RPi.GPIO as GPIO


class FWD(object):

    # 初始化, 输入引脚标号, GPIO.BCM模式
    def __init__(self, pin_left_motor_en, pin_left_motor_in1, pin_left_motor_in2,
                 pin_right_motor_en, pin_right_motor_in1, pin_right_motor_in2):
        self.__status = 0 # 状态 0-停止, 1-工作
        GPIO.setmode(GPIO.BCM)

        self.__pin_left_motor_en = pin_left_motor_en
        self.__pin_left_motor_in1 = pin_left_motor_in1
        self.__pin_left_motor_in2 = pin_left_motor_in2
        GPIO.setup(self.__pin_left_motor_en, GPIO.OUT)
        GPIO.setup(self.__pin_left_motor_in1, GPIO.OUT)
        GPIO.setup(self.__pin_left_motor_in2, GPIO.OUT)
        self.__pwd_left_motor_en = GPIO.PWM(self.__pin_left_motor_en, 500)

        self.__pin_right_motor_en = pin_right_motor_en
        self.__pin_right_motor_in1 = pin_right_motor_in1
        self.__pin_right_motor_in2 = pin_right_motor_in2
        GPIO.setup(self.__pin_right_motor_en, GPIO.OUT)
        GPIO.setup(self.__pin_right_motor_in1, GPIO.OUT)
        GPIO.setup(self.__pin_right_motor_in2, GPIO.OUT)
        self.__pwd_right_motor_en = GPIO.PWM(self.__pin_right_motor_en, 500)

    # 发动
    def launch(self):
        self.__status = 1
        self.__pwd_left_motor_en.start(0)
        self.__pwd_right_motor_en.start(0)

    # 向前
    def forward(self):
        self.__pwd_left_motor_en.ChangeDutyCycle(100)
        GPIO.output(self.__pin_left_motor_in1, True)
        GPIO.output(self.__pin_left_motor_in2, False)

        self.__pwd_right_motor_en.ChangeDutyCycle(100)
        GPIO.output(self.__pin_right_motor_in1, True)
        GPIO.output(self.__pin_right_motor_in2, False)

    # 向左
    def left(self):
        self.__pwd_left_motor_en.ChangeDutyCycle(0)
        GPIO.output(self.__pin_left_motor_in1, False)
        GPIO.output(self.__pin_left_motor_in2, False)

        self.__pwd_right_motor_en.ChangeDutyCycle(60)
        GPIO.output(self.__pin_right_motor_in1, True)
        GPIO.output(self.__pin_right_motor_in2, False)

    # 向右
    def right(self):
        self.__pwd_left_motor_en.ChangeDutyCycle(60)
        GPIO.output(self.__pin_left_motor_in1, True)
        GPIO.output(self.__pin_left_motor_in2, False)

        self.__pwd_right_motor_en.ChangeDutyCycle(0)
        GPIO.output(self.__pin_right_motor_in1, False)
        GPIO.output(self.__pin_right_motor_in2, False)

    # 刹车
    def brake(self):
        self.__pwd_left_motor_en.ChangeDutyCycle(100)
        GPIO.output(self.__pin_left_motor_in1, True)
        GPIO.output(self.__pin_left_motor_in2, True)

        self.__pwd_right_motor_en.ChangeDutyCycle(100)
        GPIO.output(self.__pin_right_motor_in1, True)
        GPIO.output(self.__pin_right_motor_in2, True)