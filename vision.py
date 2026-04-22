from pathlib import Path
import time
import keyboard
import pyautogui
import cv2
import numpy as np
import pytesseract
import requests
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Path("screenshot").mkdir(exist_ok=True)

type_ids = {
    "veldspar": 1230,
    "scordite": 1228,
    "pyroxeres": 1224
}

def load_prices():
    try:
        response = requests.get('https://esi.evetech.net/latest/markets/prices/?datasource=tranquility')
        response.raise_for_status()
        data = response.json()
        prices = {}
        for item in data:
            type_id = item['type_id']
            if type_id in type_ids.values():
                name = [k for k, v in type_ids.items() if v == type_id][0]
                prices[name] = item['adjusted_price']
        return prices
    except requests.RequestException as e:
        print(f"Error loading prices: {e}")
        return {}

capture_width = 200
capture_height = 30

# Загрузка цен с рынка
prices = load_prices()


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