from os import system

def limpar_console():
    system('cls')


def validar_identificador_do_funcionario(identificador_funcionario):
    return not identificador_funcionario is None

def obter_identificador_funcionario():
    try:
        identificador_funcionario = int(input('Qual demitir?: '))
        if validar_identificador_do_funcionario(identificador_funcionario):
            return identificador_funcionario
        return None
    except (TypeError, ValueError) as erro:
        print(f'Erro: {erro}')

def obter_quantidade(funcionarios):
    quantidade = funcionarios.keys()
    return quantidade


def obter_resposta():
    resposta = input('Deseja continuar?(S:SIM | N:NÃO): ').upper()
    return resposta == 'S'


funcionarios = {
    1: "Cleiton",
    2: "Fabiana",
    3: "Higor",
    4: "Flávia"
}


reposta_usuario = True
while reposta_usuario:
    limpar_console()
    quantidade = obter_quantidade(funcionarios)
    print(f'Há {quantidade} funcionários')
    identificador = obter_identificador_funcionario()
    print(identificador)
    input()
    if validar_identificador_do_funcionario(identificador):
        funcionarios.pop(identificador)
        resposta_usuario = obter_resposta()
        
print(sorted(funcionarios))
        
    