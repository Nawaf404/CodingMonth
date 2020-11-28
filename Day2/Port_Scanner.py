# Second way in Ethical Hacking
# Enter, TCP or UDP
# range from 0 to 65,535 thousands
import time
from socket import *
import datetime
from termcolor import colored
host = "127.0.0.1"
start_port = 10
end_port = 100
active_ports = []
start_time = datetime.datetime.now()
print("Starting NawafScan 1.0 ( https://TechCampus.com ) at ", start_time)
print("NawafScan report for", host)
print("Ports range from", start_port, " to ", end_port)
print("\n")
for port in range(start_port,end_port):
    s = socket(AF_INET, SOCK_STREAM) # connect start
    result = s.connect_ex((host, port)) # make connection for know if device work or not
    if result == 0:
        print(colored(f"port {port} is open", "green"))
        active_ports.append(port)
        print("ports open : ", active_ports)
    else:
        continue
        print(colored(f"port {port} is close", "red"))
    #time.sleep(2) # for take a rest
end_time = datetime.datetime.now()
print("\n")
print("The end time is", end_time, "- the open ports are", active_ports)
print("NawafScan complete successfully!")