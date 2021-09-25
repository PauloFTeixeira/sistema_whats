"""
Leitura de arquivo .csv
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import random
import pandas


def carrega_dados(planilha_contatos):
    """
    Carregamento da base de dados
    """
    contatos = pandas.read_excel(planilha_contatos, sheet_name="Planilha1")
    print(contatos)

def enviar_mensagem():
    for i, n in enumerate(contatos['NumEddd']):
        pessoa = contatos.loc[i, 'Name']
        numero = contatos.loc[i, 'NumEddd']
        texto = urllib.parse.quote(f'*Bom dia Sr(a)* {pessoa}')
        texto2 = urllib.parse.quote(f'Estou passando para avisar que temos a disposição, sementes de Milheto e Capim Sudão')
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}%0A{texto2}"
        browser.get(link)
        tempo = random.randrange(10, 30)
        while len(browser.find_elements_by_id('side')) < 1:
            time.sleep(1)
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(5)


browser = webdriver.Chrome()
browser.get(link)
while len(browser.find_elements_by_id('side')) < 1:
    time.sleep(1)

link = ("https://web.whatsapp.com/")

nomes = [
    'Erivelton'
    'Ederson'
    'Andressa Cotrisul'
    'Carlotto'
    'Donairo - Coop'
    'Eder'
    'Fabio Detec'
    'Carlo - Coop'
    'Felipe Cervo'
    'Felipe Estoque'
    'Jocinei Indústria'
    'Kauã'
    'Lairto'
    'Lavras'
    'Leonardo Tavares'
    'Lizelbio'
    'Maikel'
    'Maikel Coop'
    'Mateus Tolfo'
    'Paulo Sérgio'
    'Rafael'
    'Roger Agrônomo'
    'Tita'
    'Ueslhei'
    'Vanderleia'
    'Zezinho'
    'Mãe'
    'Amor'
    'Eu '
    'Mackson'
]

carrega_dados("contatos.xlsx")
enviar_mensagem()


