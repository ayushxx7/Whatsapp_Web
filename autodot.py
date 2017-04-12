import webbrowser
import pyautogui
import time
import random

'''
This code should be used to figure out pixel location of name box.
It will be different for every monitor, every window size, and also depends on extra messages
such as low battery that appear on Whatsapp Web.

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(216, 346)


'''

'''
To ensure that chrome is opened when alt tab is pressed, I open a new tab in chrome & close it.
'''

#sleep timing is dependent on machine performance, and expected lag in processing.

webbrowser.open("www.google.com",new=2,autoraise=True)
time.sleep(2)
pyautogui.hotkey('ctrl','f4')
pyautogui.hotkey('alt','tab')
#autoraise is working right now. after giving sleep time
'''
Right Now we are assuming that whatsapp web is open in tab 1 of the browser.
'''
for x in range(0,int(input("How many people are you going to autodot? "))):
    name = input('autodot who? ')
    count = int(input('how many lines of dot? '))
    max = int(input('how many max dots in each line? '))
    pyautogui.moveTo(206, 200) #hopefully reaches name box.
    #time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    #time.sleep(2)
    pyautogui.hotkey('ctrl', '1') #assuming whatsapp web is opened in tab 1.
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'a')
    #time.sleep(2)
    pyautogui.press('backspace')
    #time.sleep(2)
    pyautogui.typewrite(name)
    #pyautogui.moveTo(216, 346)
    pyautogui.press('enter')
    time.sleep(2)
    #pyautogui.click()
    #pyautogui.moveTo(776, 802)
    #pyautogui.click()
    for y in range(0,count):
        for z in range(random.randrange(1,max)):
            pyautogui.typewrite(".")
            time.sleep(0.02)
        pyautogui.press('enter')
        time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')

