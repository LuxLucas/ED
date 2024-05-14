from os import system

def limpar_console():
    system('cls')


def obter_nome_funcionario():
    nome = input('Nome do funcionário: ')
    return nome


def obter_codigo_funcionario():
    codigo = input('Código do funcionário: ')
    return codigo


def criar_funcionario():
    funcionario = {}
    nome = obter_nome_funcionario()
    codigo = obter_codigo_funcionario()
    funcionario[codigo] = nome
    return funcionario


def cadastrar_grupo_funcionarios():
    grupo_funcionario = {}
    quantidade_cadastros = int(input('Quantos deseja cadastrar?: '))
    for i in range(quantidade_cadastros):
        limpar_console()
        grupo_funcionario[i] = criar_funcionario()
    return grupo_funcionario


def exibir_grupo(grupo_funcionarios):
    tamanho_grupo = grupo_funcionarios.keys
    return tamanho_grupo


def validar_demissao(grupo, chave):
    return chave in grupo


def demitir_funcionario(grupo_funcionarios):
    while True:
        limpar_console()
        print(f'Funcionário cadastrados: {exibir_grupo(grupo_funcionarios)}')
        escolha_demissao = int(input(f'Quem demitir?: '))
        if validar_demissao(escolha_demissao):
            del grupo_funcionarios[escolha_demissao]
            break
        
        
def obter_resposta():
    resposta = input('Deseja continuar? (S:SIM | N:NÃO)').upper() == 'S'
    return resposta


limpar_console()
grupo = cadastrar_grupo_funcionarios()
resposta_usuario = True
while resposta_usuario:
    quantidade_funcionario = exibir_grupo(grupo)
    demitir_funcionario(grupo)
    resposta_usuario = obter_resposta()
limpar_console()
print(grupo)