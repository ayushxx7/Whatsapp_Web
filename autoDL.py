import pyautogui
import time
import shutil
import glob
import os


#disclaimer: pixel location will vary for each new machine and browser config(including resizing) [first figure out pixel locations of the buttons], 
#so will SaveAs.png [take your own ss and replace the existing file.]
cnt = int(input('How many images to DL? '))
x = input('Directory Name? ')
pre = input('Prefix for files? ')
pyautogui.hotkey('alt','tab')  #assuming you alt+tab swtiched to the program runner(such as CMD/PyCharm) directly 
							   #also it assumes you have opened up the first image from where you would like to start downloading.
pyautogui.moveTo(1488,114)
pyautogui.click()
time.sleep(1.5)

path = 'C:\Whatsapp DLs'+'\\'+str(x)
if not os.path.exists(path):
    os.mkdir(path)
pyautogui.hotkey('alt','d') #neat hun :P 
pyautogui.typewrite("C:\Whatsapp DLs"+"\\"+x)
pyautogui.press('enter')
a,b,c,d = pyautogui.locateOnScreen('SaveAs.png')
pyautogui.moveTo(a+581,b+430)
pyautogui.click()
#pyautogui.press('s')
time.sleep(3)
'''
test = '/'+path+'/*'
r = glob.glob(test)
for i in r:
   os.remove(i)

shutil.rmtree(path+'/')
'''
#pyautogui.hotkey('alt','tab')
for x in range(0,cnt):
    pyautogui.moveTo(1488,114)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.typewrite(pre+" "+str(x))
    time.sleep(0.8)
    pyautogui.press('enter')
    pyautogui.press('right')

