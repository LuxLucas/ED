class ArvoreBinaria:
    def __init__(self, chave, esquerda=None, direita=None, pai=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai

    def obter_chave(self):
        return self.chave

    def obter_direita(self):
        return  self.direita

    def obter_esquerda(self):
        return self.esquerda
    
    def obter_pai(self):
        return self.pai
    
    def alterar_chave(self, nova_chave):
        self.chave = nova_chave

    def alterar_direita(self, nova_direita):
        self.direita = nova_direita

    def alterar_esquerda(self, nova_esquerda):
        self.esquerda = nova_esquerda

    def aletrar_pai(self, novo_pai):
        self.pai = novo_pai

    def __repr__(self):
        return '{} <- {} -> {}'.format(self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)
