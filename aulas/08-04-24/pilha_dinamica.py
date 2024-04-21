from collections import deque
from os import system

def limpar_console():
    system('cls')


def receber_equacao():
    return input('Entrada: ')


def receber_parentese(pilha_dinamica, equacao):
    for elemento in equacao:
        if elemento == '(':
            pilha_dinamica.append('(')


def tirar_parentese(pilha_dinamica):
    pilha_dinamica.pop()


def conferir_balanceamento_equacao(pilha_dinamica, equacao):
    for elemento in equacao:
        if elemento == ')':
            if len(pilha_dinamica) == 0:
                return False
            else:
                tirar_parentese(pilha_dinamica) 
                
    if len(pilha_dinamica) == 0:
        return True
    else:
        return False
                        

def avisar_resultado(problema_encontrado):
    if problema_encontrado:
        print('Equação balanceada')
    else:
        print('Equação NÃO balanceada')


def receber_resposta_usuario():
    while True:
        limpar_console()
        resposta_usuario = input('Deseja recomeçar ? (S - Sim || N - Não): ').upper()
        match resposta_usuario:
            case 'S': return False
            case 'N': return True
            case _: input('Resposta Inváida - Enter para continuar...') 
            

def main():
    while True:
        limpar_console()
        pilha = deque()
        equacao = receber_equacao()
        receber_parentese(pilha, equacao)
        resultado = conferir_balanceamento_equacao(pilha, equacao)
        avisar_resultado(resultado)
        
        input('\nPrescione "ENTER" para continuar...')
        
        resposta_usuario = receber_resposta_usuario()
        if resposta_usuario:
            break
        

if __name__ == "__main__":
    main()
