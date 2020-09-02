import RPi.GPIO as GPIO  # 导入模块
import time

# L298N

GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
pin26_in1 = 26;
pin19_in2 = 19;
pin13_ena = 13;
GPIO.setup(pin26_in1, GPIO.OUT)
GPIO.setup(pin19_in2, GPIO.OUT)

GPIO.setup(pin13_ena, GPIO.OUT)
pwm = GPIO.PWM(pin13_ena, 500)
try:
    pwm.start(100)
    while True:
        GPIO.output(pin26_in1, True)
        GPIO.output(pin19_in2, False)
        time.sleep(2)
        duty = input("输入(0 - 100): ")
        pwm.ChangeDutyCycle(int(duty))
finally:
    GPIO.cleanup()  # 程序异常 清除引脚上的电平 防止下次使用时, 出现意外
    print("GPIO.cleanup()")
