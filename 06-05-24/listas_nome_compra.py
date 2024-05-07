from os import system

def limpar_console():
    system('cls')


def nome_valido(nome):
    return nome != '' and not nome is None


def compra_valida(compra):
    return not compra is None


def obter_compra():
    try:
        compra = float(input('Valor compra: '))
        return compra
    except (TypeError, ValueError) as erro:
      print(erro)
      return None  
    
    
def obter_nome():
    nome = input('Nome cliente: ')
    return nome


def controlar_repeticao():
    limpar_console()
    resposta_usuario = input('Deseja continuar?(S: Sim||N: Não): ').upper()
    return resposta_usuario == 'S'


def mostrar_relacao_nome_compra(lista_nomes, lista_compras):
    quantidade_nomes = len(lista_nomes)
    print(f'{f'{"Nome Cliente:":<50}'} {f'{"Saldo Copra":<12}'}')
    for i in range(quantidade_nomes):
        print(f'{lista_nomes[i]:<50} {lista_compras[i]:<10,.2f}')


def maior_compra_e_nome_comprador(lista_nomes, lista_compras):
    maior_compra = max(lista_compras)
    index_maior_compra = lista_compras.index(maior_compra)
    nome_comprador = lista_nomes[index_maior_compra]
    return nome_comprador, maior_compra


def menor_compra_e_nome_comprador(lista_nomes, lista_compras):
    menor_compra = min(lista_compras)
    index_menor_compra = lista_compras.index(menor_compra)
    nome_comprador = lista_nomes[index_menor_compra]
    return nome_comprador, menor_compra


def mostrar_relacao_maior_e_menor(lista_nomes, lista_compras):
    nomes = []
    compras = []
    maior_comprador, maior_compra = maior_compra_e_nome_comprador(lista_nomes, lista_compras)
    nomes.append(maior_comprador)
    compras.append(maior_compra)
    
    menor_comprador, menor_compra = menor_compra_e_nome_comprador(lista_nomes, lista_compras)
    nomes.append(menor_comprador)
    compras.append(menor_compra)
    
    mostrar_relacao_nome_compra(nomes, compras)


nomes = []
compras = []
usuario_querer_repeticao = True
while usuario_querer_repeticao:
    limpar_console()
    nome = obter_nome()
    compra = obter_compra()
    if nome_valido(nome) and compra_valida(compra):
        nomes.append(nome)
        compras.append(compra)
        usuario_querer_repeticao = controlar_repeticao()
    else:
        input('Nome ou valor de compra INVÁLIDO')
        
limpar_console()
print(f'{" RESULTADO ":=^72}')
mostrar_relacao_nome_compra(nomes, compras)

print(f'\n{" MAIOR E MENOR SALDO ":=^72}')
mostrar_relacao_maior_e_menor(nomes, compras)

