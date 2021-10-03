"""
funçao
"""

def setting_contacts():
    acao = int(input('Escolha uma opção: [1]EDITAR UM CONTATO, [2]INCLUIR UM CONTATO, [3]EXCLUIR UM CONTATO, [0]SAIR  '))
    if acao == 1:
        with open('contatos.txt', 'r+') as arq:
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
        with open('contatos.txt', 'a') as arq:
            novo = "**"
            novos = []
            while len(novo) > 0:
                novo = input('Informe o contato a ser incluido: ') 
                arq.write(novo + '\n')
                novos.append(novo)
            print(f'Os novos contatos incluídos foram {novos}')
        setting_contacts()
    elif acao == 3:
        with open('contatos.txt') as arq:
            nomes = arq.readlines()
            print(nomes)
            deletar = str(input('Informe o contato a ser removido: ') + "\n")
            nomes.remove(deletar)
            print('**')
            with open ('contatos.txt', 'w') as arquivo:
                arquivo.writelines(nomes)
        setting_contacts()          

setting_contacts()


