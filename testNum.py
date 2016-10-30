#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

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

# 定义按钮输入的GPIO口
btn = 27

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT1, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT2, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT3, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT4, RPi.GPIO.OUT)

RPi.GPIO.output(DIGIT1, False)
RPi.GPIO.output(DIGIT2, False)
RPi.GPIO.output(DIGIT3, False)
RPi.GPIO.output(DIGIT4, False)

RPi.GPIO.setup(btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showDigit(no, num, showDotPoint):
    # 先将正极拉低，关掉显示
    RPi.GPIO.output(DIGIT1, False)
    RPi.GPIO.output(DIGIT2, False)
    RPi.GPIO.output(DIGIT3, False)
    RPi.GPIO.output(DIGIT4, False)

    if (num == 0) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, True)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 1) :
        RPi.GPIO.output(LED_A, True)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, True)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, True)
        RPi.GPIO.output(LED_G, True)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 2) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, True)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_F, True)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 3) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, True)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 4) :
        RPi.GPIO.output(LED_A, True)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, True)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 5) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, True)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 6) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, True)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 7) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, True)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, True)
        RPi.GPIO.output(LED_G, True)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 8) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 9) :
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, True)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_DP, not showDotPoint)

    if (no == 1) :
        RPi.GPIO.output(DIGIT1, True)
    elif (no == 2) :
        RPi.GPIO.output(DIGIT2, True)
    elif (no == 3) :
        RPi.GPIO.output(DIGIT3, True)
    elif (no == 4) :
        RPi.GPIO.output(DIGIT4, True)

try:
    t=0.25

    for y in [1, 2, 3, 4]:
        for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for z in [True, False]:
                time.sleep(t)
                showDigit(y, x, z)

except KeyboardInterrupt:
    pass

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
RPi.GPIO.cleanup()