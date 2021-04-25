import os
import requests
import json
from colorama import Fore
import sys

def __start__():
 try:        
        
        print (Fore.GREEN+" [+] "+Fore.WHITE+"Enter The Domain / IP\n")

        website = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+" Reverse IP"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")

        mysite = {"remoteAddress":website}

        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)

        source = json.loads(link.content)

        for data in source["domainArray"]:
                print(Fore.GREEN+"[+]"+Fore.WHITE+data[0]+"\n")

        try:

                input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
                print("")
                sys.exit()
 except:
         print("")
         sys.exit()