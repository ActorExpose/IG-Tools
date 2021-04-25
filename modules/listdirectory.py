import requests 
import sys
from colorama import Fore,init
import time
def __start__():
 listdir=("""robots.txt
admin-ajax.php
search/
login/
sitemap.xml
sitemap2.xml
config.php
wp-login.php
log.txt
update.php
INSTALL.pgsql.txt
user/login/
INSTALL.txt
profiles/
scripts/
LICENSE.txt
CHANGELOG.txt
themes/
inculdes/
misc/
user/logout/
user/register/
cron.php
filter/tips/
comment/reply/
xmlrpc.php
install.php
modules/
MAINTAINERS.txt
user/password/
node/add/
INSTALL.sqlite.txt
UPGRADE.txt
INSTALL.mysql.txt""")
print(Fore.GREEN+"[+]"+Fore.WHITE+"Pless Enter url web site..!\n")
url = print(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"List Directory"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")

if 'http' in url:
                pass

elif 'http' not in url:
                url=('http://'+url)


for i in listdir:
    urls=url+"/"+listdir
    req = requests.get(urls)
    if req.status_code==200:
        print(Fore.GREEN+"  [+]  "+Fore.WHITE+"Faund: "+urls )
    else:
        print(Fore.GREEN+"  [-]  "+Fore.WHITE+"Not Faund: "+urls)

        try:
            input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()


    

