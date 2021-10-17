from os import close
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from time import sleep
from tkinter import filedialog
import random
import functions
import os


init(autoreset=True)
link = ("https://web.whatsapp.com/")

while True:
    functions.menu(functions, link)  


