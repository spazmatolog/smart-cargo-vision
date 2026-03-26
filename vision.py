from pathlib import Path
import time
import keyboard
import pyautogui
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Path("screenshot").mkdir(exist_ok=True)

capture_width = 200
capture_height = 30

# цены на руды чегоо
prices = {
    "veldspar": 12.5,
    "scordite": 15.0,
    "pyroxeres": 45.0
}


sizex, sizey = pyautogui.size()
print("Screen size: " + str(sizex) + "x" + str(sizey))
print()
while True:
    if keyboard.is_pressed('p'):

        x, y = pyautogui.position()
        cargo = pyautogui.screenshot(region=(x, y, capture_width, capture_height))
        cargo.save("screenshot/cargo.png")


        img = cv2.imread("screenshot/cargo.png", cv2.IMREAD_GRAYSCALE)

        img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2), interpolation=cv2.INTER_CUBIC)
        retval, result = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

        cv2.imwrite("screenshot/result.png", result)

        textresult = pytesseract.image_to_string("screenshot/result.png")
        textresult = textresult.strip().lower()
        print(repr(textresult))
        
        time.sleep(0.3)

        if textresult in prices:
            print("Price: " + str(prices[textresult]) + " ISK/m3")

    elif keyboard.is_pressed(']'):
        break
    time.sleep(0.05)
