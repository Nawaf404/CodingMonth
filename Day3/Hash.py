import hashlib
from termcolor import colored
print(colored("Hi, what is your password ?","red"))
password = input()

print(colored("SHA1 Hash :","blue"))
sha1_pass = hashlib.sha1(password.encode())
print(colored(sha1_pass.hexdigest(),"green")) #

print(colored("MD5 Hash:","red"))
md5_pass = hashlib.md5(password.encode())
print(colored(md5_pass.hexdigest(),"green"))