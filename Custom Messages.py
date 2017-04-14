import pyautogui
import time
import random

#path where contacts are stored.

path = 'C:\Contacts\\'
N = path+'UseThis'

f = open(N+'.txt','r')


l1 =['I wish the electrons from the valence band get sufficient energy to jump the forbidden energy gap and reach conduction band ,so that in the presence of external electric field ,the electrons move and conduct electricity so that ur home lights up with happiness n joy. Wish You and your Family a very happy and prosperous Diwali',
     ' Diwali ki hardik shubhkamnaye Maa mahalakshmi ap par or apke privar par apni asim kripa drishti banaye rakhe ',
     'i wish that the spark you create takes the oil in the wick to the temperature enough to cause combustion and create the divine flames that light up your house with happiness and joy. Wish u and your family a happy diwali',
     'Wishing you and your family a very HAPPY DEEPAWALI. May this year brings prosperity and happiness with blessings of goddess LAXMI',
     'Deepak ka prakash har pal aapke jivan me ek nayi roshni de, Bas yehi shubhkamna hai hamari aapke liye diwali ke is paawan avsar par, Happy Choti Deepavali!!!',
     'THIS DIWALI MAY YOU BE BLESSED WITH GOOD FORTUNE AS LONG AS GANESHJIS TRUNK, WEALTH & PROSPERITY AS BIG AS HIS STOMACH, HAPPINESS AS SWEET AS HIS LADOOS & MAY YOUR TROUBLE BE AS SMALL AS HIS HIS MOUSE   & MANY MORE WISHES TO U SHARE YOUR HAPPINESS WITH PEOPLES AS MUCH AS YOU CAN, MAY GOD BLESS YOU, KEEP SMILING & HELP TO KEEP KEEP CITY CLEAN  WISH U VERY HAPPY DIWALI TO YOU AND YOUR FAMILY ..',
     'Adorn our lives else trite With sparklers that motley skies As soaring spirits of powder wander Let us thank the heavenly might, In this festive season of lights. Happy Diwali!!!',
     'Diwali night is full of lights, may your life be filled with colors and lights of happiness. Happy Diwal']

l2 = ['umeed hai bohot maze kiye honge tune aaj, aur dusron ki naak me dam bhi kiya hoga khoob ','kitne bam fode? aur kitne bam fodne valon ko foda aaj tune ',
      'kitno ke ghar jalaye aur kitno ke kaan ke parde faad diye tune aaj ']

pyautogui.hotkey('alt','tab') #switch to whatsapp web. [see at the end wtf this is if u don't get it]

for i in f.read().splitlines():
    #print(i+' - '+str(cnt))
    #print(i.split()[0])
    na = i.split()[0]

    #while cnt!=4:
    z = random.randrange(1, 9) #random text from list 1
    z2 = random.randrange(0,3) #random text from list 2
    #z3 = random.randrange(0,8) #random image from a group images stored in the pc
    
    #pyautogui.typewrite(i)
    #time.sleep(0.5)

    pyautogui.moveTo(206, 200)  #this is where name box in whatsapp web is. (for my config)
    # time.sleep(2)
    #pyautogui.hotkey('alt', 'tab')
    # time.sleep(2)
    #pyautogui.hotkey('ctrl', '1')
    #time.sleep(1)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.hotkey('ctrl', 'a')
    # time.sleep(2)
    pyautogui.press('backspace')
    # time.sleep(2)
    pyautogui.typewrite(i)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.typewrite('I know you\'ve already seen this forwarded message a gazillion times but any ways'+'\n'+l1[z3])
    pyautogui.press('enter')
    pyautogui.typewrite(l2[z2]+' '+na)  #magic, name is typed here, giving personal touch.
    pyautogui.press('enter')
    
    '''

    This is for also sending images along with the text which is a given for any Diwali greeting on Whatsapp.
	Try and test different pixel locations before trying to implement this.    
    # pyautogui.moveTo(1466,131)
    # pyautogui.click()
    # pyautogui.moveTo(1466, 209)
    # pyautogui.click()
    # time.sleep(1.5)
    # pyautogui.typewrite(str(z)+'.jpg')
    # time.sleep(1.5)
    # pyautogui.press('enter')
    # time.sleep(1)
    # pyautogui.press('enter')
    # time.sleep(1.5)
	
	'''

