class Pilha_estatica:
    def __init__(self, tamanho):
        self.Tamaho = tamanho
        self.UltimoIndice = -1
        self.Pilha = [None] * tamanho
        
    def vazia(self):
        return self.UltimoIndice == -1
    
    def cheia(self):
        return self.UltimoIndice == self.Tamanho - 1
    
    def empilhar(self, elemento):
        if self.cheia():
            print(f'\nERRO: Lista cheia')
        self.Pilha.append(elemento)
        self.UltimoIndice += 1 
       
    def desempilhar(self):
        if self.vazia():
            print(f'\nERRO: Lista vazia')
            return None
        ElementoRetirado = self.Pilha.pop(self.Pilha.UltimoIndice)
        self.UltimoIndice -= 1
        return ElementoRetirado
