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

    def extract_weather_info(self, data, response):  # method to handle response received 
        if response.status_code == 200:   # if request is successfull extract information
           temperature = data['main']['temp']
           weather_description = data['weather'][0]['description']
           # return information as dictionary
           return {
               "temperature": temperature,
               "description": weather_description,
               "city": self.city
           }
        else:
            print("Failed to retrieve weather data")
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