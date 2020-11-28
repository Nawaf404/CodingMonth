import subprocess
import socket
from art import *
from termcolor import *
import pyfiglet
logo = pyfiglet.figlet_format("Project")
print(logo)

print(colored("Welcome In Project Cyber Python","cyan"))
print("|----------------------------------------------------|")
print(colored("|    1- Scrabing Web for Amazon                      |", "red"))
print(colored("|    2 - Weather Status                              |","yellow"))
print(colored("|    3- DNS                                          |","green"))
print(colored("|    4- PING                                         |", "blue"))
print(colored("|    5- Network Discovery                            |", "cyan"))
print(colored("|    6- Port Scanner                                 |", "red"))
print(colored("|    7- ScannerAdvance                               |", "green"))
print(colored("|    8- Scrabing Instagram                           |","blue"))
print(colored("|    9- Hash                                         |","yellow"))
print(colored("|    10- Dicionary Attack                            |","blue"))
print(colored("|    11- Stenganography                              |", "red"))
print("|----------------------------------------------------|")
ask = input(colored("kali@root $ ", "blue"))
if ask == "1":
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("https://www.amazon.ae/whitefriday/")
    print("Code Of HTTP : ", response)
    # 200 is ok, 300 redirect, 400 for visitor
    # help you in parsin
    # XML = for store datas like json, use it in API almost
    content = response.text
    print(content)  # will print html tags

    soup = BeautifulSoup(content, 'html.parser')
    # name of module , use content and read it as html parser
    for link in soup.find_all('img'):
        # soup.find_all('a') will print all of a, include href , clases, everything
        print(link.get('src'))
        # type link.get(choose tags to show)

    # API = Application Programming Interface
if ask == "2":
    import requests

    api_address = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = input("Hi, What's your city name :\n")
    url = api_address + city
    json_data = requests.get(url).json()
    main_weather = json_data['weather'][0]['description']
    print(main_weather)
if ask == "3":
    import socket
    import requests
    import pyfiglet  # make text a great logo

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
if ask == "4":
    tprint("Nawaf", font="block", chr_ignore=True)
    logo = pyfiglet.figlet_format("Ping")
    print(colored(logo, "cyan"))
    print(colored("---------- TechCampus, Nawaf ---------", "yellow"))
    print(colored("--------- Cyper Python ----------", "blue"))
    print("")
    host = input("What is your IP :\n")
    result = subprocess.call(['ping', host], stdout=subprocess.PIPE)
    if result == 0:
        print(colored('The Host is UP', 'green'))
    else:
        print(colored('The Host is DOWN', 'red'))

if ask == "5":
    tprint("Nawaf", font="block", chr_ignore=True)
    count = 0
    print("type first 3 in iP and . dot in last")
    ip = input("Enter iP to Scan : ")
    rangeTo = int(input("Enter range to : "))
    print(colored(f"Will scan ip {ip}", 'green'))
    for ping in range(0, rangeTo):
        host = "127.0.0." + str(ping)
        # ip = socket.gethostbyaddr(str(host))
        result = subprocess.call(["ping", host], stdout=subprocess.PIPE)
        if result == 0:
            # print(host,colored(f"Device {socket.gethostbyaddr(host)}","cyan"),colored(' - the Host is UP', 'green'))
            print(host, colored("Device", "cyan"), colored(' - the Host is UP', 'green'))
        else:
            print(host, colored('- the Host is DOWN', 'red'))
        count = count + 1
    print("Scanned ", count, "systems")
if ask == "6":
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
    for port in range(start_port, end_port):
        s = socket(AF_INET, SOCK_STREAM)  # connect start
        result = s.connect_ex((host, port))  # make connection for know if device work or not
        if result == 0:
            print(colored(f"port {port} is open", "green"))
            active_ports.append(port)
            print("ports open : ", active_ports)
        else:

            print(colored(f"port {port} is close", "red"))
        # time.sleep(2) # for take a rest
    end_time = datetime.datetime.now()
    print("\n")
    print("The end time is", end_time, "- the open ports are", active_ports)
    print("NawafScan complete successfully!")

if ask == "7":
    from socket import *
    import sys
    import datetime
    import time
    from termcolor import *

    print("First, you can't run the program in IDLE, must in CMD")
    # like nmap 127.0.0.1 ip is input in same line
    if len(sys.argv) == 1: sys.exit("NawafScan error! please check the option.")
    print("---------------- Cyber Python -----------------")
    print("")
    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    color = sys.argv[4]
    active_ports = []

    start_time = datetime.datetime.now()
    print(colored("Starting NawafScan 1.0 (https://TechCampus.com) at", "yellow"), start_time)
    print("NawafScan report for", host)
    print("Ports range from", start_port, "to", end_port)
    print("\n")
    for port in range(start_port, end_port):
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((host, port))
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
if ask == "8":

    from bs4 import BeautifulSoup
    import requests

    user = input("Enter your Username : ")
    URL = f"https://www.instagram.com/{user}/"
    send = requests.get(URL)
    if send.status_code == 200:
        print("Found Page, will work now")
    elif send.status_code == 404:
        print("Canno't found user")
    else:
        print("Sorry something goes happen, check http code -->", send.status_code)
        exit()
    print("Working .. ")


    def parse_data(s):
        data = {}
        # print(s)
        s = s.split(",")
        # print(s)

        data['Followers'] = s[0]
        data['Following'] = s[2]
        Posts = s[3]
        Posts = Posts.split("-")
        # print(Posts)
        data['Posts'] = Posts[0]
        return data


    def scrape_data(username):
        r = requests.get(URL)
        s = BeautifulSoup(r.text, "html.parser")
        meta = s.find('meta', property="og:description")
        nickname = s.find('meta', property="og:title")
        nickname = nickname.attrs['content']
        nickname = nickname.split("•")

        print(f"User {user} and nickname ", nickname[0])
        return parse_data(meta.attrs['content'])


    if __name__ == "__main__":
        data = scrape_data(user)
        print()
        print(user, "has", data['Followers'])
        print(user, "has", data['Following'])
        print(user, "has", data['Posts'])

if ask == "9":
    import hashlib
    from termcolor import colored

    print(colored("Hi, what is your password ?", "red"))
    password = input()

    print(colored("SHA1 Hash :", "blue"))
    sha1_pass = hashlib.sha1(password.encode())
    print(colored(sha1_pass.hexdigest(), "green"))  #

    print(colored("MD5 Hash:", "red"))
    md5_pass = hashlib.md5(password.encode())
    print(colored(md5_pass.hexdigest(), "green"))

if ask == "10":
    from urllib.request import urlopen
    import hashlib
    from termcolor import colored

    print(r"""

        _____________
       /      _      \
       [] :: (_) :: []
       [] ::::::::: []
       [] ::::::::: []
       [] ::::::::: []
       [] ::NAWAF:: []
       [_____________]
           I     I
           I_   _I
            /   \
            \   /
            (   )
            /   \
            \___/

                    """)

    hash = input("Enter your Hash :")

    pass_file = str(urlopen(
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(),
                    'UTF-8')
    pass_line = pass_file.split("\n")  # split it as element in array, becuase for loop will take around of it

    for password in pass_line:
        byte_password = bytes(password, 'UTF-8')  # read as Byte UTF-8
        hash_pw = hashlib.md5(byte_password)
        random_hashed_pw = hash_pw.hexdigest()
        if hash == random_hashed_pw:
            print(colored(f"The Password is {password}", 'green'))
            break
        else:
            print(colored("The password is wrong", "red"))
if ask == "11":
    from stegano import lsb
    ss = input("Do you want Hide msg Or Detect Msg ? [Hide/Detect] : ")
    if ss == "Hide":
        print("Hint:\nif show Error, check you are type / not \ ")
        path = input("Enter the Path of Image : ")
        secret_msg = input("type msg you want to hide in Image : ")
        secret = lsb.hide(path, secret_msg)
        name = input("Enter name of secret Image : ")

        secret.save(f"{path}/{+str(name)}")
        print("saved ..")

    elif ss == "Detect":
        try:
            path_image = input("Enter path of image : ")
            msg = lsb.reveal(path_image)
            print("The secret msg is :", msg)
        except TypeError:
            print("Sorry i can't find Image!")