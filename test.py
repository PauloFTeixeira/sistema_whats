

id = 1

if id == 0:
    with open('contatos.txt', 'r+') as arq:
            arq.seek(0)
            linhas = arq.readlines()
            for l in enumerate(linhas, 0):
                print(l)
            arq.seek(0)
            id = input('Qual o nº que desaja alterar? ')
            alter = input('Informe o novo nome do contato: ')
            linhas[id] = (alter + '\n')
            arq.writelines(linhas)
            print()
            for li in enumerate(linhas, 0):
                print(li)


