from os import system

def limpar_console():
    system('cls')


def obter_estado():
    estado = input('Estado: ')
    return estado.upper()


def obter_capital():
    capital = input('capital: ')
    return capital.upper()


def cadastrar_estado(pais):
    estado = obter_estado()
    capital = obter_capital()
    pais[estado] = capital


def validar_estado(estado, pais):
    return estado in pais


def pesquisar_capital(pais):
    estado = input('Pesquisar a capital de qual estado?: ').upper()
    if validar_estado(estado, pais):
        capital = pais[estado]
    else:
        capital = 'Erro: estado não encontrado'
    return capital


def alterar_capital(pais):
    estado = input('Alterar a capital de qual estado?: ').upper()
    if validar_estado(estado, pais):
        capital = input(f'Nova capital para {estado}: ').upper()
        pais.update({estado:capital})
    else:
        print('Erro: estado não encontrado')


def mostrar_estados(pais):
    if len(pais) != 0:
        print(f'{"ESTADO":<30}{"CAPITAL":>30}')
        for estado in pais.keys():
            print(f'{estado:<30}{pais[estado]:>30}')
    else:
        print('Sem estados cadastrados')


def main():
    pais = {}
    while True:
        limpar_console()
        print('1 - Adicionar estado')
        print('2 - Pesquisar capital de estado')    
        print('3 - Alterar capital')
        print('4 - Mostrar estados')
        print('5 - Sair')
        resposta = input('\nSeu comando: ')
        
        if resposta == '5':
            break
        
        match resposta:
            case '1': 
                limpar_console()
                cadastrar_estado(pais)
                input('\nEstado Cadastrado... ')
            case '2':
                limpar_console()
                capital = pesquisar_capital(pais)
                print(f'A capital desse estado é: {capital}')
                input('\nTentativa de pesquisa completa...')
            case '3': 
                limpar_console()
                alterar_capital(pais)
                input('\nTentativa de alteração completa...')
            case '4':
                limpar_console()
                mostrar_estados(pais)
                input('\nSeu comando...')
                
            
if __name__ == "__main__":
    main()