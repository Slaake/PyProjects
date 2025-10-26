import requests

baseurl = 'https://api.weather.gov'
endpoint = '/points/'
latitude = '38.9526,' 
longitude = '-77.3411'
day = 0

fullurl = baseurl + endpoint + latitude + longitude
location_response = requests.get(fullurl)

weatherdata = location_response.json()
city = weatherdata['properties']['relativeLocation']['properties']['city']
state = weatherdata['properties']['relativeLocation']['properties']['state']
forecasturl = weatherdata['properties']['forecast']

response_forecast = requests.get(forecasturl)
forecastdata = response_forecast.json()

forecast = forecastdata['properties']['periods'][day]

def get_weather():
    print(f'Location: {city},{state}')
    print()
    day = 0
    while day < 12:
        weekday = forecastdata['properties']['periods'][day]['name']
        shortforecast = forecastdata['properties']['periods'][day]['shortForecast']
        temp = forecast = forecastdata['properties']['periods'][day]['temperature']
        rainpercent = forecastdata['properties']['periods'][day]['probabilityOfPrecipitation']['value']
        wind = forecastdata['properties']['periods'][day]['windSpeed']
        print(f'Forecast for {weekday}')
        print(f'    {shortforecast}')
        print(f'    Temperature: {temp}F degrees')
        print(f'    Chance of rain is {rainpercent}%')
        print(f'    Wind speed is {wind} mph')
        print()
        day += 2








