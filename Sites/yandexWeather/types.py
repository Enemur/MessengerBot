class WeatherData:
    def __init__(self, temp: str, wind: str,
                 pressure: str, humidity: str, typeWeather: str, time: str):
        self.temp = temp
        self.wind = wind
        self.pressure = pressure
        self.humidity = humidity
        self.time = time
        self.typeWeather = typeWeather

    def __str__(self):
        return f'температура: {self.temp}, ветер: {self.wind},' \
        f'давеление: {self.pressure}, влажность: {self.humidity}, погода: {self.typeWeather},' \
        f'время: {self.time}'