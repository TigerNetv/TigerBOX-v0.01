import requests

from colored import fg, attr
redcolor = fg('#8B0000')
greencolor = fg('#009900')
whitecolor = fg('#FFFFFF')
timecolor = fg('#9400D3')
res = attr('reset')


def proxyscraper():    
    
    print()
    print ((whitecolor + "              What proxies do you want to scrape?" + res))
    print ((greencolor + "              [1] " + res) + (whitecolor + "ALL TYPES" + res))
    print ((greencolor + "              [2] " + res) + (whitecolor + "HTTPS/HTTP" + res))
    print ((greencolor + "              [3] " + res) + (whitecolor + "SOCKS4" + res))
    print ((greencolor + "              [4] " + res) + (whitecolor + "SOCKS5" + res))
    print ((greencolor + "              [5] " + res) + (whitecolor + "BACK" + res))
    print ((greencolor + "              [6] " + res) + (whitecolor + "Quits the program" + res))
    print()
    
    inp = input(whitecolor + " > " + res)
    print()
    
    if inp == '1':
        alltypes = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=all&timeout=10000&country=all&ssl=all&anonymity=all%22")
        with open('all_proxies.txt', 'wb') as f:
            f.write(alltypes.content)
        print("Proxies saved!")
        f.close()
    elif inp == '2':
        httpstype = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all")
        with open('http_proxies.txt', 'wb') as g:
            g.write(httpstype.content)
        print("Proxies saved!")
        g.close()
    elif inp == '3':
        sockspatrutype = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
        with open('socks4_proxies.txt', 'wb') as h:
            h.write(sockspatrutype.content)
        print("Proxies saved!")
        h.close()
    elif inp == '4':
        sockscincitype = requests.get("https://api.proxyscrape.com/?request=getprox&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
        with open('socks5_proxies.txt', 'wb') as i:
            i.write(sockscincitype.content)
        print("Proxies saved!")
        i.close()   
    elif inp == '6':
        exit()