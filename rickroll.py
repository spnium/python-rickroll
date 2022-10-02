import webbrowser
import time
from pyautogui import *
import pyautogui

for _ in range(100):
    time.sleep(4.5)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', autoraise=True)
    play_button = locateCenterOnScreen('playbotton.png', confidence=0.88, grayscale=True)
    while True:
        if play_button == None:
            play_button = locateOnScreen('playbotton.png', confidence=0.88, grayscale=True)
        else:
            break
    pyautogui.click(play_button)