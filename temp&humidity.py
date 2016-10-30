#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

BCM = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(BCM, GPIO.IN)

# 定义单个数码管各段led对应的GPIO口
LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 11
LED_G = 9
LED_DP = 10

# 定义1到4号数码管阳极对应的GPIO口
DIGIT1 = 12
DIGIT2 = 16
DIGIT3 = 20
DIGIT4 = 21

# 定义温湿度输入的GPIO口
TH = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(LED_C, GPIO.OUT)
GPIO.setup(LED_D, GPIO.OUT)
GPIO.setup(LED_E, GPIO.OUT)
GPIO.setup(LED_F, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_DP, GPIO.OUT)
GPIO.setup(DIGIT1, GPIO.OUT)
GPIO.setup(DIGIT2, GPIO.OUT)
GPIO.setup(DIGIT3, GPIO.OUT)
GPIO.setup(DIGIT4, GPIO.OUT)

GPIO.setup(TH, GPIO.IN)

GPIO.output(DIGIT1, True)
GPIO.output(DIGIT2, True)
GPIO.output(DIGIT3, True)
GPIO.output(DIGIT4, True)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showDigit(no, num, showDotPoint):
	# 先将正极拉低，关掉显示
	GPIO.output(DIGIT1, False)
	GPIO.output(DIGIT2, False)
	GPIO.output(DIGIT3, False)
	GPIO.output(DIGIT4, False)

	GPIO.output(LED_A, True)
	GPIO.output(LED_B, True)
	GPIO.output(LED_C, True)
	GPIO.output(LED_D, True)
	GPIO.output(LED_E, True)
	GPIO.output(LED_F, True)
	GPIO.output(LED_G, True)

	if (num == 0) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, False)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, True)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 1) :
		GPIO.output(LED_A, True)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, True)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, True)
		GPIO.output(LED_G, True)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 2) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, True)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, False)
		GPIO.output(LED_F, True)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 3) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, True)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 4) :
		GPIO.output(LED_A, True)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, True)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 5) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, True)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 6) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, True)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, False)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 7) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, True)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, True)
		GPIO.output(LED_G, True)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 8) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, False)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (num == 9) :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, False)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)

	if (no == 1) :
		GPIO.output(DIGIT1, True)
	elif (no == 2) :
		GPIO.output(DIGIT2, True)
	elif (no == 3) :
		GPIO.output(DIGIT3, True)
	elif (no == 4) :
		GPIO.output(DIGIT4, True)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showLetter(no, Letter, showDotPoint):

	if (Letter == 'o') :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, False)
		GPIO.output(LED_C, True)
		GPIO.output(LED_D, True)
		GPIO.output(LED_E, True)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, False)
		GPIO.output(LED_DP, not showDotPoint)
	elif (Letter == 'C') :
		GPIO.output(LED_A, False)
		GPIO.output(LED_B, True)
		GPIO.output(LED_C, True)
		GPIO.output(LED_D, False)
		GPIO.output(LED_E, False)
		GPIO.output(LED_F, False)
		GPIO.output(LED_G, True)
		GPIO.output(LED_DP, not showDotPoint)

	if (no == 1) :
		GPIO.output(DIGIT1, True)
	elif (no == 2) :
		GPIO.output(DIGIT2, True)
	elif (no == 3) :
		GPIO.output(DIGIT3, True)
	elif (no == 4) :
		GPIO.output(DIGIT4, True)


try:
    t=0.005
    while True:
        # 按钮按下时显示日期，否则显示时间
        # 为了区别左右的数字，让第二个数码管的小数点显示出来
        #（本来应该是一个冒号，我们这个数码管没有，就用小数点代替了）
        
        time.sleep(t)
        showDigit(1, 2, False)
        time.sleep(t)
        showDigit(2, 9, False)
        time.sleep(t)
        showLetter(3, 'o', False)
        time.sleep(t)
        showLetter(4, 'C', False)

except KeyboardInterrupt:
    pass

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
GPIO.cleanup()