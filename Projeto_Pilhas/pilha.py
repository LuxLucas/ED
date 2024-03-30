class Pilha:
    def __init__(self, comprimento):
        self.tamanho = comprimento
        self.ultimo_indice = -1
        self.pilha = []
        
    def vazia(self):
        return self.ultimo_indice == -1
    
    def cheia(self):
        return self.ultimo_indice == self.tamanho - 1
    
    def empilhar(self, elemento):
        if self.cheia():
            print(f'\nERRO: Lista cheia')
        else:
            self.pilha.append(elemento)
            self.ultimo_indice += 1
       
    def desempilhar(self):
        if self.vazia():
            print(f'\nERRO: Lista vazia')
        else:
            elemento_retirado = self.pilha.pop(self.ultimo_indice)
            self.ultimo_indice -= 1
            return elemento_retirado
