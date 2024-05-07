from os import system

def limpar_console():
    system('cls')


def fruta_valido(fruta):
    return fruta != '' and not fruta is None


def preco_valido(preco):
    return not preco is None


def quantidade_valida(quantidade):
    return not quantidade is None


def obter_preco():
    try:
        preco = float(input('Valor preco: '))
        return preco
    except (TypeError, ValueError) as erro:
      print(erro)
      return None  
    
    
def obter_fruta():
    fruta = input('Fruta: ')
    return fruta


def obter_quantidade():
    try:
        quantidade = float(input('Quantidade fruta: '))
        return quantidade
    except (TypeError, ValueError) as erro:
      print(erro)
      return None  


def controlar_repeticao():
    limpar_console()
    resposta_usuario = input('Deseja continuar?(S: Sim||N: Não): ').upper()
    return resposta_usuario == 'S'


def mostrar_relacao_fruta_preco_quantidade(frutas, quantidades, precos):
    quantidade_frutas = len(frutas)
    print(f"{f'{"Fruta:":<30}'} {f'{"Qtde Estoque":<12}'} {f'{"Preço Kg":>12}'}")
    for i in range(quantidade_frutas):
        print(f'{frutas[i]:<30} {quantidades[i]:<10,.2f} {precos[i]:>10,.2f}')


def maior_quantidade_e_fruta(frutas, quantidades, precos):
    quantidade = max(quantidades)
    index = quantidades.index(quantidade)
    fruta = frutas[index]
    preco = precos[index]
    return fruta, quantidade, preco


def menor_quantidade_e_fruta(frutas, quantidades, precos):
    quantidade = min(quantidades)
    index = quantidades.index(quantidade)
    fruta = frutas[index]
    preco = precos[index]
    return fruta, quantidade, preco


def mostrar_relacao_maior_e_menor(frutas, quantidades, precos):
    fruta = []
    quantidade = []
    preco = []
    
    fruta_menor_quantidade, menor_quantidade, preco_menor_quantidade = menor_quantidade_e_fruta(frutas, quantidades, precos)  
    fruta_maior_quantidade, maior_quantidade, preco_maior_quantidade = maior_quantidade_e_fruta(frutas, quantidades, precos)
    
    fruta.append(fruta_maior_quantidade)
    fruta.append(fruta_menor_quantidade)
    quantidade.append(maior_quantidade)
    quantidade.append(menor_quantidade)
    preco.append(preco_maior_quantidade)
    preco.append(preco_menor_quantidade)
    
    mostrar_relacao_fruta_preco_quantidade(fruta, quantidade, preco)


frutas = []
quantidades = []
precos = []
usuario_querer_repeticao = True
while usuario_querer_repeticao:
    limpar_console()
    fruta = obter_fruta()
    quantidade = obter_quantidade()
    preco = obter_preco()
    if fruta_valido(fruta) and preco_valido(preco):
        frutas.append(fruta)
        quantidades.append(quantidade)
        precos.append(preco)
        usuario_querer_repeticao = controlar_repeticao()
    else:
        input('fruta ou valor de preco INVÁLIDO')
        
limpar_console()
print(f'{" RESULTADO ":=^72}')
mostrar_relacao_fruta_preco_quantidade(frutas, quantidades, precos)

print(f'\n{" MAIOR E MENOR QUANTIDADE ":=^72}')
mostrar_relacao_maior_e_menor(frutas, quantidades, precos)
