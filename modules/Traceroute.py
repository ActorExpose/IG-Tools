import requests
import sys
from colorama import Fore,init

init()
def __start__():
    
    try:
        print(Fore.GREEN+" [+] "+Fore.WHITE+"Please Enter Domain \n")
        target = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+Fore.BLUE+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+Fore.WHITE+"TraceToute"+Fore.GREEN+"""]
 └──╼  """+Fore.WHITE+"$ ").lower()
 
        req = requests.get("https://api.hackertarget.com/mtr/?q="+target).text

        print(Fore.LIGHTBLUE_EX+req)

        try:
            input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()

    except:
        print("")
        sys.exit()


