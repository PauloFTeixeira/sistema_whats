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

print(Fore.CYAN + '=-=' * 40)
print('Envio de mensagens')
print('[1]Informando contatos personalizados  |  [2]Usando Lista de contatos')
print(Fore.CYAN + '=-=' * 40)
print('Configurações')
print('[3]Criar nova lista de contatos  |  [4]Alterar lista existente')
print(Fore.CYAN + '=-=' * 40)
print('[0]Sair')
print(Fore.CYAN + '=-=' * 40)
opcao = int(input('Escolha qual a opção deseja: '))

if opcao == 1:
    functions.Informa_contatos()
    functions.criar_mensagem()
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
                print(Fore.BLUE + "Conexão bem sucedida!")
        elif navegador == 2:
                browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                browser.get(link)
                print(Fore.BLUE + "Aguardando conexão com o WhatsApp...")
                sleep(1)
                manter_conectado = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input').click()
                while len(browser.find_elements_by_id("side")) < 1:
                    sleep(1)
                print(Fore.BLUE + "Conexão bem sucedida!")
        elif navegador == 0:
                exit()
        functions.enviar_mensagem_contato_personalizado(browser)
    except:
        print(Fore.RED + 'Conexão mal sucedida!')

elif opcao == 2:
    with open('nome_listas') as listas_salvas:
        nome = listas_salvas.readlines()
        for n in nome:
            print(n)
    nome_lista = str(input('Informe o nome da lista que desaja usar: '))
    functions.criar_mensagem()
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
                print(Fore.BLUE + "Conexão bem sucedida!")
        elif navegador == 2:
                browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                browser.get(link)
                print(Fore.BLUE + "Aguardando conexão com o WhatsApp...")
                sleep(1)
                manter_conectado = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input').click()
                while len(browser.find_elements_by_id("side")) < 1:
                    sleep(1)
                print(Fore.BLUE + "Conexão bem sucedida!")
        elif navegador == 0:
                exit()
        functions.enviar_mensagem_buscando_contato(browser, nome_lista)
    except:
        print(Fore.RED + 'Conexão mal sucedida!')

elif opcao == 3:
    functions.criar_lista_contatos()

elif opcao == 4:
    functions.setting_contacts()

elif opcao == 0:
    close()
    

