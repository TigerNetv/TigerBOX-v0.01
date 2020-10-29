import os

import datetime

from src.scan import *
from src.credits import *
from src.proxyscraper import *
from src.passgen import *
from src.iptool import *

from colored import fg, attr

now = datetime.datetime.now()


commandloop = 1;
whitecolor = fg('#FFFFFF')
redcolor = fg('#8B0000')
greencolor = fg('#009900')
timecolor = fg('#9400D3')
res = attr('reset')






print()
print(" ___  _                 ___  ___ __  _ ")
print("|_ _|<_> ___  ___  _ _ | . >| . |\ \/  ")
print(" | | | |/ . |/ ._>| '_>| . \| | | \ \  ")
print(" |_| |_|\_. |\___.|_|  |___/`___'_/\_\ ")
print("        <___'                          ")
print()

name = input(whitecolor + "What is your name? " + res)
os.system("title User : " + name + " TigerBOX v0.01")
print()
print(whitecolor + "Welcome " + res + greencolor + name + res)
print()

while commandloop == 1:
    print ("")
    print ((timecolor + now.strftime("%d/%m/%Y %H:%M:%S") + res) + (whitecolor + " Select a module" + res))
    print("")
    print ((greencolor + "              [1] " + res + whitecolor + "Scan Network" + res))
    print ((greencolor + "              [2] " + res + whitecolor + "Proxy Scraper" + res))
    print ((greencolor + "              [3] " + res + whitecolor + "IPTool [Whois / DNS Reverse / Reverse IP " + res))
    print ((greencolor + "              [4] " + res + whitecolor + "Password Generator" + res))
    print ((greencolor + "              [5] " + res + whitecolor + "Credits" + res))
    print ((greencolor + "              [6] " + res + whitecolor + "Quits the program" + res))    
    commandinput = input(whitecolor + " > " + res) 
    if commandinput == '1':
        scan()
    if commandinput == '2':
        proxyscraper()
    if commandinput == '3':
        iptool()
    if commandinput == '4':
        passgen()
    if commandinput == '5':
        credits()
    if commandinput == '6':
        exit()
        