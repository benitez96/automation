#Module --> pip install pyautogui


# To stop a bug program move mouse cursor to top-left corner.
import pyautogui

# ========MOUSE METHODS===========

pyautogui.size()    #returns monitor pixels
width, height = pyautogui.size()
pyautogui.position()    # returns mouse's current position
pyautogui.moveTo(550, 266, duration=1.5)    # moves mouse
pyautogui.moveRel(200,-200, duration = 1)   
pyautogui.click(484,16) # Clicks on pixel
pyautogui.dragRel(200, 200, duration=1.2)   #drags pointer

pyautogui.displayMousePosition()    #shows current position in live -> must be run on console

#==========KEYBOARD METHODS===============

pyautogui.typewrite('Hello world!!', interval=0.5)
#makes click and write keys from the list
pyautogui.click(375,501); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X','Y'], interval=0.5)
# to seeing every key
pyautogui.KEYBOARD_KEYS
# to hotkeys
pyautogui.hotkey('ctrl', 'o')

#========SCREENSHOTS & IMAGE RECOGNITION==============

pyautogui.screenshot('screenshot.png')
pyautogui.locateOnScreen('example_img.png') #returns (x_pos, y_pos, width, height)
pyautogui.locateCenterOnScreen('example_img.png') #returns (x_pos, y_pos)