from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()
    
    def enfileirar(self, elemento):
        self.fila.append(elemento)
    
    def desenfileirar(self):
        if not self.is_vazio():
            self.fila.popleft()

    def tamanho(self):
        tamanho = len(self.fila)
        return tamanho
    
    def is_vazio(self):
        estado_fila = self.tamanho() == 0
        return estado_fila
    
    def obter_primeiro_elemento(self):
        if not self.is_vazio():
            primeiro_elemento = self.fila[0]
            return primeiro_elemento
        else:
            return None
        
