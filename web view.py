import getpass
import webbrowser
import time

p = getpass.getpass(prompt='WHO IS KING OR OWNER OF UNIVERSE ')

if p.lower() == 'harshmghero':
    print('Welcome HARSH MG!!!')
    print('I am your servent bot for website view')
    a = input('Enter your URL: ')
    b = int(input('Enter the no. of views:  '))
    c= b *6;
    print("estimate views :",c)
    count = 0
    while count < b:
            webbrowser.open(a)
            time.sleep(0.1)
            webbrowser.open_new_tab(a)
            time.sleep(0.2)
            webbrowser.open_new_tab(a)
            time.sleep(0.2)
            webbrowser.open_new_tab(a)
            time.sleep(0.21)
            webbrowser.open_new_tab(a)
            time.sleep(0.2)
            webbrowser.open_new_tab(a)
            time.sleep(0.1)
            count = count + 1
            print('thank for using me !!!')
            print('Made by HARSH MG !!!')
else: 
    print('The passcode entered by you is incorrect..!!!')
    print('you ar not HARSH MG!!!')
    time.sleep(3) 
    
