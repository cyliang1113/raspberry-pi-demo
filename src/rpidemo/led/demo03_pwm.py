import RPi.GPIO as GPIO  # 导入模块

GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
pin = 18  # 18号引脚
GPIO.setup(pin, GPIO.OUT)  # 18号引脚设置为输出
pwm = GPIO.PWM(pin, 500)  # 创建pwm 频率为500Hz 树莓派的pwm超过500Hz稳定性差

try:
    pwm.start(100)  # 开始脉冲, 占空比为100
    while True:
        duty = input("输入(0 - 100): ")
        pwm.ChangeDutyCycle(int(duty))
finally:
    GPIO.cleanup()  # 程序异常 清除引脚上的电平 防止下次使用时, 出现意外
    print("GPIO.cleanup()")