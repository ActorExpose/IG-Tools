import requests, builtwith
from colorama import Fore,init
import sys


init()
def __start__():

 try:
    print(Fore.GREEN+" [+] "+Fore.WHITE+"Plase Enter Domain\n")
    target = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"Cms Detect"+Fore.GREEN+"""]
 └──╼  """+Fore.WHITE+"$ ").lower()


    if "http://" in target:
        pass
    elif not "http://" in target:
        target = 'http://'+target

    info = builtwith.parse(target)


    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(Fore.BLUE+"\n"+name+': '+value)

    try:
         input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
    except:
         print("")
         sys.exit()


 except:
         print("")
         sys.exit()







