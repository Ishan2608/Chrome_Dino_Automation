import pyautogui
from PIL import ImageGrab
import time


def check_for_dark_theme(img_data):
    for i in range(70, 100):
        for j in range(505, 515):
            if img_data[i, j] < 50:
                return True
            else:
                return False


def dodge(img_data, mode):
    if mode == 'dark':

        for i in range(190, 325):
            for j in range(431, 440):
                if img_data[i, j] > 170:
                    pyautogui.keyDown('up')
                    return

    elif mode == 'light':

        for i in range(190, 325):
            for j in range(431, 440):
                if 170 < img_data[i, j] < 200:
                    pyautogui.keyDown('up')
                    return


time.sleep(3)
pyautogui.keyDown('up')

while True:

    image = ImageGrab.grab().convert('L')
    image_data = image.load()

    dark_theme = check_for_dark_theme(img_data=image_data)

    if dark_theme:
        mode = 'dark'
        dodge(img_data=image_data, mode=mode)
    else:
        mode = 'light'
        dodge(img_data=image_data, mode=mode)

image.show()
