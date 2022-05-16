import pyautogui
import random
import time
from pynput.mouse import Button, Controller
mouse = Controller()
x = pyautogui.displayMousePosition()

print(x)

# # # open txt file and read the lines
# # # fname_object = open('email.txt', 'r')
# # # fname_list = fname_object.readlines()

# # # print(fname_list[3])
# a = pyautogui.locateCenterOnScreen('new.png', confidence=0.9)
# while a == None:
#     print('not found')
#     mouse.scroll(1,-10)
#     time.sleep(1)
#     a = pyautogui.locateCenterOnScreen('new.png', confidence=0.9)


# else:
#     b = pyautogui.click(a)