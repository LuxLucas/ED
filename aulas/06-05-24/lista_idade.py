from os import system

def limpar_console():
    system('cls')


def idade_valida(idade):
    return not idade is None


def obter_idade():
    try:
        idade = int(input('Idade: '))
        if idade_valida(idade):
            return idade
        else:
            return None
    except (TypeError, ValueError) as erro:
        print(erro)
        return None
    
    
def controlar_repeticao():
    limpar_console()
    resposta_usuario = input('Deseja continuar?(S: Sim||N: Não): ').upper()
    return resposta_usuario == 'S'

while usuario_querer_