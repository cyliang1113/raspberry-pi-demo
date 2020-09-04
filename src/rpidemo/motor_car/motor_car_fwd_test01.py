#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .motor_car_fwd import FWD
import time

pin_left_motor_en = 13
pin_left_motor_in1 = 19
pin_left_motor_in2 = 26

pin_right_motor_en = 16
pin_right_motor_in1 = 20
pin_right_motor_in2 = 21

fwd = FWD(pin_left_motor_en, pin_left_motor_in1, pin_left_motor_in2,
          pin_right_motor_en, pin_left_motor_in1, pin_right_motor_in2)
fwd.launch()
fwd.forward()
time.sleep(2)