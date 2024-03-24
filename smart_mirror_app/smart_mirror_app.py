from tkinter import Tk, Frame, Label
from datetime import datetime
import pyowm

class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.own = pyowm.OWM(api_key) # authentication connection to the api

    def fetch_weather(self, location):
        try:
            # Fetch weather for a specified location
            observation = self.owm.weather_at_place(location)
            weather = observation.get_weather()
            
            temperature = weather.get_temperature('celsius')['temp']
            status = weather.get_status()

            # Return weather data as a dictionary
            return{
                'location': location,
                'status': status,
                'temperature': temperature
            }
        except pyowm.exceptions.api_response_error.NotFoundError:
            print('Location not found')
            return None
        except pyowm.exceptions.api_call_error.APICallError as e:
            print(f"Error fetching weather data: {e}")
            return None

class SmartMirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mirror")
        self.root.geometry("1920x1080")
        self.root.configure(background='black')
        self.root.attributes('-topmost', 1)
        self.root.attributes('-fullscreen', True)
        # self.root.iconbitmap('mirror_86251.ico')


if __name__ == "__main__":
    root = Tk()
    app = SmartMirrorApp(root)
    app.root.mainloop()