import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.amazon.ae/whitefriday/")
print("Code Of HTTP : ", response)
# 200 is ok, 300 redirect, 400 for visitor
# help you in parsin
# XML = for store datas like json, use it in API almost
content = response.text
print(content) # will print html tags

soup = BeautifulSoup(content, 'html.parser')
# name of module , use content and read it as html parser
for link in soup.find_all('img'):
    # soup.find_all('a') will print all of a, include href , clases, everything
    print(link.get('src'))
    # type link.get(choose tags to show)

# API = Application Programming Interface
