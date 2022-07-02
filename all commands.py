import pyautogui as pygui
import time

#safty
pygui.FAILSAFE = True

time.sleep(3)

#take a screenshot and save it 
#pygui.screenshot('1.png')

#print(pygui.locateOnScreen('1.png'))

#current mouse x and y
#print(pygui.position())

# current screen resolution width and height
#print(pygui.size())

'''
mouse control

'''

x=908
y=808

# move mouse to XY coordinates over num_second seconds
#pygui.moveTo(x, y, duration=5)

# drag mouse to XY
#pygui.dragTo(x, y, duration=5)

#The button keyword argument can be 'left', 'middle', or 'right'.
#pygui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')



#pyautogui.rightClick(x=moveToX, y=moveToY)
#pyautogui.middleClick(x=moveToX, y=moveToY)
#pyautogui.doubleClick(x=moveToX, y=moveToY)
#pyautogui.tripleClick(x=moveToX, y=moveToY)

#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)

'''
Keyboard controls

'''

# useful for entering text, newline is Enter
#pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

#pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
#pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste


'''
#pyautogui.alert('This displays some text with an OK button.')
#pyautogui.confirm('This displays text and has an OK and Cancel button.')
'OK'
#pyautogui.prompt('This lets the user type in a string and press OK.')
'This is what I typed in.'
'''

