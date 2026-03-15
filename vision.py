import keyboard
import pyautogui
import cv2
import numpy as np
sizex, sizey = pyautogui.size()
print("Screen size: " + str(sizex) + "x" + str(sizey))
print()
keyboard.wait('p')

x, y = pyautogui.position()
cargo = pyautogui.screenshot(region=(x, y, 300, 300))
cargo.save("screenshot/cargo.png")

img = cv2.imread("screenshot/cargo.png", cv2.IMREAD_GRAYSCALE)
 
retval, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite("screenshot/result.png", result)