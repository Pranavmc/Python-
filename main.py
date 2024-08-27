import requests
from pprint import pprint
API_Key='dad2d1447ad00dba8fc84b5d1883ba2a'
city=input("enter the city:-")
base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)

