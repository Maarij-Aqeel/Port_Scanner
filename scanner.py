#!/bin/python

import sys
from datetime import datetime as dt
import socket


common_ports=["53","80","443","22","143","445","139"]

#Just Basic Banner :)
print("""
__________              __      _________                                         
\______   \____________/  |_   /   _____/ ____ _____    ____   ____   ___________ 
 |     ___/  _ \_  __ \   __\  \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
 |    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
 |____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /___|  /\___  >__|   
                                      \/     \/     \/     \/     \/     \/       
""")

print("Syntax: python3 scanner.py ***.***.*.* -p 12,54,76,43")
print("        python3 scanner.py ***.***.*.* (Will run on default ports)")

#Help page
if '-h'in sys.argv:
       print("        python3 scanner.py -h (Displays this page)")
       print("\nExample:python3 scanner.py 10.10.14.1 -p 443,80,143,53")
       sys.exit()

#Define target 

if len(sys.argv)<2:
       print("No Host Given!")
       sys.exit()

target = sys.argv[1]
ip_addr=target.split(".")
if  ip_addr[0].isdigit():
    if len(ip_addr)!=4:
        print("\nInvalid IP_Address/Hostname")
        sys.exit()
    else:
        Target=socket.gethostbyname(sys.argv[1])#gethostbyname convert given host to ip_addrs like daraz.pk to 10.10.43.12 something like this
else:
        try:
         Target=socket.gethostbyname(sys.argv[1])
        except socket.gaierror:
                print("\nHostname Couldn't be resolved")#Host can't be converted to ip addrs
                sys.exit()

if len(sys.argv)==2:
        port=common_ports

elif len(sys.argv)==4:
        if sys.argv[2]!='-p':
               print("\nInvalid Syntax!")
               sys.exit()
        stri=(sys.argv[3])
        port=stri.split(",")
else:
        print("\nInvalid Syntax!")
        sys.exit()

print("-"*80)
print(f"Scanning Target {Target}")
print(f"Time started {str(dt.now())}")
print("-"*80)

#Logic
try:
        for p in port:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                p=int(p)
                print(f"Connecting to {Target} at port {p}")
                connect=s.connect_ex((Target,p))
                if connect==0:
                        print(f"Port {p} is Open")
                else:
                        print(f"Port {p} is Closed")
                s.close()

except KeyboardInterrupt:
        print("\nExiting program....")#CTRL+C interrupt
        sys.exit()
except socket.error:
       print("\nConnection to server Refused!")#Server is down
       sys.exit()

print(f"Scanning finished at {dt.now()}")

