import keyboard
import pyautogui
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


sizex, sizey = pyautogui.size()
print("Screen size: " + str(sizex) + "x" + str(sizey))
print()
keyboard.wait('p')

x, y = pyautogui.position()
cargo = pyautogui.screenshot(region=(x, y, 300, 300))
cargo.save("screenshot/cargo.png")

img = cv2.imread("screenshot/cargo.png", cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2), interpolation=cv2.INTER_CUBIC)
retval, result = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("screenshot/result.png", result)

print(pytesseract.image_to_string('screenshot\\result.png'))