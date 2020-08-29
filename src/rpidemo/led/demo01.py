import RPi.GPIO as GPIO  # 导入模块
GPIO.setmode(GPIO.BCM)  # 设置gpio引脚编号编码(BCM, BOARD) gpio.jpg
GPIO.setup(18, GPIO.OUT)  # 18号引脚设置为输出
try:
    GPIO.output(18, True)  # 18号引脚高电平
finally:
    GPIO.cleanup()  # 程序异常 清除引脚上的电平 防止下次使用时, 出现意外
    print("GPIO.cleanup()")
