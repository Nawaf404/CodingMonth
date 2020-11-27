import requests
api_address = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input("Hi, What's your city name :\n")
url = api_address + city
json_data = requests.get(url).json()
main_weather = json_data['weather'][0]['description']
country = json_data['country']
print(country,"\n",main_weather)