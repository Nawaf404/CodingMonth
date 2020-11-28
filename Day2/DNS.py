import socket
import requests
import pyfiglet # make text a great logo
# chmod +x dns : excute turn on as App
ascii_banner = pyfiglet.figlet_format("TechCampus")
print(ascii_banner)
print("------ Cyper Python -------")
print("")
print("if you want to change, search about domain of ip type X")
try:
    domain = input("What is the domain :\n")

    if domain == "X":
        ipGet = input("Enter iP Address : ")
        d = socket.gethostbyaddr(ipGet)
        print(d)
    elif "1" in domain:
        print("Sorry but u typed iP Address, not domain!")
        exit()
    else:
        pass
    ip = socket.gethostbyname(domain)
    print('The DNS of ', domain, ' is: ', ip)
except socket.herror:
    print("Sorry Host not found!")
    exit()
except socket.gaierror:
    print("Sorry iP invalid")


myName = pyfiglet.figlet_format("N a w a f")
print(myName)