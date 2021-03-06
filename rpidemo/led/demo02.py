import RPi.GPIO as GPIO  # 导入模块
import time



GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
pin = 18  # 18号引脚
GPIO.setup(pin, GPIO.OUT)  # 引脚设置为输出

try:
    for i in range(10):
        GPIO.output(pin, True)  # 18号引脚高电平
        time.sleep(0.5)
        GPIO.output(pin, False)
        time.sleep(0.5)
finally:
    GPIO.cleanup()  # 程序异常 清除引脚上的电平 防止下次使用时, 出现意外
    print("GPIO.cleanup()")
