import pyautogui
import keyboard
import win32api,win32con
import time

#TODO - select 4 rows before


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("starting")
time.sleep(2)

while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(1080,850)[0] ==0:
        click(1080,850)
    if pyautogui.pixel(1211,850)[0] ==0:
        click(1211,850)
    if pyautogui.pixel(1334,850)[0] ==0:
        click(1334,850)
    if pyautogui.pixel(1450,850)[0] ==0:
        click(1450,850)
print("finishing")