import RPi.GPIO as GPIO  # 导入模块
import time

# L298N

GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
pin26_in1 = 26;
pin19_in2 = 19;
pin13_ena = 19;
GPIO.setup(pin26_in1, GPIO.OUT)
GPIO.setup(pin19_in2, GPIO.OUT)
GPIO.setup(pin13_ena, GPIO.OUT)
try:
    GPIO.output(pin13_ena, True)

    GPIO.output(pin26_in1, True)
    GPIO.output(pin19_in2, False)
    time.sleep(2)
    GPIO.output(pin26_in1, False)
    GPIO.output(pin19_in2, True)
    time.sleep(2)
finally:
    GPIO.cleanup()  # 程序异常 清除引脚上的电平 防止下次使用时, 出现意外
    print("GPIO.cleanup()")
