'''
@author "Lucas Pizoni Flôres"

    Funções Estudadas Usadas:

    - lista.count(item)
    --------------------------------
    - lista.append(item)
    - lista.insert(indice, item)
    --------------------------------
    - lista.index(item)
    --------------------------------
    - lista.remove(item)
    - lista.pop(indice)

    
Este programa foi criado com o objetivo de concluir uma atividade da matéria de 
Estrutura de Dados que envolvia gerenciar uma lista na linguagem de programação
Python.

O programa consiste em receber comandos e dados do usuário para, dessa maneira, 
inserir itens, pesquisar elementos, excluir itens e mostrar todos os elementos
da lista gerenciada.

Não foi obrigatório, mas adicionei a opção de gerar e ler arquivos de texto na lista.
'''

# ========================================================================================
#   0. DECLARAÇÕES DE MÓDULOS E DICIONÁRIO
# ========================================================================================


from os import system, path

lista = []
cores = {
        'padrao': '\033[m',
        'azul': '\033[1;36m',
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m'
    }


# ========================================================================================
#   1. FUNÇÕES DE SERVIÇO
# ========================================================================================


def limpar_console():
    system('cls')


def avisar_erro(erro):
    limpar_console()
    if type(erro) is int:
        match erro:
            case 0:
                print(f'\n{cores["vermelho"]}{"ERRO: COMANDO INVÁLIDO":=^70}{cores["padrao"]}')
                print(f'Log: COMANDO NÃO EXISTE')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case 1:
                print(f'\n{cores["vermelho"]}{"ERRO: ÍNDICE INVÁLIDO":=^70}{cores["padrao"]}')
                print(f'Log: ÍNDICE NÃO EXISTE NA LISTA')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case 2:
                print(f'\n{cores["vermelho"]}{"ERRO: SEM ÍNDICES E ITENS":=^70}{cores["padrao"]}')
                print(f'Log: LISTA VAZIA')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case 3:
                print(f'\n{cores["vermelho"]}{"ERRO: ITEM INVÁLIDO":=^70}{cores["padrao"]}')
                print(f'Log: ITEM NÃO EXISTE NA LISTA')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case 4:
                print(f'\n{cores["vermelho"]}{"ERRO: ITEM JÁ FOI REGISTRADO":=^70}{cores["padrao"]}')
                print(f'Log: NÃO PODE HAVER ITENS IGUAIS NA LISTA')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case 5:
                print(f'\n{cores["vermelho"]}{"ERRO: ARQUIVO NÃO EXISTE":=^70}{cores["padrao"]}')
                print(f'Log: ARQUIVO NÃO FOI ENCONTRADO')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

            case _:
                print(f'\n{cores["vermelho"]}{"ERRO DESCONHECIDO":=^70}{cores["padrao"]}')
                print(f'Log: ERRO NÃO LISTADO')
                print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

    else:
        print(f'\n{cores["vermelho"]}{"ERRO":=^70}{cores["padrao"]}')
        print(f'Log: {erro}')
        print(f'{cores["vermelho"]}{"=":=^70}{cores["padrao"]}\n')

    EncerrarMensagem = input(f'{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ')   


def validar_comando(comando):
    if comando in ['A', 'B']:
        return True
    else:
        avisar_erro(0)
        return False


def validar_indice(indice):
    if type(indice) is int:
        if 0 <= indice < len(lista):
            return True
        else:
            avisar_erro(1)
            return False
    else:
        avisar_erro(1)
        return False
    

def validar_item(item):
    if item in lista:
        return True
    else:
        avisar_erro(3)
        return False
    
    
def procurar_itens_iguais(item):
    if lista.count(item) > 0:
        avisar_erro(4)
        return True
    else:
        return False


def inserir_item(item, indice):
    OperacaoConcluida = False

    if indice == None:
        lista.append(item)
        OperacaoConcluida = True

    elif validar_indice(indice):
        lista.insert(indice, item)
        OperacaoConcluida = True

    if OperacaoConcluida:
        limpar_console()
        print(f'{cores["verde"]}{" ITEM ADICIONADO ":=^70}{cores["padrao"]}')
        print(f'\nITEM: {cores["azul"]}{item}{cores["padrao"]} | Índice: {cores["azul"]}{lista.index(item)}{cores["padrao"]}')

        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ')  


def pesquisar_item(item, indice):
    limpar_console()
    OperacaoConcluida = False

    if indice == None:
        if validar_item(item):
            print(f'{cores["verde"]}{"ITEM ENCONTRADO":=^70}{cores["padrao"]}')
            print(f'\nItem: {cores["azul"]}{item}{cores["padrao"]} | Índice: {cores["azul"]}{lista.index(item)}{cores["padrao"]}')
            OperacaoConcluida = True

    elif validar_indice(indice) and item == None:
        print(f'{cores["verde"]}{"ITEM ENCONTRADO":=^70}{cores["padrao"]}')
        print(f'\nItem: {cores["azul"]}{lista[indice]}{cores["padrao"]} | Índice: {cores["azul"]}{indice}{cores["padrao"]}')
        OperacaoConcluida = True

    if OperacaoConcluida:
        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ') 


def excluir_item(item, indice):
    OperacaoConcluida = False

    if indice == None:
        if validar_item(item):
            indiceDeletado = lista.index(item)
            lista.remove(item)
            OperacaoConcluida = True

    elif validar_indice(indice):
        indiceDeletado = indice
        item = lista.pop(indice)
        OperacaoConcluida = True

    if OperacaoConcluida:
        limpar_console()
        print(f'{cores["vermelho"]}{" ITEM EXCLUÍDO ":=^70}{cores["padrao"]}')
        print(f'\nitem EXCLUÍDO: {cores["azul"]}{item}{cores["padrao"]} || Índice EXCLUÍDO: {cores["azul"]}{indiceDeletado}{cores["padrao"]}')

        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ') 
    

def mostrar_lista():
    if len(lista) > 0:
        limpar_console()
        print(f'{cores["verde"]}{"ITENS DA LISTA":=^70}{cores["padrao"]}')
        Contador = -1
        for item in lista:
            Contador += 1
            print(f'Índice - {cores["azul"]}{Contador}{cores["padrao"]} | Item - {cores["azul"]}{item}{cores["padrao"]}')

        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ')  
    else:
        avisar_erro(2)


'''
Lembre-se:
- 'r'  -> Para ler algo
- 'w'  -> Para escrever algo
- 'r+' -> Para ler e escrever algo
- 'a'  -> Para acrescentar algo
'''


def gerar_arquivo():
    try: 
        caminho_arquivo = './texto/lista.txt'
        if path.exists(caminho_arquivo):
            Contador = 1
            while path.exists(caminho_arquivo):
                caminho_arquivo = f'./texto/lista({Contador}).txt'
                Contador += 1

        with open(caminho_arquivo, 'w') as arquivo:
            for item in lista:
                arquivo.write(item+'\n')

        limpar_console()
        print(f'{cores["verde"]}{"="*70}')
        print(f'{"ARQUIVO DE TEXTO CRIADO":=^70}')
        print(f'{"="*70}{cores["padrao"]}')
        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ')  

    except (IOError, NameError) as erro:
        avisar_erro(erro)


def receber_caminho(caminho):
    if path.exists(caminho):
        return caminho
    elif path.exists('./texto/'+ caminho):
        return './texto/'+ caminho
    elif path.exists('./texto/'+ caminho + '.txt'):
        return './texto/'+ caminho + '.txt'
    else:
        return ''

def ler_arquivo(caminho):
    caminho = receber_caminho(caminho)
    if len(caminho) > 0:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                lista.append(linha.replace('\n',''))

        limpar_console()
        print(f'{cores["verde"]}{"="*70}')
        print(f'{"O ARQUIVO FOI LIDO":=^70}')
        print(f'{"="*70}{cores["padrao"]}')
        EncerrarMensagem = input(f'\n{cores["verde"]}Pressione "ENTER" para continuar{cores["padrao"]} ')
        
    else:
        avisar_erro(5)


# ========================================================================================
#   2. FUNÇÕES DE INTERFACE
# ========================================================================================


def menu_principal():
    limpar_console()
    print(f'{cores["azul"]}1{cores["padrao"]} - Inserir item na lista')
    print(f'{cores["azul"]}2{cores["padrao"]} - Pesquisar item na lista')
    print(f'{cores["azul"]}3{cores["padrao"]} - Excluir um item da lista')
    print(f'{cores["azul"]}4{cores["padrao"]} - Imprimir items da lista')
    print(f'{cores["azul"]}5{cores["padrao"]} - Arquivos de texto')
    print(f'{cores["vermelho"]}0{cores["padrao"]} - Encerrar o programa')

    ComandoDoUsuario = input(f'\n{cores["verde"]}Seu Comando ?:{cores["padrao"]} ')
    return ComandoDoUsuario


def menu_inserir():
    limpar_console()
    print(f'{cores["azul"]}A{cores["padrao"]} - Inserir item na última posição')
    print(f'{cores["azul"]}B{cores["padrao"]} - Inserir item em posição existente')

    ComandoDoUsuario = input(f'\n{cores["verde"]}Seu Comando ?:{cores["padrao"]} ').upper()  
    if validar_comando(ComandoDoUsuario):
        menu_categoria_insercao(ComandoDoUsuario)


def menu_categoria_insercao(comando):
    limpar_console()

    if comando == 'A':
        item = input(f'{cores["verde"]}Item a adicionar:{cores["padrao"]} ')
        if not procurar_itens_iguais(item):
            inserir_item(item, None)

    if comando == 'B':
        try:
            Indice = int(input(f'{cores["verde"]}ÍNDICE do item:{cores["padrao"]} '))
            if validar_indice(Indice):
                item = input(f'{cores["verde"]}Item a adicicionar:{cores["padrao"]} ')
                if not procurar_itens_iguais(item):
                    inserir_item(item, Indice)

        except (TypeError, ValueError) as erro:
            avisar_erro(erro)


def menu_pesquisar():
    limpar_console()

    print(f'{cores["azul"]}A{cores["padrao"]} - Pesquisar por item na lista')
    print(f'{cores["azul"]}B{cores["padrao"]} - Pesquisar por posição existente na lista')

    ComandoDoUsuario = input(f'\n{cores["verde"]}Seu Comando ?:{cores["padrao"]} ').upper()  
    if validar_comando(ComandoDoUsuario):
        menu_categoria_pesquisa(ComandoDoUsuario)


def menu_categoria_pesquisa(comando):
    limpar_console()

    if comando == 'A':
        item = input(f'{cores["verde"]}Item a pesquisar:{cores["padrao"]} ')
        pesquisar_item(item, None)

    if comando == 'B':
        try:
            Indice = int(input(f'{cores["verde"]}Índice a pesquisar:{cores["padrao"]} '))
            if validar_indice(Indice):
                pesquisar_item(None, Indice)
                
        except (TypeError, ValueError) as erro:
            avisar_erro(erro)


def menu_excluir():
    limpar_console()

    print(f'{cores["azul"]}A{cores["padrao"]} - Excluir item na lista')
    print(f'{cores["azul"]}B{cores["padrao"]} - Excluir por posição existente na lista')

    ComandoDoUsuario = str(input(f'\n{cores["verde"]}Seu Comando ?:{cores["padrao"]} ')).upper()  
    if validar_comando(ComandoDoUsuario):
        menu_categoria_exclusao(ComandoDoUsuario)


def menu_categoria_exclusao(comando):
    limpar_console()

    if comando == 'A':
        item = input(f'{cores["verde"]}Item a excluir:{cores["padrao"]} ')
        excluir_item(item, None)

    if comando == 'B':
        try:
            Indice = int(input(f'{cores["verde"]}Índice a excluir:{cores["padrao"]} '))
            if validar_indice(Indice):
                excluir_item(None, Indice)

        except (TypeError, ValueError) as erro:
            avisar_erro(erro)


def menu_arquivar():
    limpar_console()
    print(f'{cores["azul"]}A{cores["padrao"]} - Gerar arquivo de texto')
    print(f'{cores["azul"]}B{cores["padrao"]} - Inserir itens de arquivo de texto')

    ComandoDoUsuario = input(f'\n{cores["verde"]}Seu comando ?: {cores["padrao"]}').upper()
    if validar_comando(ComandoDoUsuario):
        if ComandoDoUsuario == 'A':
            if len(lista) > 0:
                menu_categoria_arquivamento(ComandoDoUsuario)
            else:
                avisar_erro(2)
        else:
            menu_categoria_arquivamento(ComandoDoUsuario)
            


def menu_categoria_arquivamento(comando):
    limpar_console()
    if comando == 'A':
        gerar_arquivo()

    if comando == 'B':
        NomeArquivo = input(f'{cores["verde"]}Nome do arquivo: {cores["padrao"]}')
        ler_arquivo(NomeArquivo)


def main():
    while True:
        ComandoDoUsuario = menu_principal()

        match ComandoDoUsuario:
            case '0':
                break
            case '1':
                menu_inserir()
            case '2':
                menu_pesquisar()
            case '3':
                menu_excluir()
            case '4':
                mostrar_lista()
            case '5':
                menu_arquivar()

        if not(ComandoDoUsuario in ['1','2','3','4','5']):
            avisar_erro(0)


# ========================================================================================
#   3. EXECUÇÃO DO PROGRAMA
# ========================================================================================


if __name__ == '__main__':
    main()
