import requests


class Weather:

    def __init__(self, city):
        self.appID = "646e265287f3dda66934a3d756298741"
        self.city = city

    def __load_data(self):
        try:
            return requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + self.city + "&APPID=" +
                                self.appID).json()
        except:
            print("error occurred, status code :", requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +
                                                                self.city + "&APPID=" + self.appID).status_code)

    def get_temperature(self):
        return self.__load_data()['main']['temp'] - 273

    def get_weather(self):
        return self.__load_data()['weather'][0]['main']

    def is_cloudy(self):
        cloudy_percent = self.__load_data()['clouds']['all']
        if cloudy_percent < 35:
            return False
        else:
            return True

    def get_weather_description(self):
        return self.__load_data()['weather'][0]['description']

    def get_humidity(self):
        return self.__load_data()['main']['humidity']

    def get_wind_speed(self):
        return self.__load_data()['wind']['speed']



# result = 'Temperature in London is {:.1f} degrees Celsius'.format(data['main']['temp'] - 273)

