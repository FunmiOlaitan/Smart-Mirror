import pyowm
class WeatherData:
    def __init_(api_key):
        self.api_key = api_key
        self.own = pyown.OWM(api_key)

    def fetch_weather(self, location):
        try:
            london = self.own.weather_at_place('London, GB')
            weather = london.get_weather()

            temperature = weather.get_temperature('celsius')['temp']
            status = weather.get_status()

            return {
                'temperature': temperature,
                'status': status,
                'location': location,
            }
        except pyown.expetion.api_response_error.NotFoundError:
            print('Location not found')
            return None 
        except pyowm.exceptions.api_call_error.APICallError as e:
            print(f"Error fetching weather data: {e}")
            return None


