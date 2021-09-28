"""
Sistema de automação para WhatsApp

"""

#  from selenium.webdriver import Chrome
#  from selenium.webdriver import Firefox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from time import sleep
import random

init(autoreset=True)
dict_mensagens = {}
link = ("https://web.whatsapp.com/")


def Informa_contatos():
    with open('contatos.txt', 'a+') as ctt:
        nome = "****"
        nome = input('Informe o nome de seu contato: ')
        ctt.write(nome + '\n')
        while len(nome) > 1:
            nome = input('Algum outro contato? ')
            ctt.write(nome + '\n')
        
    with open('contatos.txt') as arq:
        for c in enumerate(arq.readlines()): 
            print(c)


def criar_mensagem():

    contador = 0
    mensagem = '***'
    while len(mensagem) > 1:
        contador = contador + 1
        mensagem = input(f'Digite sua {contador}ª mensagem: ')
        dict_mensagens[contador] = mensagem
        
    dict_mensagens.pop(contador)
    for msg in dict_mensagens:
        print(Fore.BLUE + f'{msg}, {dict_mensagens[msg]}')


def enviar_mensagem_buscando_contato():
    """
    Envia mensagem utilizando uma lista de contatos préviamente informada, através de informação direta ou busca por contatos em arquivo .csv
    
    """
    try:
        for contato in contatos:
            campo_pesquisa = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
            campo_pesquisa.click()
            sleep(0.25)
            campo_pesquisa.send_keys(contato)
            campo_pesquisa.send_keys(Keys.ENTER)
            
            for chave in dict_mensagens:
                msg = dict_mensagens[chave]
                tempo_entre_mensagens = float(len(msg)) * 0.15
                sleep(tempo_entre_mensagens)
                campo_digitacao = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
                campo_digitacao.click()
                campo_digitacao.send_keys(msg)
                sleep(0.05)
                enviar = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button')
                enviar.click()
            print(Fore.GREEN + f'Mensagem enviada para {contato}')
        sleep(10)
            
        browser.quit()
    except:
        print('Erro ao enviar mensagem, contate o Administrador do sistema!')


#  Execução
"""
Informa_contatos()
criar_mensagem()
navegador = int(input("Qual navegador desaja usar? (1)Chrome, (2)Firefox, (0)Cancelar: "))

try:
    if navegador == 1:
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get(link)
            print(Fore.BLUE + "Aguardando conexão com o WhatsApp...")
            sleep(1)
            manter_conectado = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input').click()
            while len(browser.find_elements_by_id("side")) < 1:
                sleep(1)
            print(Fore.GREEN + "Conexão bem sucedida!")
    elif navegador == 2:
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get(link)
            print(Fore.BLUE + "Aguardando conexão com o WhatsApp...")
            sleep(1)
            manter_conectado = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input').click()
            while len(browser.find_elements_by_id("side")) < 1:
                sleep(1)
            print(Fore.GREEN + "Conexão bem sucedida!")
    elif navegador == 0:
            exit()
    else:
        abrir_navegador()
except:
    print(Fore.RED + 'Conexão mal sucedida!')

enviar_mensagem_buscando_contato()
"""
Informa_contatos()

