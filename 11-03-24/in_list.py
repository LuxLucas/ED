lista = [1, 2, 6, 67, 90]

#   Comandos apresentados:
#       - in

#   Pega posição do elemento
'''while True:
    try:
        elemento = int(input('Número a procurar: '))
        break
    except (TypeError, ValueError) as erro:
        print(f'{"CARACTER INVÁLIDO":=^50}')

if elemento in lista:
    posicao = lista.index(elemento)
    print(f'Elemento na lista, sua posição é {posicao}')
else:
    print(f'{"ELEMENTO NÃO ENCONTRADO":=^50}')'''
    
#   Pega elemento pela posição

posicao = int(input('Pesquisar posição: '))

if 0>posicao>len(lista):
    print(f'Caráctere inválido')
else:
    print(f'Elemento da posição: {lista[posicao]}')