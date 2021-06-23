import requests
from datetime import datetime
api_key="07e4ad9cf9ccbd324a0280bc24225c5a"
location=input("enter the city name: ")
com_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(com_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp']-273.15))
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("...................................................................")
print("weather stats for -{} || {}".format(location.upper(),date_time))
print("...................................................................")
 
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


'''
output:
enter the city name: anantapur
...................................................................
weather stats for -ANANTAPUR || 23 Jun 21 | 11:15:51 AM
...................................................................
Current temperature is: 32.58 deg C
Current weather desc  : overcast clouds
Current Humidity      : 41 %
Current wind speed    : 5.09 kmph
>>> 
'''


    
