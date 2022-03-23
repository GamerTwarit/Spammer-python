import pyautogui as spam
import time
time.sleep(2)
print('''welcome to spam-PyAutoGUI 



.to end this you will have to take the cursor to bottom right or left corner of the screen



Made by GamerTwarit
with PyAutoGUI


 ''')
input("press enter to start ")

A = input("type the text you want to spam ")
print("your text will look like", A)
input("press enter to start")
while True:
    spam.typewrite(A)
    spam.press("enter")
	
    