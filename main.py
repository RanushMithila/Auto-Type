import pyautogui as spam
import time

#safety
spam.FAILSAFE = True

limit = 889
msg = "You are a "

x = 0
time.sleep(3)

txt = open('animal.txt', 'r')

for i in txt:
    spam.typewrite(msg + i)
    spam.press('Enter')
    x+=1
    if (x > limit):
        break
