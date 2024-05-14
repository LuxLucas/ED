from os import system

def limpar_console():
    system('cls')


def obter_estado():
    estado = input('Estado: ')
    return estado


def obter_capital():
    capital = input('capital: ')
    return capital


def cadastrar_estado(pais):
    estado = obter_estado()
    capital = obter_capital()
    pais[estado] = capital


def validar_estado(estado, pais):
    return estado in pais


def pesquisar_capital(pais):
    estado = input('Capital de qual estado? ')
    if validar_estado(estado, pais):
        capital = pais[estado]
    capital = 'Erro: capital não encontrada'
    print(capital)


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
                input('Seu comando?... ')
            case '2':
                limpar_console()
                capital = pesquisar_capital(pais)
                input('Seu comando?... ')
            case '3': 
                limpar_console()

            case '4':
                limpar_console()
                print(pais)
                input()
                
            
if __name__ == "__main__":
    main()