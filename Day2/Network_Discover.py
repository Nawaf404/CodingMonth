import socket
import subprocess
from termcolor import colored
from art import *
tprint("Nawaf",font="block",chr_ignore=True)
count = 0
print("type first 3 in iP and . dot in last")
ip = input("Enter iP to Scan : ")
rangeTo = int(input("Enter range to : "))
print(colored(f"Will scan ip {ip}", 'green'))

for ping in range(0,rangeTo):
    host = ip + str(ping)
    # ip = socket.gethostbyaddr(str(host))
    result = subprocess.call(["ping",host],stdout=subprocess.PIPE)
    if result == 0:
        # print(host,colored(f"Device {socket.gethostbyaddr(host)}","cyan"),colored(' - the Host is UP', 'green'))
        print(host,colored("Device","cyan"),colored(' - the Host is UP', 'green'))
    else:
        print(host, colored('- the Host is DOWN', 'red'))
    count = count+1
print("Scanned ", count, "systems")
# server google maybe not be google.com, maybe it's API or service