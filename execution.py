from os import close
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from time import sleep
import random
import functions

init(autoreset=True)
link = ("https://web.whatsapp.com/")

while True:
    functions.menu(functions)  

