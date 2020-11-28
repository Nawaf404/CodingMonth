# Steganography

# C:\Users\nawaf\Desktop
print(r"""

           _ . - = - . _
       . "  \  \   /  /  " .
     ,  \                 /  .
   . \   _,.--~=~"~=~--.._   / .
  ;  _.-"  / \ !   ! / \  "-._  .
 / ,"     / ,` .---. `, \     ". \
/.'   `~  |   /:::::\   |  ~`   '.\
\`.  `~   |   \:::::/   | ~`  ~ .'/
 \ `.  `~ \ `, `~~~' ,` /   ~`.' /
  .  "-._  \ / !   ! \ /  _.-"  .
   ./    "=~~.._  _..~~=`"    \.
     ,/         ""          \,
      . _/             \_ . 
          " - ./. .\. - "

                """)
# pip install stegano
from stegano import lsb
#secret = lsb.hide("C:/Users/nawaf/Desktop/CodingMonthLogo.png", "HELLO WORLD!, you solve the Challenge !")
#secret.save("C:/Users/nawaf/Desktop/CodingSecret.png")

msg = lsb.reveal('C:/Users/nawaf/Desktop/CodingSecret.png')
print("The secret msg is :", msg)