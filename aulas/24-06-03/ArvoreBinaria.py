class ArvoreBinaria:
    def __init__(self, chave, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def obter_chave(self):
        return self.chave

    def obter_direita(self):
        return  self.direita

    def obter_esquerda(self):
        return self.esquerda

    def alterar_chave(self, nova_chave):
        self.chave = nova_chave

    def alterar_direita(self, nova_direita):
        self.direita = nova_direita

    def alterar_esquerda(self, nova_esquerda):
        self.esquerda = nova_esquerda

    def tem_esquerda(self):
        return self.esquerda is not None

    def tem_direita(self):
        return self.direita is not None

    def tem_filhos(self):
        return self.tem_esquerda() or self.tem_direita()

    def valor_e_igual(self, valor):
        return valor == self.chave

    def valor_e_maior(self, valor):
        return valor > self.chave

    def valor_e_menor(self, valor):
        return valor < self.chave

    def obter_no_direito_se_existir(self):
        if self.tem_direita():
            no_direito = self.obter_direita()
            return no_direito

    def obter_no_esquerdo_se_existir(self):
        if self.tem_esquerda():
            no_esquerdo = self.obter_esquerda()
            return no_esquerdo

    def obter_no_mais_proximo_da_pesquisa(self, pesquisa):
        if self.valor_e_maior(pesquisa):
            no = self.obter_no_direito_se_existir()
        if self.valor_e_menor(pesquisa):
            no = self.obter_no_esquerdo_se_existir()
        return no

    def existe_na_arvore(self, pesquisa):
        no = self
        while not no is None:
            if no.valor_e_igual(pesquisa):
                return True
            if no.tem_filhos():
                no = no.obter_no_mais_proximo_da_pesquisa(pesquisa)
            else:
                return False
            
    def adicionar_no(self, novo_no):
        no_pai = self.obter_no_mais_proximo_da_pesquisa()
        if self.valor_e_maior(novo_no):
            

    def __repr__(self):
        return '{} <- {} -> {}'.format(self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)