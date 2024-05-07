from os import system

def limpar_console():
    system('cls')


def veiculo_valido(veiculo):
    return veiculo != '' and not veiculo is None


def ano_valida(ano):
    return not ano is None


def obter_ano():
    try:
        ano = int(input('Ano: '))
        return ano
    except (TypeError, ValueError) as erro:
      print(erro)
      return None  
    
    
def obter_veiculo():
    veiculo = input('Veiculo: ')
    return veiculo


def controlar_repeticao():
    limpar_console()
    resposta_usuario = input('Deseja continuar?(S: Sim||N: Não): ').upper()
    return resposta_usuario == 'S'


def mostrar_relacao_veiculo_ano(lista_veiculos, lista_anos):
    quantidade_veiculos = len(lista_veiculos)
    print(f'{f'{"Veículo:":<50}'} {f'{"Ano:":^4}'}')
    for i in range(quantidade_veiculos):
        print(f'{lista_veiculos[i]:<50} {lista_anos[i]:^4}')


def maior_ano_e_veiculo(lista_veiculos, lista_anos):
    maior_ano = max(lista_anos)
    index = lista_anos.index(maior_ano)
    veiculo = lista_veiculos[index]
    return veiculo, maior_ano


def menor_ano_e_veiculo(lista_veiculos, lista_anos):
    menor_ano = min(lista_anos)
    index = lista_anos.index(menor_ano)
    veiculo = lista_veiculos[index]
    return veiculo, menor_ano


def mostrar_relacao_maior_e_menor(lista_veiculos, lista_anos):
    veiculos = []
    anos = []
    
    veiculo, maior_ano = maior_ano_e_veiculo(lista_veiculos, lista_anos)
    veiculos.append(veiculo)
    anos.append(maior_ano)
    
    veiculo, menor_ano = menor_ano_e_veiculo(lista_veiculos, lista_anos)
    veiculos.append(veiculo)
    anos.append(menor_ano)
    
    mostrar_relacao_veiculo_ano(veiculos, anos)


def obter_primeiro_veiculo(lista_veiculo, lista_ano):
    primeiro_veiculo = lista_veiculo[0]
    ano = lista_ano[0]
    return primeiro_veiculo, ano


def obter_ultimo_veiculo(lista_veiculo, lista_ano):
    ultimo_veiculo = lista_veiculo[-1]
    ano = lista_ano[-1]
    return ultimo_veiculo, ano


def mostrar_primeiro_e_ultimo_veiculo(lista_veiculo, lista_ano):
    veiculos = []
    anos = []
    
    primeiro_veiculo, ano = obter_primeiro_veiculo(lista_veiculo, lista_ano)
    veiculos.append(primeiro_veiculo)
    anos.append(ano)
    
    ultimo_veiculo, ano = obter_ultimo_veiculo(lista_veiculo, lista_ano)
    veiculos.append(ultimo_veiculo)
    anos.append(ano)
    
    mostrar_relacao_veiculo_ano(veiculos, anos)


veiculos = []
anos = []
usuario_querer_repeticao = True
while usuario_querer_repeticao:
    limpar_console()
    veiculo = obter_veiculo()
    ano = obter_ano()
    if veiculo_valido(veiculo) and ano_valida(ano):
        veiculos.append(veiculo)
        anos.append(ano)
        usuario_querer_repeticao = controlar_repeticao()
    else:
        input('veiculo ou valor de ano INVÁLIDO')
        
limpar_console()
print(f'{" RESULTADO ":=^54}')
mostrar_relacao_veiculo_ano(veiculos, anos)

print(f'\n{" MAIOR E MENOR ANO ":=^54}')
mostrar_relacao_maior_e_menor(veiculos, anos)

print(f'\n{" PRIMEIRO E ÚLTIMO ":=^54}')
mostrar_primeiro_e_ultimo_veiculo(veiculos, anos)

print(f'\n{" QUANTIDADE DE VEÍCULOS CADASTRADOS ":=^54}')
print(len(veiculos))