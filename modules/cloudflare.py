import socket
import sys
import time
from colorama import Fore,init
from helplist import helpp


def __start__():

    init()

    print(Fore.GREEN+" [+] "+Fore.WHITE+"Please Enter The Target Website Address\n")
    subdom = ("""ftp
cpanel
webmail
localhost
local 
mysql 
forum
driect-connect
blog 
vb
forums
home
direct
forums
mail
access
admin
administrator
email
downloads
ssh
owa
bbs
webmin
paralel
parallels
www0
www
www1
www2
www3
www4
www5
shop
api
blogs
test
mx1
cdn 
mysql
mail1
secure
server
ns1
ns2
smtp
vpn
m
mail2 
postal
support
web
dev
""").split()
    site = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+Fore.BLUE+"~"+Fore.RED+"Root"+Fore.WHITE+"/"+Fore.WHITE+"Cloud Flare"+Fore.GREEN+"""]
 └──╼  """+Fore.WHITE+"$ ").lower()
    
    

    if site == "":
        try:
            print(Fore.YELLOW+"\n [!] "+Fore.WHITE+"Please Enter Address :) \n")
            time.sleep(5)
            sys.exit()
        except:
            return
    


    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (Fore.GREEN+" [+] "+Fore.YELLOW+"CloudFlare Bypass"+Fore.WHITE+ str(bypass) +Fore.YELLOW+ ' | '+Fore.WHITE+ str(hosts))
        except Exception:
            pass


    try:
        
        input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...)")
    except:
        print("")
        sys.exit()



