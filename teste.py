from os import close
import sys
from colorama.initialise import reinit
from requests.api import get
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from time import sleep
from tkinter import filedialog
import random
import os

link = ("https://web.whatsapp.com/")
init(autoreset=True)


browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(link)
print(Fore.BLUE + "Aguardando conexão com o WhatsApp...")
sleep(1)
manter_conectado = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input').click()
while len(browser.find_elements_by_id("side")) < 1:
    sleep(1)
print(Fore.BLUE + "Conexão bem sucedida!")


#  browser.implicitly_wait(30)  # espera a imagem ser carregada e envia
contato = 'amor'
campo_pesquisa = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
browser.implicitly_wait(30)
campo_pesquisa.click()
campo_pesquisa.send_keys(contato)   
sleep(1)             
campo_pesquisa.send_keys(Keys.ENTER)

sleep(3)

confirmacao = browser.find_element_by_css_selector('div[class="_21nHd"]').text.lower()

msg = "Os nomes são iguais"
msg2 = "Os contatos não são iguais"
if confirmacao == contato:
    campo_digitacao = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    sleep(0.5)
    campo_digitacao.click()
    campo_digitacao.send_keys(msg)

else:
    campo_digitacao = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    
    sleep(0.5)
    campo_digitacao.click()
    campo_digitacao.send_keys(msg2)

