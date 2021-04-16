import pyautogui
import keyboard
import win32api
import cv2 
import numpy as np

from grabscreen import grab_screen

#https://www.ponggame.org/

# TODO - mark field on our own 
# TODO - constantly follow the balls y position 

#directly infront x = 1420
y_offset = 470
lower_hsv= np.array([0,0,50])
upper_hsv = np.array([255,255,255])


pyautogui.countdown(2)
while keyboard.is_pressed("q") == False:
    screen = grab_screen(region=(1420,482,1420,1038))
    # cv2.imshow("screen",screen)
    # cv2.waitKey(5)
    hsv = cv2.cvtColor(screen,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_hsv,upper_hsv)
    # cv2.imshow("mask",mask)
    # cv2.waitKey(5)

    matches = np.argwhere(mask==255)
    if len(matches)>0:
        mean_y = np.mean(matches[:,0])
        move = (1430,int(mean_y+y_offset))
        win32api.SetCursorPos(move)
        print(move)
    
