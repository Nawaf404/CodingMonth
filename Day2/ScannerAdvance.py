from socket import *
import sys
import datetime
import time
from termcolor import *
print("First, you can't run the program in IDLE, must in CMD")
# like nmap 127.0.0.1 ip is input in same line
if len(sys.argv)==1: sys.exit("NawafScan error! please check the option.")
print("---------------- Cyber Python -----------------")
print("")
host = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
color = sys.argv[4]
active_ports = []

start_time = datetime.datetime.now()
print(colored("Starting NawafScan 1.0 (https://TechCampus.com) at","yellow"),start_time)
print("NawafScan report for", host)
print("Ports range from", start_port, "to", end_port)
print("\n")
for port in range(start_port, end_port):
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((host,port))
    if result == 0:
        print("port", port, "is open")
        active_ports.append(port)
    else:
        print("port", port, "is close")
    time.sleep(2)
end_time = datetime.datetime.now()
print("\n")
print("The end time is ", end_time, "- the open ports are", active_ports)
print("NawafScan completed successfully")