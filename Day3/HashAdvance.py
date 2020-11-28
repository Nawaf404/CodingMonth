print(r"""

                                   ._ o o
                                   \_`-)|_
                                ,""       \
                              ,"  ## |   ಠ ಠ.
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)
print("--------- TechCampus.com ---------")
print("---------  Cyber Python  ---------")
print("")

import hashlib
import sys
print("prefer type password with kind of hashing (md5 or sha1)")
if len(sys.argv) == 1 : sys.exit("Hashing error! please check the options.")
try:
    password = sys.argv[1]
    hash = sys.argv[2]
    if hash == "md5":
        md5_pass = hashlib.md5(password.encode())
        print("MD5 Hash :")
        print(md5_pass.hexdigest())
    elif hash == "sha1":
        sha1_pass = hashlib.sha1(password.encode())
        print("SHA1 Hash:")
        print(sha1_pass.hexdigest())
    else:
        print("Sorry i don't get it")
except IndexError:
    print("Sorry must type two parameter")
