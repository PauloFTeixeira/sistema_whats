
"""contatos = []
def Informa_contatos():
    nome = "****"
    nome = input('Informe um nome de seus contatos: ')
    contatos.append(nome.title())
    while len(nome) > 1:
        nome = input('Algum outro nome? ')
        contatos.append(nome.title())
    contatos.pop()

Informa_contatos()
print(contatos)

import time



mensagem = 'Um texto é, maioritariamente, um conjunto organizado de palavras, que formam frases, que formam parágrafos, que formam o próprio texto.\nEssa unidade estruturada apresenta um sentido completo e tem um objetivo comunicativo.'
def __digitar__(mensagem):
    for letra in mensagem:
        print(letra, end="")
        time.sleep(0.1)

dict_mensagens = {}

def criar_mensagem():
    contador = 0
    mensagem = '***'
    while len(mensagem) > 1:
        contador = contador + 1
        mensagem = input(f'Digite sua {contador}ª mensagem: ')
        dict_mensagens[contador] = mensagem
        
    dict_mensagens.pop(contador)
    print(dict_mensagens)

criar_mensagem()

for c in dict_mensagens:
    print(dict_mensagens[c])




from time import sleep

msg = 'aaaaaaaaaaaaa'
msg2 = 'bbbbbbbbbbbbbbbbbbbb'
len_msg = float(len(msg))
len_msg2 = float(len(msg2))
#tempo = len_msg * 0.01
#tempo2 = len_msg2 * 0.01


tempo = float(len(msg)) * 0.01
tempo2 = float(len(msg2)) * 0.01
print(tempo)
print()
print(tempo2)
"""