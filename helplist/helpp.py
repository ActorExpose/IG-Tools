import os
from colorama import Fore
import time
import sys
def Banner():

    os.system("cls")
    
    print(Fore.GREEN+"""\n    
                         .-'''-.        .-'''-.                      
                        '   _    \     '   _    \                    
  .--.                /   /` '.   \  /   /` '.   \                   
  |__|  .--./)       .   |     \  ' .   |     \  '                   
  .--. /.''.\     .| |   '      |  '|   '      |  '  .|              
  |  || |  | |  .' |_\    \     / / \    \     / / .' |_             
  |  | \`-' / .'     |`.   ` ..' /   `.   ` ..' /.'     |       _    
  |  | /("'` '--.  .-'   '-...-'`       '-...-'`'--.  .-'     .' |   
  |  | \ '---.  |  |                              |  |      .   | / 
  |__|  /'""'.\ |  |      Developer:OmidRanjbar   |  |    .'.'| |// 
       ||     |||  '.'    Channel  :@aGreyHat    |  '.'.'.'.-'  /  
        \. __./ |   /     ToolsName:IGTOOLS      |   / .'   \_.'   
        `'---'  `'-'                               `'-'                       
           """)       
# ₿
def infolist1():
    time.sleep(0.1)
    print(Fore.WHITE+"-01"+Fore.YELLOW+"  [-$]  "+Fore.BLUE+"- Welcome To IGTOOLS"+Fore.YELLOW+"        [-k]  "+Fore.BLUE+"- Developer")
    time.sleep(0.1)
    print(Fore.WHITE+"-02"+Fore.GREEN+"  [-h]  "+Fore.WHITE+"- Help"+Fore.GREEN+"                      [-B]  "+Fore.WHITE+"- Bypass Cloud Flare")
    time.sleep(0.1)
    print(Fore.WHITE+"-03"+Fore.GREEN+"  [-c]  "+Fore.WHITE+"- Cms Detect"+Fore.GREEN+"                [-T]  "+Fore.WHITE+"- Trace Toute")
    time.sleep(0.1)
    print(Fore.WHITE+"-04"+Fore.GREEN+"  [-V]  "+Fore.WHITE+"- Reverse IP"+Fore.GREEN+"                [-P]  "+Fore.WHITE+"- Port Scan")
    time.sleep(0.1)
    print(Fore.WHITE+"-05"+Fore.GREEN+"  [-H]  "+Fore.WHITE+"- Show HTTP Header"+Fore.GREEN+"          [-D]  "+Fore.WHITE+"- Find Shared DNS")
    time.sleep(0.1)
    print(Fore.WHITE+"-06"+Fore.GREEN+"  [-W]  "+Fore.WHITE+"- Whois site"+Fore.GREEN+"                [-L]  "+Fore.WHITE+"- DNS Lookup")
    time.sleep(0.1)
    print(Fore.WHITE+"-07"+Fore.GREEN+"  [-R]  "+Fore.WHITE+"- Robots Scanner"+Fore.GREEN+"            [-F]  "+Fore.WHITE+"- Admin Page Finder")
    time.sleep(0.1)
    print(Fore.WHITE+"-08"+Fore.GREEN+"  [-q]  "+Fore.WHITE+"- CMS Detection Woedperess"+Fore.GREEN+"  [-i]  "+Fore.WHITE+"- IP Location")
    time.sleep(0.1)
    print(Fore.WHITE+"-09"+Fore.GREEN+"  [-X]  "+Fore.WHITE+"- Exit\n")
    # time.sleep(0.1)
    # print(Fore.WHITE+"-10"+Fore.GREEN+"  [-G]  "+Fore.WHITE+"- Test\n")

    #Next Update in Ig tools (;
    #ListDirectory

 

def infolist2():

      Banner()
      time.sleep(0.1)
      print (Fore.YELLOW+"  [$]  "+Fore.BLUE+"  Develper  :  "+Fore.WHITE+"OmidRanjbar(Zed)\n")
      time.sleep(0.1)
      print (Fore.YELLOW+"  [$]  "+Fore.BLUE+"  Thank's  :  "+Fore.WHITE+"ArashGholipor\n")
      time.sleep(0.1)
      print (Fore.YELLOW+"  [$]  "+Fore.BLUE+"  Channel Telegram ID  :  "+Fore.WHITE+"@aGeryHat Please Join ;)\n")
      time.sleep(0.1) 
      try:

            input(Fore.BLUE+" [-M] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
      except:
            print("")
            sys.exit()



def infowp():
    Banner()
    
    print(Fore.WHITE+"-1"+Fore.GREEN+"  [-p]  "+Fore.WHITE+" - Get Plugins ")    
    time.sleep(0.1)
    print(Fore.WHITE+"-2"+Fore.GREEN+"  [-U]  "+Fore.WHITE+" - Get Username ")    
    time.sleep(0.1)
    print(Fore.WHITE+"-3"+Fore.GREEN+"  [-M]  "+Fore.WHITE+" - Back To Menu \n")
    time.sleep(0.1)

def infohelp():
    Banner()
    print(Fore.BLUE+"""
        Hello and welcome to the help section.
        You can use keywords and go to different sections
        Access to
        This tool is open source. You can customize this tool
        It has 24-hour support
        Backup section:"""+Fore.WHITE+""" https://t.me/Deusnegro"""+Fore.BLUE+"""
        Cannele Address:"""+Fore.WHITE+""" https://t.me/aGreyHat 
        """)
    try:
        input(Fore.BLUE+" [-M] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()