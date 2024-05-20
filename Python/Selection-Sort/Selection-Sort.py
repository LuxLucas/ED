"""
Autores: Abdiel Paulino e Lucas Flôres
Método: Selection Sort
"""
from os import system

def limpar_console():
    system("cls")


def validar_repeticao(repeticao):
    return (not repeticao is None) and (repeticao >= 10)


def obter_repeticao():
    try:
        repeticao = float(input('Tamanho de repetição: '))
        if validar_repeticao(repeticao):
            return repeticao
        print(f"Erro: repetição menor que 10 (mínimo)")
        return None
    except (ValueError, TypeError) as erro:
        print(f"Erro: {erro}")
        return None


def obter_numero():
    try:
        numero = float(input('Seu número: '))
        return numero
    except (ValueError, TypeError) as erro:
        print(f"Erro: {erro}")
        return None


def selection_sort(lista):
    lista_ordenada = []
    lista_copia = lista
    tamanho_copia = len(lista_copia)
    while tamanho_copia != 0:
        menor = min(lista_copia)
        lista_ordenada.append(menor)
        lista_copia.remove(menor)
        tamanho_copia = len(lista_copia)
    return lista_ordenada

def main():
    repeticao = 0
    while True:
        repeticao = obter_repeticao()
        if validar_repeticao(repeticao):
            break

    lista = []
    tamanho_lista = len(lista)
    while tamanho_lista < repeticao:
        numero = obter_numero()
        if not numero is None:
            lista.append(numero)
            tamanho_lista = len(lista)

    limpar_console()
    print(f'{" RESULTADO ":=^65}')
    print(lista)
    print(selection_sort(lista))


if __name__ == "__main__":
    main()