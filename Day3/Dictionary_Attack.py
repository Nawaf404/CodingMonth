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

hash = "202cb962ac59075b964b07152d234b70"

pass_file = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'UTF-8')
pass_line = pass_file.split("\n") # split it as element in array, becuase for loop will take around of it

for password in pass_line:
    byte_password = bytes(password, 'UTF-8') # read as Byte UTF-8
    hash_pw = hashlib.md5(byte_password)
    random_hashed_pw = hash_pw.hexdigest()
    if hash == random_hashed_pw:
        print(colored(f"The Password is {password}", 'green'))
        break
    else:
        print(colored("The password is wrong", "red"))
