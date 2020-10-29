from socket import *
import time
startTime = time.time()
from colored import fg, attr

greencolor = fg('#009900')
res = attr('reset')




def scan():
   target = input(greencolor + 'Enter the host to be scanned: ' + res)
   t_IP = gethostbyname(target)
   print (greencolor + 'Starting scan on host: ', t_IP + res)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print (greencolor + 'Port %d: OPEN' % (i,) + res)
      s.close()