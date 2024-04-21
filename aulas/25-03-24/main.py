from pilha import Pilha_estatica
from os import system


'''=======================================================================
    FUNÇÕES DE SERVIÇO
======================================================================='''


def limpar_console():
    system('cls')
    
    
def avisar_usuario(tipo_aviso):
    limpar_console()
    match tipo_aviso:
        case 0:
            print(f'Erro: Tamanho INVÁLIDO')
        case 1:
            print(f'Pilha CRIADA')
        case _:
            print(f"ERRO: {tipo_aviso}")
            
    TerminarAviso = input('\nPressione "ENTER" para continuar ')
            


def criar_pilha(tamanho):
    NovaPilha = Pilha_estatica(tamanho)
    return NovaPilha


def adicionar_elemento(Pilha, elemento):    
    limpar_console()
    Pilha.empilhar(elemento)
    TerminarAviso = input('\nPressione "ENTER" para continuar ')


def remover_ultimo_elemento(pilha):
    limpar_console()
    ElementoRemovido = pilha.desempilhar()
    
    print(f"Elemento {ElementoRemovido} REMOVIDO")
    TerminarAviso = input('\nPressione "ENTER" para continuar ')
    

def verificar_pilha_cheia(pilha):
    limpar_console()
    if pilha.cheia():
        print(f"Pilha está CHEIA")
    else:
        print(f"Pilha NÃO está CHEIA")
    TerminarAviso = input('\nPressione "ENTER" para continuar ')
    
    
def verificar_pilha_vazia(pilha):
    limpar_console()
    if pilha.vazia():
        print(f"Pilha está VAZIA")
    else:
        print(f"Pilha NÃO está VAZIA")
    TerminarAviso = input('\nPressione "ENTER" para continuar ')
    
    
'''=======================================================================
    FUNÇÕES DE MENUS
======================================================================='''


def menu_criar_pilha(Pilha):
    limpar_console()
    
    try:
        TamanhoPilha = int(input(f"Tamanho da pilha: "))
        Pilha = criar_pilha(TamanhoPilha)
        avisar_usuario(1)
    
    except (ValueError, TypeError) as Erro:
        avisar_usuario(0)
        return None


def menu_adicionar(pilha):
    limpar_console()
    UltimoElemento = input("Elemento a adicionar: ")
    adicionar_elemento(pilha, UltimoElemento)
    

def menu_remover(pilha):
    limpar_console()
    remover_ultimo_elemento(pilha)
    
        

def menu_principal():
    limpar_console()
    print(f"1 - Criar pilha")
    print(f"2 - Adicionar elementos")
    print(f"3 - Remover último elemento")
    print(f"4 - Imprimir pilha")
    print(f"5 - Pilha cheia")
    print(f"6 - Pilha vazia")
    print(f"7 - Quantidade de elementos")
    print(f"0 - Sair do programa")
    
    Comando = input('\nSeu comando: ')
    return Comando
    

def main():
    Pilha = None
    while True:
        Comando = menu_principal()
        
        if Comando == '0':
            break
        
        match Comando:
            case '1':
                menu_criar_pilha(Pilha)
                print(Pilha)
                tipo = input('Esperando...')
            case '2':
                menu_adicionar(Pilha)
            case '3':
                menu_remover(Pilha)
            case '4':
                print()
            case '5':
                verificar_pilha_cheia(Pilha)
            case '6':
                verificar_pilha_vazia(Pilha)
            case '7':
                print()
    
    
'''=======================================================================
    EXECUÇÃO DO PROGRAMA
======================================================================='''
    
    
if __name__ == "__main__":
    main()