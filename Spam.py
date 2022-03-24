import pyautogui as spam
import time
time.sleep(2)
 BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'
print(BLUE +'''    welcome to spam-PyAutoGUI 



         .to end this you will have to take the cursor to bottom right or left corner of the screen



         Made by GamerTwarit
            with PyAutoGUI


 ''')
input("press enter to start ")

A = input(GREEN + "type the text you want to spam ")
print("your text will look like", A)
input("press enter to start")
while True:
    spam.typewrite(A)
    spam.press("enter")
	
    
