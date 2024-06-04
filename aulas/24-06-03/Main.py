from ArvoreBinaria import ArvoreBinaria

def main():
    raiz = ArvoreBinaria(43)

    raiz.alterar_esquerda(ArvoreBinaria(chave=11, esquerda=ArvoreBinaria(9), direita=ArvoreBinaria(41)))
    raiz.alterar_direita(ArvoreBinaria(chave=62, esquerda=ArvoreBinaria(48), direita=ArvoreBinaria(95)))
    # {43:{11:{9,41},}}
    print(raiz.existe_na_arvore(-17))


if __name__ == "__main__":
    main()