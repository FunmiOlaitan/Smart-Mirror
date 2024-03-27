from tkinter import Tk, Frame, Label
import requests

# class to fetch weather data 
class WeatherData:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    def fetch_weather(self): # method to fetch weather data from the API
        try:
            response = requests.get(self.url) # send an HTTP GET request to the url
            data = response.json() # save data in JSON 
        except requests.RequestException as e: # all exceptions from the Request library
            print(f'Error fetching weather data: {e}')
            return None
    
    def extract_weather_info(self):
        pass

class SmartMirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.configure(background='black')
        self.root.attributes('-topmost', 1)
        self.root.attributes('-fullscreen', True)

if __name__ == "__main__":
    root = Tk()
    app = SmartMirrorApp(root)
    app.root.mainloop()