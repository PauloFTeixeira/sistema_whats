from os import close
from colorama.initialise import reinit
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from time import sleep
import random


def Informa_contatos():
    with open('contatos_personalizado.txt', 'w') as ctt:
        nome = "****"
        nome = input('Informe o nome de seu contato: ')
        ctt.write(nome + '\n')
        while nome != 'sair':
            nome = input('Inform um contato ou "sair" para encerrar: ')
            if nome == 'sair':
                break
            ctt.write(nome + '\n')
        
    with open('contatos_personalizado.txt') as arq:
        for c in enumerate(arq.readlines()): 
            print(c)


def criar_mensagem():
    global dict_mensagens
    dict_mensagens = {}
    contador = 0
    mensagem = '***'
    while len(mensagem) > 1:
        contador = contador + 1
        mensagem = input(f'Digite sua {contador}ª mensagem: ')
        dict_mensagens[contador] = mensagem
        
    dict_mensagens.pop(contador)
    for msg in dict_mensagens:
        print(Fore.BLUE + f'{msg}, {dict_mensagens[msg]}')


def enviar_mensagem_buscando_contato(browser, nome_lista):
    """
    Envia mensagem utilizando uma lista de contatos préviamente informada, através de informação direta ou busca por contatos em arquivo .csv
    
    """
    try:
        with open(f'{nome_lista}') as lista_de_contatos:
            contatos = lista_de_contatos.readlines()
            for cont in contatos:
                contato = cont[:-1]
                campo_pesquisa = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
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


def setting_contacts():
    with open('nome_listas') as listas:
        lista = listas.readlines()
        print('As listas cadastradas são:')
        for l in lista:
            print(Fore.BLUE + f'{l}')
    nome_lista = str(input('Qual lista desaja modificar? '))
    with open(f'{nome_lista}') as nomes:
        print('Os contatos salvos nesta lista são:')
        for nome in nomes.readlines():
            print(Fore.BLUE + nome)
    acao = int(input('Escolha uma opção: [1]EDITAR UM CONTATO, [2]INCLUIR UM CONTATO, [3]EXCLUIR UM CONTATO, [0]SAIR  '))
    if acao == 1:
        with open(f'{nome_lista}', 'r+') as arq:
            arq.seek(0)
            linhas = arq.readlines()
            for l in enumerate(linhas, 0):
                print(l)
            arq.seek(0)
            id = int(input('Qual o nº que desaja alterar? '))
            alter = str(input('Informe o novo nome do contato: ') + '\n')
            linhas[id] = alter 
            arq.writelines(linhas)
            print()
            for li in enumerate(linhas, 0):
                print(li)
        setting_contacts()
    elif acao == 2:
        with open(f'{nome_lista}', 'a') as arq:
            novo = "**"
            novos = []
            while len(novo) > 0:
                novo = input('Informe o contato a ser incluido: ') 
                arq.write(novo + '\n')
                novos.append(novo)
            print(f'Os novos contatos incluídos foram {novos}')
        setting_contacts()
    elif acao == 3:
        with open(f'{nome_lista}') as arq:
            nomes = arq.readlines()
            print(nomes)
            deletar = str(input('Informe o contato a ser removido: ') + "\n")
            nomes.remove(deletar)
            print('**')
            with open ('contatos.txt', 'w') as arquivo:
                arquivo.writelines(nomes)
        setting_contacts()  


def erro():
    print('Esse nome de lista já está em uso, escolha outro nome.')
    criar_lista_contatos()


def criar_lista_contatos():
    nome_lista = input('Qual o nome da lista? ')
    try:
        with open(f'{nome_lista}', 'x'):
            pass
 #  Registra o nome da nova lista de contatos no arquivo que lista tais nomes.                
        with open('nome_listas', 'a') as nomes:
            nomes.write(f'{nome_lista}' + '\n')        
 #  Faz o registro de todos os contatos que o usuário quiser.
        with open(f'{nome_lista}', 'a') as lista:
            contato = '**'
            while contato != 'sair':
                contato = input('Informe um contato ou "sair" para encerrar: ')
                if contato == 'sair':
                    break
                lista.write(contato + '\n')
 #  Tratamento de erro, caso já haja uma lista com o nome informado
    except FileExistsError:
        erro()
            

def enviar_mensagem_contato_personalizado(browser):
    """
    Envia mensagem utilizando uma lista de contatos préviamente informada, através de informação direta ou busca por contatos em arquivo .csv
    
    """
    try:
        with open('contatos_personalizado.txt') as lista_de_contatos:
            contatos = lista_de_contatos.readlines()
            for cont in contatos:
                contato = cont[:-1]  # para remover o \n do final da string
                campo_pesquisa = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
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


def menu(functions):
    print(Fore.CYAN + '=-=' * 40)
    print('Envio de mensagens')
    print('[1]Informando contatos personalizados  |  [2]Usando Lista de contatos')
    print(Fore.CYAN + '=-=' * 40)
    print('Configurações')
    print('[3]Criar nova lista de contatos  |  [4]Alterar lista existente')
    print(Fore.CYAN + '=-=' * 40)
    print('[0]Fechar Sistema')
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
        quit()
    


