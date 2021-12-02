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
campo_pesquisa.click()
sleep(0.5)
campo_pesquisa.send_keys(contato)                
campo_pesquisa.send_keys(Keys.ENTER)

sleep(3)
#  nome_confirmacao = browser.find_element_by_css_selector('span[dir="auto"]')

#  nome_confirmacao = browser.find_element_by_css_selector('div[role="button"]')

#  nome_confirmacao = browser.find_element_by_css_selector('.class="_24-Ff"[role="button"]')

#  nome_confirmacao = browser.find_element_by_css_selector('div[.class="_24-Ff"]')

#  nome_confirmacao = browser.find_element_by_css_selector('span[dir="auto"], [title="Amor"]').text

superior = browser.find_element_by_class_name('_2YnE3')
sleep(2)
superior.click()

n = browser.find_element_by_class_name('_2P1rL _1is6W RVTrW').find_element_by_tag_name(h2).text

print(n)


#  EX.: b.find_elements_by_class_name('//nome da classe').find_element_by_id('//valor do id')
"""
    EXEMPLO: Buscando uma classe chamada linguagens: 
classe = b.find_elements_by_class_name('linguagens')  # irá retornar uma lista
for c in classe:
    print(c.find_element_by_tag_name(h2).text)  # imprimi o texto contigo dentro da TAG h2
"""






#  <span dir="auto" title="Amor" class="emoji-texttt _ccCW FqYAR i0jNr">Amor</span>
#  <div class="_21nHd"><span dir="auto" title="Amor" class="emoji-texttt _ccCW FqYAR i0jNr">Amor</span></div>
#  <div class="_2YnE3" role="button"><div class="_3GlyB" style="height: 40px; width: 40px;"><div class="_1lPgH"><span data-testid="default-user" data-icon="default-user" class=""><svg viewBox="0 0 212 212" width="212" height="212" class=""><path fill="#DFE5E7" class="background" d="M106.251.5C164.653.5 212 47.846 212 106.25S164.653 212 106.25 212C47.846 212 .5 164.654.5 106.25S47.846.5 106.251.5z"></path><path fill="#FFF" class="primary" d="M173.561 171.615a62.767 62.767 0 0 0-2.065-2.955 67.7 67.7 0 0 0-2.608-3.299 70.112 70.112 0 0 0-3.184-3.527 71.097 71.097 0 0 0-5.924-5.47 72.458 72.458 0 0 0-10.204-7.026 75.2 75.2 0 0 0-5.98-3.055c-.062-.028-.118-.059-.18-.087-9.792-4.44-22.106-7.529-37.416-7.529s-27.624 3.089-37.416 7.529c-.338.153-.653.318-.985.474a75.37 75.37 0 0 0-6.229 3.298 72.589 72.589 0 0 0-9.15 6.395 71.243 71.243 0 0 0-5.924 5.47 70.064 70.064 0 0 0-3.184 3.527 67.142 67.142 0 0 0-2.609 3.299 63.292 63.292 0 0 0-2.065 2.955 56.33 56.33 0 0 0-1.447 2.324c-.033.056-.073.119-.104.174a47.92 47.92 0 0 0-1.07 1.926c-.559 1.068-.818 1.678-.818 1.678v.398c18.285 17.927 43.322 28.985 70.945 28.985 27.678 0 52.761-11.103 71.055-29.095v-.289s-.619-1.45-1.992-3.778a58.346 58.346 0 0 0-1.446-2.322zM106.002 125.5c2.645 0 5.212-.253 7.68-.737a38.272 38.272 0 0 0 3.624-.896 37.124 37.124 0 0 0 5.12-1.958 36.307 36.307 0 0 0 6.15-3.67 35.923 35.923 0 0 0 9.489-10.48 36.558 36.558 0 0 0 2.422-4.84 37.051 37.051 0 0 0 1.716-5.25c.299-1.208.542-2.443.725-3.701.275-1.887.417-3.827.417-5.811s-.142-3.925-.417-5.811a38.734 38.734 0 0 0-1.215-5.494 36.68 36.68 0 0 0-3.648-8.298 35.923 35.923 0 0 0-9.489-10.48 36.347 36.347 0 0 0-6.15-3.67 37.124 37.124 0 0 0-5.12-1.958 37.67 37.67 0 0 0-3.624-.896 39.875 39.875 0 0 0-7.68-.737c-21.162 0-37.345 16.183-37.345 37.345 0 21.159 16.183 37.342 37.345 37.342z"></path></svg></span></div><img src="https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F165558981_4393969970682441_1303667213280299184_n.jpg%3Fccb%3D11-4%26oh%3Df7552e76ba1448f7501fec912e6df357%26oe%3D617EAEDA&amp;t=s&amp;u=555596718866%40c.us&amp;i=1634331213&amp;n=X%2BN9K0%2BSKvVc0%2BO6%2BWGmbc5lVZXF0N21Nnp%2Bqd%2FFz1s%3D" alt="" draggable="false" class="_8hzr9 M0JmA i0jNr" style="visibility: visible;"></div></div>

#  <h2 class="_3WYXy VWPRY _1lF7t"><span dir="auto" class="emoji-texttt FqYAR i0jNr selectable-text copyable-text">Amor</span></h2>
#  <div class="_2P1rL _1is6W RVTrW"><div class="p357zi0d ac2vgrno du8bjn1j"><div class="_3GlyB" style="height: 200px; width: 200px; cursor: pointer;"><div class="_1lPgH"><span data-testid="default-user" data-icon="default-user" class=""><svg viewBox="0 0 212 212" width="212" height="212" class=""><path fill="#DFE5E7" class="background" d="M106.251.5C164.653.5 212 47.846 212 106.25S164.653 212 106.25 212C47.846 212 .5 164.654.5 106.25S47.846.5 106.251.5z"></path><path fill="#FFF" class="primary" d="M173.561 171.615a62.767 62.767 0 0 0-2.065-2.955 67.7 67.7 0 0 0-2.608-3.299 70.112 70.112 0 0 0-3.184-3.527 71.097 71.097 0 0 0-5.924-5.47 72.458 72.458 0 0 0-10.204-7.026 75.2 75.2 0 0 0-5.98-3.055c-.062-.028-.118-.059-.18-.087-9.792-4.44-22.106-7.529-37.416-7.529s-27.624 3.089-37.416 7.529c-.338.153-.653.318-.985.474a75.37 75.37 0 0 0-6.229 3.298 72.589 72.589 0 0 0-9.15 6.395 71.243 71.243 0 0 0-5.924 5.47 70.064 70.064 0 0 0-3.184 3.527 67.142 67.142 0 0 0-2.609 3.299 63.292 63.292 0 0 0-2.065 2.955 56.33 56.33 0 0 0-1.447 2.324c-.033.056-.073.119-.104.174a47.92 47.92 0 0 0-1.07 1.926c-.559 1.068-.818 1.678-.818 1.678v.398c18.285 17.927 43.322 28.985 70.945 28.985 27.678 0 52.761-11.103 71.055-29.095v-.289s-.619-1.45-1.992-3.778a58.346 58.346 0 0 0-1.446-2.322zM106.002 125.5c2.645 0 5.212-.253 7.68-.737a38.272 38.272 0 0 0 3.624-.896 37.124 37.124 0 0 0 5.12-1.958 36.307 36.307 0 0 0 6.15-3.67 35.923 35.923 0 0 0 9.489-10.48 36.558 36.558 0 0 0 2.422-4.84 37.051 37.051 0 0 0 1.716-5.25c.299-1.208.542-2.443.725-3.701.275-1.887.417-3.827.417-5.811s-.142-3.925-.417-5.811a38.734 38.734 0 0 0-1.215-5.494 36.68 36.68 0 0 0-3.648-8.298 35.923 35.923 0 0 0-9.489-10.48 36.347 36.347 0 0 0-6.15-3.67 37.124 37.124 0 0 0-5.12-1.958 37.67 37.67 0 0 0-3.624-.896 39.875 39.875 0 0 0-7.68-.737c-21.162 0-37.345 16.183-37.345 37.345 0 21.159 16.183 37.342 37.345 37.342z"></path></svg></span></div><img src="https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F165558981_4393969970682441_1303667213280299184_n.jpg%3Fccb%3D11-4%26oh%3Df7552e76ba1448f7501fec912e6df357%26oe%3D617EAEDA&amp;t=l&amp;u=555596718866%40c.us&amp;i=1634331213&amp;n=X%2BN9K0%2BSKvVc0%2BO6%2BWGmbc5lVZXF0N21Nnp%2Bqd%2FFz1s%3D" alt="" draggable="false" class="_8hzr9 M0JmA i0jNr" style="visibility: visible;"></div></div><h2 class="_3WYXy VWPRY _1lF7t"><span dir="auto" class="emoji-texttt FqYAR i0jNr selectable-text copyable-text">Amor</span></h2><div class="g4oj0cdv g1eqewly gfz4du6o r7fjleex hp667wtd lhj4utae le5p0ye3"><span class="_3Bg5b VWPRY _1lF7t"></span><span class="_3Bg5b VWPRY _1lF7t"></span></div></div>