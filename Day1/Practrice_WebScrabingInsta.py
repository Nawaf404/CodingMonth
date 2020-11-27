'''
html tags in web page
<meta property="og:type" content="profile" />
            <meta property="og:image" content="https://instagram.fruh4-1.fna.fbcdn.net/v/t51.2885-19/s150x150/127090099_378308690153951_6863632313025658797_n.jpg?_nc_ht=instagram.fruh4-1.fna.fbcdn.net&_nc_ohc=3JlkcUCBV-EAX9D1FoM&tp=1&oh=745a7d155142cc7b8826f78c53d2702c&oe=5FEB838C" />
            <meta property="og:title" content="‏★𓅔سكويز (@skoiiiz) • Instagram photos and videos" />
            <meta property="og:description" content="75.6k Followers, 1,436 Following, 10k Posts - See Instagram photos and videos from ‏★𓅔سكويز (@skoiiiz)" />
            <meta property="og:url" content="https://www.instagram.com/skoiiiz/" />
'''

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
    #print(s)
    s = s.split(",")
    #print(s)

    data['Followers'] = s[0]
    data['Following'] = s[2]
    Posts = s[3]
    Posts = Posts.split("-")
    #print(Posts)
    data['Posts'] = Posts[0]
    return data

def scrape_data(username):
    r = requests.get(URL)
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find('meta',property="og:description")
    nickname = s.find('meta',property="og:title")
    nickname = nickname.attrs['content']
    nickname = nickname.split("•")

    print(f"User {user} and nickname ",nickname[0])
    return parse_data(meta.attrs['content'])

if __name__ == "__main__":
    data = scrape_data(user)
    print()
    print(user, "has", data['Followers'])
    print(user, "has", data['Following'])
    print(user, "has", data['Posts'])


'''
Outout :
Enter your Username : skoiiiz
75.6k Followers, 1,436 Following, 10k Posts - See Instagram photos and videos from ‏★𓅔سكويز (@skoiiiz)
['75.6k Followers', ' 1', '436 Following', ' 10k Posts - See Instagram photos and videos from \u200f★𓅔سكويز (@skoiiiz)']
[' 10k Posts ', ' See Instagram photos and videos from \u200f★𓅔سكويز (@skoiiiz)']
Working Now .. 
{'Followers': '75.6k Followers', 'Following': '436 Following', 'Posts': ' 10k Posts '}
skoiiiz has 75.6k Followers
skoiiiz has 436 Following
skoiiiz has  10k Posts 

'''