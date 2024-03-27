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
            return data, response
        except requests.RequestException as e: # all exceptions from the Request library
            print(f'Error fetching weather data: {e}')
            return None, None

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
            return None
class WeatherDisplay(Frame):
    def __init__(self, parent, api_key, city, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.configure(bg='black')
        self.weather_data = WeatherData(api_key, city)
        self.weather_widget()
        self.update_weather()

    def weather_widget(self):
        # labels for displaying weather information
        self.temp_label = Label(self, font=('Courier', 28), text="", fg='White', bg="black")
        self.temp_label.grid(row=0, column=0, padx=5, pady=3, sticky='ne')

        self.describe_label = Label(self, font=('Courier', 13), text="", fg='White', bg="black")
        self.describe_label.grid(row=1, column=0, padx=5, pady=3, sticky='ne')

        self.city_label = Label(self, font=('Courier', 13), text="", fg='White', bg="black")
        self.city_label.grid(row=2, column=0, padx=5, pady=3, sticky='ne')
    
    def update_weather(self):
        # unpacking the tuple retured by fetch_weather
        data, response = self.weather_data.fetch_weather()
        weather_info = self.weather_data.extract_weather_info(data, response)

        if weather_info:
            self.temp_label.config(text=f"{weather_info['temperature']}°C")
            self.describe_label.config(text=weather_info['description'])
            self.city_label.config(text=weather_info['city'])
        else:
            self.temp_label.config(text='Failed to retrieve weather data')

class SmartMirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.configure(background='black')
        self.root.attributes('-topmost', 1)
        self.root.attributes('-fullscreen', True)

    # Weather display frame
        self.weather_display = WeatherDisplay(root, api_key='3e28611a96f98531af8cdf8f67545878', city= 'London' )
        self.weather_display.place(relx=1, rely=0, anchor='ne')

if __name__ == "__main__":
    root = Tk()
    app = SmartMirrorApp(root)
    app.root.mainloop()