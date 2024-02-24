import pyowm
class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.owm = pyowm.OWM(api_key)

    def fetch_weather(self, location):
        try:
            observation = self.owm.weather_at_place(location)
            weather = observation.get_weather()

            temperature = weather.get_temperature('celsius')['temp']
            status = weather.get_status()

            return {
                'temperature': temperature,
                'status': status,
                'location': location,
            }
        except pyowm.exceptions.api_response_error.NotFoundError:
            print('Location not found')
            return None
        except pyowm.exceptions.api_call_error.APICallError as e:
            print(f"Error fetching weather data: {e}")
            return None