import pyautogui
import time
import cv2
import numpy as np
import keyboard
import sys

# 关闭pyautogui的鼠标从边缘移动检测
pyautogui.FAILSAFE = False
# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()
# 计算目标图像缩放尺寸
resized_width = int(116 * screen_width / 3840)
# 计算一键点血网位置
skip = (int(1362 * screen_width / 3840), int(1143 * screen_width / 3840))


# pyautogui的click无法直接点血网，故用长按0.1秒替代
def click():
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def click_target(target):
    # 移动鼠标至左下角
    pyautogui.moveTo(0, screen_height)
    while True:
        # 截图并转换为灰度图像
        screenshot = pyautogui.screenshot()
        gray_screenshot = cv2.cvtColor(cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        # 将目标图像缩放尺寸并转换为灰度图像
        resized_target = cv2.resize(target, (resized_width, resized_width), interpolation=cv2.INTER_AREA)
        gray_resized_target = cv2.cvtColor(cv2.cvtColor(resized_target, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

        # 使用模板匹配
        result = cv2.matchTemplate(gray_screenshot, gray_resized_target, cv2.TM_CCOEFF_NORMED)
        # 获取匹配位置，依次为——最低匹配度，最高匹配度，最低匹配度坐标，最高匹配度坐标
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 匹配度判断<0.6则认为目标不存在
        if max_val < 0.6:
            pyautogui.moveTo(skip)
            click()
            time.sleep(0.1)
            pyautogui.moveTo(0, screen_height)
            time.sleep(8)
        else:
            target_center = (max_loc[0] + resized_target.shape[1] // 2,
                             max_loc[1] + resized_target.shape[0] // 2)
            pyautogui.moveTo(target_center)
            click()
            time.sleep(0.1)
            pyautogui.moveTo(0, screen_height)
            time.sleep(3)


# 检测按esc退出程序
def detect_keyboard():
    while True:
        if keyboard.is_pressed('esc'):
            sys.exit()
