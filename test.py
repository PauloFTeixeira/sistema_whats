from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

link = ("https://www.americanas.com.br/")

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(link)

pesquisa = browser.find_element_by_css_selector('input[id="h_search-input"]')
