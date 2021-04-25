import sys
import requests
from colorama import Fore

def __start__():
    try:
        print(Fore.GREEN+"\n [+] "+Fore.WHITE+"Plase Enter IP / Domain\n")
        inp = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"Port Scan"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")
        result = requests.get('https://api.hackertarget.com/nmap/?q=' + inp).text
        print(Fore.GREEN+" [+] "+Fore.WHITE+result)
        try:

            input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
        
    except:
        print("")
        sys.exit()
