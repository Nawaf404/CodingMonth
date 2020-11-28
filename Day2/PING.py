from art import * # for draw text with great shapes
import subprocess
import pyfiglet
from termcolor import colored
tprint("Nawaf",font="block",chr_ignore=True)
logo = pyfiglet.figlet_format("Ping")
print(colored(logo,"cyan"))
print(colored("---------- TechCampus, Nawaf ---------","yellow"))
print(colored("--------- Cyper Python ----------","blue"))
print("")
host = input("What is your IP :\n")
result = subprocess.call(['ping',  host], stdout=subprocess.PIPE)
# ping only, just for windows , for linux ping -c
# subprocess , call ( use connect type ping ) , ping -c ( -c option )
# stdout = time out if reach that's mean unreachable or maybe private ip
# 1 for one time only, without wait for 40 packet example, because i want check for 1 times only
# , stdout=subprocess.PIPE for hide opreate and show it
print(result)
if result == 0:
    print(colored('The Host is UP', 'green'))
else:
    print(colored('The Host is DOWN', 'red'))
