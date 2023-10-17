import requests,json
api = "1fdef6bf7c4eff26d594b8049a075cec"
base = "http://api.openweathermap.org/data/2.5/weather?"
cname = input("Enter city name : ")
complete = base + "appid=" + api + "&q=" + cname
response = requests.get(complete)
x = response.json()
if x["cod"] != "404":
	y = x["main"]
	temp = y["temp"]
	pressure = y["pressure"]
	humidity = y["humidity"]
	z = x["weather"]
	weather_desc = z[0]["description"]
	
	print(" Temperature (in kelvin unit) = " + str(temp) +
              "\n atmospheric pressure (in hPa unit) = " + str(pressure) +
	      "\n humidity (in percentage) = " + str(humidity) +
	      "\n description = " + str(weather_desc))
else:
	print(" City Not Found ")
