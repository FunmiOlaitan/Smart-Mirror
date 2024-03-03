from tkinter import Tk, Frame, Label
from datetime import datetime

# Importing modules
from modules.weather_data import WeatherData
from modules.news_data import NewsData

class SmartMirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mirror")
        self.root.geometry("1920x1080")
        self.root.configure(background='black')
        self.root.attributes('-topmost', 1)
        self.root.attributes('fullscreen', True) 
        self.root.iconbitmap("mirror_86251.ico")

        # Initialize weather data and news data objects
        self.weather_data = WeatherData()
        self.news_data = NewsData()