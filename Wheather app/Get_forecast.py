# Imports
import requests

def main():
    # Keys and urls
    def get_wheather(city):
        weather_key = 'fdebe23da7db60522fe2952ca445f7dd'
        url = 'http://api.openweathermap.org/data/2.5/forecast?'

        # paramaters
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}

        # the response
        response = requests.get(url, params=params)
        weather = response.json()

        return (weather)

        print(weather)


    # get the mean of temp of forecasted value
    def getMean(weather):
        SumForecatTemp = 0
        for i in range(len(weather['list'])):
            #print(weather['list'][i]['main']['temp'])
            SumForecatTemp += weather['list'][i]['main']['temp']
            #print(SumForecatTemp)
        print(SumForecatTemp)
        return (SumForecatTemp / (len(weather['list'])))


    city = 'London'
    forecastWeather = get_wheather(city)
    SumForecatTemp = getMean(forecastWeather)

    print(SumForecatTemp)

if __name__ == '__main__':
    main()