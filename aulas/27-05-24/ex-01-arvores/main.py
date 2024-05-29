from ArvoreBinaria import ArvoreBinaria


def tem_esquerda(no):
    return no.esquerda is not None


def tem_direita(no):
    return no.direita is not None


def tem_filhos(no):
    return tem_esquerda(no) or tem_direita(no)


def valor_e_igual(valor, no):
    return valor == no.chave


def valor_e_maior(valor, no):
    return valor > no.chave


def valor_e_menor(valor, no):
    return valor < no.chave


def obter_no_direito_se_existir(no):
    if tem_direita(no):
        no = no.obter_direita()
        return no


def obter_no_esquerdo_se_existir(no):
    if tem_esquerda(no):
        no = no.obter_esquerda()
        return no


def obter_no_mais_proximo_da_pesquisa(pesquisa, no):
    if valor_e_maior(pesquisa, no):
        no = obter_no_direito_se_existir(no)
    if valor_e_menor(pesquisa, no):
        no = obter_no_esquerdo_se_existir(no)
    return no


def existe_na_arvore(pesquisa, raiz):
    no = raiz
    while True:
        if valor_e_igual(pesquisa, no):
            return True
        if tem_filhos(no):
            no = obter_no_mais_proximo_da_pesquisa(pesquisa, no)
        else:
            return False


def main():
    raiz = ArvoreBinaria(43)

    raiz.alterar_esquerda(ArvoreBinaria(chave=11, esquerda=ArvoreBinaria(9), direita=ArvoreBinaria(41), pai=raiz))
    raiz.alterar_direita(ArvoreBinaria(chave=62, esquerda=ArvoreBinaria(48), direita=ArvoreBinaria(95), pai=raiz))

    print(existe_na_arvore(45,raiz))


if __name__ == '__main__':
    main()
