import webbrowser
from colored import fg, attr


whitecolor = fg('#FFFFFF')
redcolor = fg('#8B0000')
greencolor = fg('#009900')
timecolor = fg('#9400D3')
res = attr('reset')

def iptool():
    print(greencolor + "                  [1] " + res + whitecolor + "Whois Lookup" + res)
    print(greencolor + "                  [2] " + res + whitecolor + "DNS Lookup" + res)
    print(greencolor + "                  [3] " + res + whitecolor + "Reverse Lookup" + res)
    userinput = input(whitecolor + " > " + res)
    
    if userinput == '1':
        print()
        url_input = input(greencolor + "Your Url :" + res)
        url = 'http://api.hackertarget.com/whois/?q=' + url_input
        webbrowser.get().open(url)        
    if userinput == '2':
        url_input = input(greencolor + "Your Url :" + res)
        url = 'https://api.hackertarget.com/dnslookup/?q=' + url_input
        webbrowser.get().open(url)
    if(userinput == '3'):
        url_input = input(greencolor + "Your IP :" + res)
        url = 'http://api.hackertarget.com/reverseiplookup/?q=' + url_input
        webbrowser.get().open(url)
