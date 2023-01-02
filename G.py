import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import os
import time
import sys

r="\x1b[91;1m"
g="\x1b[32;1m"
y="\x1b[33;1m"
p="\x1b[34;1m"
c="\x1b[36;1m"
o="\x1b[37;1m"
w="\x1b[00m"
u="\x1b[4m"
b="\x1b[5m"

def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

logo = """\x1b[32;1m
████████ ██   ██ ███████ ███    ███ ███████ 
   ██    ██   ██ ██      ████  ████ ██      
   ██    ███████ █████   ██ ████ ██ █████   
   ██    ██   ██ ██      ██  ██  ██ ██      
   ██    ██   ██ ███████ ██      ██ ███████ 
                                            
   \033[41m    DEVELOPED BY ZIHAD HOSSAIN RAFI    \033[00m"""
   
   try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="RAFI-allahuakbar1971"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get("https://github.com/MR-ZIHAD/Approved/blob/main/Approved.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print(logo)
    print("\n\033[1;92mYour key  : "+key2)
    print("\n\033[1;92mContact Admin ")
    os.system("xdg-open https://facebook.com/zihad.hossain36")
    exit()
   
def mainmenu():
        try:
                os.system ("clear")
                sprint (o+logo)
                print ("")
                print (w+"THIS TOOL IS MADE TO FACILITATE TERMINAL USERS")
                print (w+"HOPEFULLY USEFUL, THANKS!")
                print ("")
                print ("01"+r+")"+w+" ASCII LOGO")
                print ("02"+r+")"+w+" FONT STYLE")
                print ("03"+r+")"+w+" BACKGROUND COLORS")
                print ("04"+r+")"+w+" PROMPT STYLE")
                print ("05"+r+")"+w+" ZSH THEME")
                print ("06"+r+")"+w+" OPEN ZSHRC")
                print ("00"+r+")"+w+" EXIT")
                print("")
                saydog()
        except KeyboardInterrupt:
                sys.exit(1)

def saydog():
        pil = str(input("["+r+"~"+w+"]"+r+" > "+w))
        if pil == "0" or pil == "00":
                sys.exit(1)
        elif pil == "1" or pil == "01":
                print ("")
                print ("\033[41mASCII LOGO\033[00m")
                print ("CUSTOMIZE ASCII LOGO FOR TERMINAL THEME")
                print ("")
                print ("01"+r+")"+w+" GET ASCII LOGO FROM LIST")
                print ("02"+r+")"+w+" GENERATE ASCII LOGO FROM FILES")
                print ("03"+r+")"+w+" SET LOGO MANUALLY")
                print ("")
                pil = str(input("["+r+"~/"+w+"asciilogo"+r+"/"+w+"]"+r+" > "+w))
                if pil == "back":
                        saydog()
                elif pil == "1" or pil == "01":
                        os.system("cd lib;python ascii.py")
                        print ("")
                        print (r+"HOW TO USE"+w)
                        print ("COPY YOUR FAVORITE LOGO")
                        print ("THEN PUT YOUR LOGO IN THE logo.txt FILE ")
                        print ("YOU CAN PROVIDE A COLOR FOR THE LOGO")
                        print ("THAT YOU HAVE SAVED BEFORE")
                        print ("")
                        pil = str(input("DO YOU WANT TO OPEN logo.txt file ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                print ("")
                                print (c+"[+]"+w+" OPENING logo.txt")
                                print (c+"[+]"+w+" PASTE YOUR LOGO IN THIS FILE")
                                print (c+"[+]"+w+" AND SAVE YOUR LOGO WITHCTRL + X + Y and ENTER")
                                print ("")
                                time.sleep(6)
                                os.system("nano cache/logo.txt")
                                os.system("cat cache/d1 > logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                print (c+"[+]"+w+" files saved as cache/logo.txt")
                                print (c+"[+]"+w+" success")
                                print ("")
                                pil = str(input("do you want to add color ? (y/n) "))
                                if pil == "y" or pil == "Y":
                                        print ("")
                                        print (w+"01"+r+")"+w+" red")
                                        print (w+"02"+r+")"+w+" yellow")
                                        print (w+"03"+r+")"+w+" green")
                                        print (w+"04"+r+")"+w+" purple")
                                        print (w+"05"+r+")"+w+" cyan")
                                        print (w+"06"+r+")"+w+" blue")
                                        print (w+"07"+r+")"+w+" dark red")
                                        print (w+"08"+r+")"+w+" dark yellow")
                                        print (w+"09"+r+")"+w+" dark green")
                                        print (w+"10"+r+")"+w+" dark purple")
                                        print (w+"11"+r+")"+w+" dark cyan")
                                        print (w+"12"+r+")"+w+" dark blue")
                                        print ("")
                                        pil = str(input("color number"+r+" => "+w))
                                        if pil == '1' or pil == "01":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '2' or pil == "02":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '3' or pil == "03":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '4' or pil == "04":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '5' or pil == "05":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '6' or pil == "06":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '7' or pil == "07":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '8' or pil == "08":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '9' or pil == "09":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '10':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '11':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '12':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                else:
                                        mainmenu()
                        else:
                                mainmenu()
                elif pil == "2":
                        print ("")
                        print (c+"[+]"+w+" IMAGE TO ASCII")
                        print (c+"[+]"+w+" CHECKING ACCESS TO STORAGE")
                        os.system("termux-setup-storage")
                        print (c+"[+]"+w+" MAKE SURE THE IMAGE TYPE IS jpg / jpeg")
                        print ("")
                        print (r+"HOW TO USE")
                        print (w+"PLEASE INPUT THE IMAGE DIRECTORY")
                        print (w+"EXAMPLE: /sdcard/download/image.jpg")
                        print ("")
                        img = input(w+"CHOOSE FILES"+r+" => ")
                        print (c+"[+]"+w+" GENERATING ASCII")
                        os.system("jp2a "+img)
                        pil = str(input("DO YOU WANT TO USE THIS LOGO? (y/n) "))
                        if pil == "y" or pil == "Y":
                                print ("")
                                os.system("jp2a "+img+" > cache/logo.txt")
                                print (c+"[+]"+w+" FILE SAVED AS cache/logo.txt")
                                print ("")
                                pil = str(input("DO YOU WANT TO ADD COLOR ? (y/n) "))
                                if pil == "y" or pil == "Y":
                                        print ("")
                                        print (w+"01"+r+")"+w+" red")
                                        print (w+"02"+r+")"+w+" yellow")
                                        print (w+"03"+r+")"+w+" green")
                                        print (w+"04"+r+")"+w+" purple")
                                        print (w+"05"+r+")"+w+" cyan")
                                        print (w+"06"+r+")"+w+" blue")
                                        print (w+"07"+r+")"+w+" dark red")
                                        print (w+"08"+r+")"+w+" dark yellow")
                                        print (w+"09"+r+")"+w+" dark green")
                                        print (w+"10"+r+")"+w+" dark purple")
                                        print (w+"11"+r+")"+w+" dark cyan")
                                        print (w+"12"+r+")"+w+" dark blue")
                                        print ("")
                                        pil = str(input("COLOR NUMBER"+r+" => "+w))
                                        if pil == '1' or pil == "01":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '2' or pil == "02":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '3' or pil == "03":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" File SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '4' or pil == "04":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '5' or pil == "05":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '6' or pil == "06":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '7' or pil == "07":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '8' or pil == "08":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED ASmylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '9' or pil == "09":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '10':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '11':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '12':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                                print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                                print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                        elif pil == "n" or pil == "N":
                                mainmenu()
                elif pil == "3" or pil == "03":
                        print ("")
                        print (c+"[+]"+w+" PLEASE PUT YOUR LOGO INlogo.txt files")
                        print (c+"[+]"+w+" SAVE WITH CTRL + X + Y and ENTER")
                        print (c+"[+]"+w+" OPENING logo.txt")
                        time.sleep(6)
                        os.system("nano cache/logo.txt")
                        print (c+"[+]"+w+" FILE SAVED as cache/logo.txt")
                        print ("")
                        pil = str(input("DO YOU WANT TO ADD COLOR? (y/n) "))
                        if pil == "y" or pil ==  "Y":
                                print ("")
                                print (w+"01"+r+")"+w+" red")
                                print (w+"02"+r+")"+w+" yellow")
                                print (w+"03"+r+")"+w+" green")
                                print (w+"04"+r+")"+w+" purple")
                                print (w+"05"+r+")"+w+" cyan")
                                print (w+"06"+r+")"+w+" blue")
                                print (w+"07"+r+")"+w+" dark red")
                                print (w+"08"+r+")"+w+" dark yellow")
                                print (w+"09"+r+")"+w+" dark green")
                                print (w+"10"+r+")"+w+" dark purple")
                                print (w+"11"+r+")"+w+" dark cyan")
                                print (w+"12"+r+")"+w+" dark blue")
                                print ("")
                                pil = str(input("COLOR NUMBER"+r+" => "+w))
                                if pil == '1' or pil == "01":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '2' or pil == "02":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED ASmylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '3' or pil == "03":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED ASmylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '4' or pil == "04":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '5' or pil == "05":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '6' or pil == "06":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '7' or pil == "07":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '8' or pil == "08":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '9' or pil == "09":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '10':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '11':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  ENTER "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '12':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" COLOR HAS BEEN ADDED")
                                        print (c+"[+]"+w+" GENERATING PYTHON FILE")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" YOUR FILE HAS BEEN GENERATED")
                                        print (c+"[+]"+w+" FILE SAVED AS mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                        else:
                                mainmenu()
                else:
                        mainmenu()
        elif pil == "2" or pil == "02":
                print ("")
                print ("\033[041mFONT STYLE\033[00m")
                print ("CUSTOMIZE FONT STYLE FOR TERMINAL")
                os.system ("~/.termux/fonts.sh")
                mainmenu()
        elif pil == "3" or pil == "03":
                print ("")
                print ("\033[041mBACKGROUND COLOR\033[00m")
                print ("Customize Background Color For Terminal")
                os.system ("~/.termux/colors.sh")
                mainmenu()
        elif pil == "4" or pil == "04":
                print ("")
                print ("\033[41mPROMPT STYLE\033[00m")
                print ("Customize Prompt Style For Terminal")
                print ("")
                print (w+"[1] YOURNAME@ROOT:~#")
                print (w+"[2] Custom Manually")
                print ("")
                pil = str(input("Enter A Number, Leave Blank To Not To Change: "))
                if pil == "back":
                        saydog()
                elif pil == "1" or pil == "01":
                        name = str(input(w+"PLEASE INPUT YOUR USERNAME HERE: "))
                        print ("")
                        print (c+"[+]"+w+" GENERATE PROMPT STYLE")
                        print (c+"[+]"+w+" USE USERNAME "+name)
                        print ("")
                        os.system("echo "+'"PS1='+"'"+name+"@root:~# '"+'"'+" >> ~/.zshrc")
                        time.sleep(3)
                        print (c+"[+]"+w+" SUCCESS")
                        print (c+"[+]"+w+" PLEASE RESTART YOUR TERMINAL")
                        print ("")
                        pil = str(input("DO YOU WANT TO EXIT THIS TOOL? (y/n) "))
                        if pil == "y" or pil == "Y":
                                sys.exit(0)
                        else:
                                mainmenu()
                elif pil == "2" or pil == "02":
                        print ("")
                        print (c+"[+]"+w+" OPENING FILES myprompt.txt")
                        print (c+"[+]"+w+" PLEASE PUT YOUR PROMPT CODE IN THIS FILE")
                        print (c+"[+]"+w+" SAVE FILE WITH CTRL + X + Y and ENTER")
                        time.sleep(6)
                        print ("")
                        os.system("nano cache/myprompt.txt")
                        print ("")
                        print (c+"[+]"+w+" FILE SAVED AS cache/myprompt.txt")
                        print (c+"[+]"+w+" CLONING INTO ZSHRC ...")
                        os.system("cat cache/myprompt.txt >> ~/.zshrc")
                        time.sleep(3)
                        print (c+"[+]"+w+" SUCCESS, PLEASE RESTART YOUR TERMINAL")
                        pil = str(input("DO YOU WANT TO EXIT THIS TOOL ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                sys.exit(0)
                        else:
                                mainmenu()
                else:
                        time.sleep(1)
                        mainmenu()
        elif pil == "5" or pil == "05":
                print ("")
                try:
                        os.system("cd /data/data/com.termux/files/home/.oh-my-zsh/tools;./theme_chooser.sh")
                        pil = str(input("DO YOU WANT TO BACK TO MAIN MENU ? (y/n) "))
                except KeyboardInterrupt:
                        time.sleep(1)
                        mainmenu()
        elif pil == "6" or pil == "06":
                print ("")
                print (c+"[+]"+w+" OPENING ZSHRC FILES")
                print (c+"[+]"+w+" PLEASE WAIT ...")
                time.sleep(1)
                print (c+"[+]"+w+"  ")
                os.system('nano ~/.zshrc')
                print ("")
                pil = str(input("BACK TO MAIN MENU ? (y/n) "))
                if pil == "y" or pil == "Y":
                        mainmenu()
                else:
                        sys.exit(0)
        else:
                saydog()

## MAIN
os.system("curl -s ifconfig.co > cache/ip.txt")
mainmenu()
